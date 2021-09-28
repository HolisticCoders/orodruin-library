from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode

@dataclass
class Average(OMNode):

    def build(self):
        self._input_node = cmds.createNode(
            "plusMinusAverage",
            name=self._node.name(),
        )
        cmds.setAttr(f"{self._input_node}.operation", 3)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input1": "input1D[0]",
            "input2": "input1D[1]",
            "output": "output1D"
        }

