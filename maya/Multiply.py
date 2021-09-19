from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMComponent

@dataclass
class Multiply(OMComponent):

    def build(self):
        self._input_node = cmds.createNode(
            "multiplyDivide",
            name=self._component.name(),
        )
        cmds.setAttr(f"{self._input_node}.operation", 1)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input1": "input1X",
            "input2": "input2X",
            "output": "outputX"
        }
