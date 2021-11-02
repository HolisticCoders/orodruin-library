from typing import Dict

import attr
import cmdx
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class Locator(OMNode):
    def build(self):
        self._input_node = cmdx.encode(cmds.spaceLocator(name=self._name)[0])
        self._output_node = self._input_node
        self._nodes.append(self._input_node)

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
            "world_matrix": "worldMatrix[0]",
            "matrix": "matrix",
        }
