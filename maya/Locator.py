from typing import Dict

import attr
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class Locator(OMNode):
    def build(self):
        self._input_node = self.create_node("locator", name=self._name)
        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "translate": "translate",
            "translateX": "translateX",
            "translateY": "translateY",
            "translateZ": "translateZ",
            "rotate": "rotate",
            "rotateX": "rotateX",
            "rotateY": "rotateY",
            "rotateZ": "rotateZ",
            "scale": "scale",
            "scaleX": "scaleX",
            "scaleY": "scaleY",
            "scaleZ": "scaleZ",
            "rest_matrix": "offsetParentMatrix",
            "inherits_transform": "inheritsTransform",
            "world_matrix": "worldMatrix",
            "matrix": "matrix",
        }
