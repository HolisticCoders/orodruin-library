from typing import Dict

import attr
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class Power(OMNode):
    def build(self):
        self._input_node = self.create_node(
            "multiplyDivide",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node.name()}.operation", 3)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {"input1": "input1X", "input2": "input2X", "output": "outputX"}
