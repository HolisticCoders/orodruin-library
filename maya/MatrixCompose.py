from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode

@dataclass
class MatrixCompose(OMNode):

    def build(self):
        self._input_node = cmds.createNode(
            "composeMatrix",
            name=self._node.name(),
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "translate": "inputTranslate",
            "euler_rotation": "inputRotate",
            "quaternion_rotation": "inputQuat",
            "scale": "inputScale",
            "shear": "inputShear",
            "output": "outputMatrix"
        }
