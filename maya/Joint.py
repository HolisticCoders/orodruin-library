import attr
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode


@attr.s
class Joint(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "joint",
            name=self._name,
        )

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
