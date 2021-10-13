from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode


@dataclass
class QuaternionSlerp(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "quatSlerp",
            name=self._name,
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input1": "input1Quat",
            "input1X": "input1QuatX",
            "input1Y": "input1QuatY",
            "input1Z": "input1QuatZ",
            "input1W": "input1QuatW",
            "input2": "input2Quat",
            "input2X": "input2QuatX",
            "input2Y": "input2QuatY",
            "input2Z": "input2QuatZ",
            "input2W": "input2QuatW",
            "T": "inputT",
            "output": "outputQuat",
            "outputX": "outputQuatX",
            "outputY": "outputQuatY",
            "outputZ": "outputQuatZ",
            "outputW": "outputQuatW",
        }
