from dataclasses import dataclass
from typing import Dict

from orodruin_maya import OMNode

from maya import cmds


@dataclass
class QuaternionFromAxisAngle(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "axisAngleToQuat",
            name=self._name,
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "axis": "inputAxis",
            "axisX": "inputAxisX",
            "axisY": "inputAxisY",
            "axisZ": "inputAxisZ",
            "angle": "inputAngle",
            "output": "outputQuat",
            "outputX": "outputQuatX",
            "outputY": "outputQuatY",
            "outputZ": "outputQuatZ",
            "outputW": "outputQuatW",
        }
