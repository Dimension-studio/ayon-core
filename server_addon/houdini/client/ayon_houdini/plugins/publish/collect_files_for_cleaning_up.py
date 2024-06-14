import pyblish.api
import os
import clique
from ayon_core.pipeline import AYONPyblishPluginMixin
from ayon_houdini.api import lib, plugin


class CollectFilesForCleaningUp(plugin.HoudiniInstancePlugin,
                                AYONPyblishPluginMixin):
    """Collect Files For Cleaning Up.

    This collector collects output files
    and adds them to file remove list.

    CAUTION:
        This collector deletes the exported files and
          deletes the parent folder if it was empty.
        Artists are free to change the file path in the ROP node.
    """

    # It should run after CollectFrames and Collect Render plugins,
    # and before CollectLocalRenderInstances.
    order = pyblish.api.CollectorOrder + 0.115

    hosts = ["houdini"]
    families = ["*"]
    label = "Collect Files For Cleaning Up"
    intermediate_exported_render = False

    def process(self, instance):

        import hou

        node = hou.node(instance.data.get("instance_node", ""))
        if not node:
            self.log.debug("Skipping Collector. Instance has no instance_node")
            return

        output_parm = lib.get_output_parameter(node)
        if not output_parm:
            self.log.debug("ROP node type '{}' is not supported for cleaning up."
                           .format(node.type().name()))
            return

        filepath = output_parm.eval()
        if not filepath:
            self.log.warning("No filepath value to collect.")
            return

        files = []
        staging_dir, _ = os.path.split(filepath)

        expectedFiles = instance.data.get("expectedFiles", [])

        # 'expectedFiles' are preferred over 'frames'
        if expectedFiles:
            # Products with expected files
            # This can be Render products or submitted cache to farm.
            for expected in expectedFiles:
                # expected.values() is a list of lists
                files.extend(sum(expected.values(), []))
        else:
            # Products with frames or single file.
            frames = instance.data.get("frames", "")
            if isinstance(frames, str):
                # single file.
                files.append(filepath)
            else:
                # list of frame.
                files.extend(
                    ["{}/{}".format(staging_dir, f) for f in frames]
                )

        # Intermediate exported render files.
        # Note: This only takes effect when setting render target to
        #       "Farm Rendering - Split export & render jobs"
        #       as it's the only case where "ifdFile" exists in instance data.
        # TODO : Clean up intermediate files of Karma product type.
        #        as "ifdFile" works for other render product types only.
        ifdFile = instance.data.get("ifdFile")
        if self.intermediate_exported_render and ifdFile:
            start_frame = instance.data["frameStartHandle"]
            end_frame = instance.data["frameEndHandle"]
            ifd_files = self._get_ifd_file_list(ifdFile,
                                                start_frame, end_frame)
            files.extend(ifd_files)

        self.log.debug("Add directories to 'cleanupEmptyDir': {}".format(staging_dir))
        instance.context.data["cleanupEmptyDirs"].append(staging_dir)

        self.log.debug("Add files to 'cleanupFullPaths': {}".format(files))
        instance.context.data["cleanupFullPaths"].extend(files)

    def _get_ifd_file_list(self, ifdFile, start_frame, end_frame):

        file_name = os.path.basename(ifdFile)
        parent_path = os.path.dirname(ifdFile)

        # Compute frames list
        frame_collection, _ = clique.assemble(
            [file_name],
            patterns=[clique.PATTERNS["frames"]],
            minimum_items=1
        )

        # It's always expected to be one collection.
        frame_collection = frame_collection[0]
        frame_collection.indexes.clear()
        frame_collection.indexes.update(list(range(start_frame, (end_frame + 1))))

        result = [
                    "{}/{}".format(parent_path, frame)
                    for frame in frame_collection
        ]
        return result
