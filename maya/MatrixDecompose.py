from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode

@dataclass
class MatrixDecompose(OMNode):

    def build(self):
        self._input_node = cmds.createNode(
            "decomposeMatrix",
            name=self._name,
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input": "inputMatrix",
            "translate": "outputTranslate",
            "euler_rotation": "outputRotate",
            "quaternion_rotation": "outputQuat",
            "shear": "outputShear",
            "scale": "outputScale",
        }
