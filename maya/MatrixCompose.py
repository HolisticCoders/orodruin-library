from dataclasses import dataclass
from typing import Dict

from orodruin_maya import OMNode

from maya import cmds


@dataclass
class MatrixCompose(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "composeMatrix",
            name=self._name,
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "translate": "inputTranslate",
            "translateX": "inputTranslateX",
            "translateY": "inputTranslateY",
            "translateZ": "inputTranslateZ",
            "euler": "inputRotate",
            "eulerX": "inputRotateX",
            "eulerY": "inputRotateY",
            "eulerZ": "inputRotateZ",
            "quaternion": "inputQuat",
            "quaternionX": "inputQuatX",
            "quaternionY": "inputQuatY",
            "quaternionZ": "inputQuatZ",
            "quaternionW": "inputQuatW",
            "scale": "inputScale",
            "scaleX": "inputScaleX",
            "scaleY": "inputScaleY",
            "scaleZ": "inputScaleZ",
            "shear": "inputShear",
            "shearX": "inputShearX",
            "shearY": "inputShearY",
            "shearZ": "inputShearZ",
            "output": "outputMatrix",
        }
