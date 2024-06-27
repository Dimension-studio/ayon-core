import os

import clique
import pyblish.api
from ayon_core.pipeline import AYONPyblishPluginMixin
from ayon_houdini.api import plugin


class CollectFilesForCleaningUp(plugin.HoudiniInstancePlugin,
                                AYONPyblishPluginMixin):
    """Collect Files For Cleaning Up.

    This collector collects output files
    and adds them to file remove list.

    CAUTION:
        This collector registers exported files and
          the parent folder for deletion in `ExplicitCleanUp` plug-in.
          please refer to `ExplicitCleanUp`'s docstring for further info.

    Notes:
        Artists are free to change the file path in the ROP node.

        Farm instances will be processed on farm by other dedicated plugins
          that live in core addon e.g. `CollectRenderedFiles` plugin.
        These dedicated plugins don't support tracking and removing
          intermediated render files.

        Local Render instances don't track intermediated render files,
        Therefore, this plugin doesn't support removing
          intermediate render files.

        HDA is not added to this plugin's options in server settings.
        Cleaning up HDA products will break the scene as Houdini will no longer
          be able to find the HDA file.
        In addition,HDA plugins always save HDAs to external files.
        Therefore, Cleaning up HDA products will break the ability to go back
          to the workfile and continue on the HDA.
    """

    # It should run after CollectFrames and Collect Render plugins,
    # and before CollectLocalRenderInstances.
    order = pyblish.api.CollectorOrder + 0.115

    hosts = ["houdini"]
    families = ["*"]
    label = "Collect Files For Cleaning Up"

    def process(self, instance):

        if instance.data.get("farm"):
            self.log.debug("Should be processed on farm, skipping.")
            return

        files: list[os.PathLike] = []
        staging_dirs: list[os.PathLike] = []
        expected_files = instance.data.get("expectedFiles", [])

        # Prefer 'expectedFiles' over 'frames' because it usually contains more
        # output files than just a single file or single sequence of files.
        if expected_files:
            # Products with expected files
            # This can be Render products or submitted cache to farm.
            for expected in expected_files:
                # expected.values() is a list of lists
                for output_files in expected.values():
                    staging_dir, _ = os.path.split(output_files[0])
                    if staging_dir not in staging_dirs:
                        staging_dirs.append(staging_dir)
                    files.extend(output_files)
        else:
            # Products with frames or single file.

            frames = instance.data.get("frames")
            if frames is None:
                self.log.warning(
                    f"No frames data found on instance {instance}"
                    ". Skipping collection for caching on farm..."
                )
                return

            staging_dir = instance.data.get("stagingDir")
            staging_dirs.append(staging_dir)

            if isinstance(frames, str):
                # single file.
                files.append(f"{staging_dir}/{frames}")
            else:
                # list of frame.
                files.extend(
                    [f"{staging_dir}/{frame}" for frame in frames]
                )

        self.log.debug(
            f"Add directories to 'cleanupEmptyDir': {staging_dirs}")
        instance.context.data["cleanupEmptyDirs"].extend(staging_dirs)

        self.log.debug("Add files to 'cleanupFullPaths': {}".format(files))
        instance.context.data["cleanupFullPaths"].extend(files)

    def _get_ifd_file_list(self, ifd_file, start_frame, end_frame):

        file_name = os.path.basename(ifd_file)
        parent_path = os.path.dirname(ifd_file)

        # Compute frames list
        frame_collection, _ = clique.assemble(
            [file_name],
            patterns=[clique.PATTERNS["frames"]],
            minimum_items=1
        )

        # It's always expected to be one collection.
        frame_collection = frame_collection[0]
        frame_collection.indexes.clear()
        frame_collection.indexes.update(
            list(range(start_frame, (end_frame + 1))))

        return [f"{parent_path}/{frame}" for frame in frame_collection]
