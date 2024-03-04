# -*- coding: utf-8 -*-
"""Validate if instance asset is the same as context asset."""
from __future__ import absolute_import

import pyblish.api
import ayon_core.hosts.maya.api.action
from ayon_core.pipeline.publish import (
    RepairAction,
    ValidateContentsOrder,
    PublishValidationError,
    OptionalPyblishPluginMixin
)

from maya import cmds


class ValidateInstanceInContext(pyblish.api.InstancePlugin,
                                OptionalPyblishPluginMixin):
    """Validator to check if instance asset match context asset.

    When working in per-shot style you always publish data in context of
    current asset (shot). This validator checks if this is so. It is optional
    so it can be disabled when needed.

    Action on this validator will select invalid instances in Outliner.
    """

    order = ValidateContentsOrder
    label = "Instance in same Context"
    optional = True
    hosts = ["maya"]
    actions = [
        ayon_core.hosts.maya.api.action.SelectInvalidAction, RepairAction
    ]
    excluded_families = []

    def process(self, instance):
        families = instance.data["families"]
        excluded_product_type = set(families).intersection(self.excluded_families)
        if excluded_product_type:
            self.log.debug("Skipping Validate Instance In Context")
            return

        if not self.is_active(instance.data):
            return

        asset = instance.data.get("folderPath")
        context_asset = self.get_context_asset(instance)
        if asset != context_asset:
            raise PublishValidationError(
                message=(
                    "Instance '{}' publishes to different asset than current "
                    "context: {}. Current context: {}".format(
                        instance.name, asset, context_asset
                    )
                ),
                description=(
                    "## Publishing to a different asset\n"
                    "There are publish instances present which are publishing "
                    "into a different asset than your current context.\n\n"
                    "Usually this is not what you want but there can be cases "
                    "where you might want to publish into another asset or "
                    "shot. If that's the case you can disable the validation "
                    "on the instance to ignore it."
                )
            )

    @classmethod
    def get_invalid(cls, instance):
        return [instance.data["instance_node"]]

    @classmethod
    def repair(cls, instance):
        context_asset = cls.get_context_asset(instance)
        instance_node = instance.data["instance_node"]
        cmds.setAttr(
            "{}.folderPath".format(instance_node),
            context_asset,
            type="string"
        )

    @staticmethod
    def get_context_asset(instance):
        return instance.context.data["folderPath"]
