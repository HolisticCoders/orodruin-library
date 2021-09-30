from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode

@dataclass
class Power(OMNode):

    def build(self):
        self._input_node = cmds.createNode(
            "multiplyDivide",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node}.operation", 3)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input1": "input1X",
            "input2": "input2X",
            "output": "outputX"
        }
