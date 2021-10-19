from typing import Dict

import attr
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class MatrixCompose(OMNode):
    def build(self):
        self._input_node = self.create_node(
            "composeMatrix",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node.name()}.useEulerRotation", False)

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
