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
            "translateX": "outputTranslateX",
            "translateY": "outputTranslateY",
            "translateZ": "outputTranslateZ",
            "euler": "outputRotate",
            "eulerX": "outputRotateX",
            "eulerY": "outputRotateY",
            "eulerZ": "outputRotateZ",
            "quaternion": "outputQuat",
            "quaternionX": "outputQuatX",
            "quaternionY": "outputQuatY",
            "quaternionZ": "outputQuatZ",
            "quaternionW": "outputQuatW",
            "scale": "outputScale",
            "scaleX": "outputScaleX",
            "scaleY": "outputScaleY",
            "scaleZ": "outputScaleZ",
            "shear": "outputShear",
            "shearX": "outputShearX",
            "shearY": "outputShearY",
            "shearZ": "outputShearZ",
        }
