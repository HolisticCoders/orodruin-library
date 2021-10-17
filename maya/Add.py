from typing import Dict

import attr
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class Add(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "plusMinusAverage",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node}.operation", 1)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {"input1": "input1D[0]", "input2": "input1D[1]", "output": "output1D"}
