import os
import pyblish.api
from pymxs import runtime as rt
from openpype.pipeline.publish import (
    RepairAction,
    ValidateContentsOrder,
    PublishValidationError,
    OptionalPyblishPluginMixin
)
from openpype.hosts.max.api.lib import get_current_renderer
from openpype.hosts.max.api.lib_rendersettings import RenderSettings


class ValidateRenderPasses(OptionalPyblishPluginMixin,
                           pyblish.api.InstancePlugin):
    """Validates Render Passes before Deadline Submission
    """

    order = ValidateContentsOrder
    families = ["maxrender"]
    hosts = ["max"]
    label = "Validate Render Passes"
    optional = True
    actions = [RepairAction]

    def process(self, instance):
        if not self.is_active(instance.data):
            return
        invalid = self.get_invalid(instance)
        if invalid:
            bullet_point_invalid_statement = "\n".join(
                f"- {err_type}: {filepath}" for err_type, filepath
                in invalid
            )
            report = (
                "Invalid render passes found.\n\n"
                f"{bullet_point_invalid_statement}\n\n"
                "You can use repair action to fix the invalid filepath."
            )
            raise PublishValidationError(
                report, title="Invalid Render Passes")

    @classmethod
    def get_invalid(cls, instance):
        """Function to get invalid beauty render outputs and
        render elements

        Args:
            instance (pyblish.api.Instance): instance
            filename (str): filename of the Max scene

        Returns:
            list: list of invalid filename which doesn't match
                with the project name
        """
        invalid = []
        file = rt.maxFileName
        filename, ext = os.path.splitext(file)
        if filename not in rt.rendOutputFilename:
            cls.log.error(
                "Render output folder "
                "doesn't match the max scene name! "
            )
            invalid_folder_name = os.path.dirname(
                rt.rendOutputFilename).replace(
                    "\\", "/").split("/")[-1]
            invalid.append(("Invalid Render Output Folder",
                            invalid_folder_name))
        beauty_fname = os.path.basename(rt.rendOutputFilename)
        ext = os.path.splitext(beauty_fname)[-1].lstrip(".")
        invalid_image_format = cls.get_invalid_image_format(
            cls, instance, ext)
        invalid.extend(invalid_image_format)
        renderer_class = get_current_renderer()
        renderer = str(renderer_class).split(":")[0]
        if renderer in [
            "ART_Renderer",
            "Redshift_Renderer",
            "V_Ray_6_Hotfix_3",
            "V_Ray_GPU_6_Hotfix_3",
            "Default_Scanline_Renderer",
            "Quicksilver_Hardware_Renderer",
        ]:
            render_elem = rt.maxOps.GetCurRenderElementMgr()
            render_elem_num = render_elem.NumRenderElements()
            for i in range(render_elem_num):
                renderlayer_name = render_elem.GetRenderElement(i)
                renderpass = str(renderlayer_name).split(":")[-1]
                rend_file = render_elem.GetRenderElementFilename(i)
                if not rend_file:
                    cls.log.error(f"No filepath for {renderpass}")
                    invalid.append((f"Invalid {renderpass}",
                                    "No filepath"))
                rend_fname, ext = os.path.splitext(
                    os.path.basename(rend_file))
                if not rend_fname.lstrip(".").endswith(renderpass):
                    err_msg = (
                        f"Filename for {renderpass} should be "
                        f"ended with {renderpass}"
                    )
                    cls.log.error(err_msg)
                    invalid.append((f"Invalid {renderpass}",
                                    os.path.basename(rend_file)))
                invalid_image_format = cls.get_invalid_image_format(
                    cls, instance, ext)
                invalid.extend(invalid_image_format)
        elif renderer == "Arnold":
            cls.log.debug(
                "Temporarily not support to check on Arnold render.")

        return invalid

    def get_invalid_image_format(self, instance, ext):
        """Function to check if the image format of the render outputs
        aligns with that in the setting.

        Args:
            instance (pyblish.api.Instance): instance
            ext (str): image extension

        Returns:
            list: list of files with invalid image format
        """
        invalid = []
        settings = instance.context.data["project_settings"].get("max")
        image_format = settings["RenderSettings"]["image_format"]
        if ext.lstrip(".") != image_format:
            msg = "Invalid image format for render outputs"
            self.log.error(msg)
            invalid.append((msg, ext.lstrip(".")))
        return invalid

    @classmethod
    def repair(cls, instance):
        container = instance.data.get("instance_node")
        RenderSettings().render_output(container)
        cls.log.debug("Reset the render output folder...")
