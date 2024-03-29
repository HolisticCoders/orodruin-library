from typing import Dict

import attr
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class VectorNormalize(OMNode):
    def build(self):
        self._input_node = self.create_node(
            "vectorProduct",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node.name()}.operation", 0)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input": "input",
            "inputX": "inputX",
            "inputY": "inputY",
            "inputZ": "inputZ",
            "output": "output",
            "outputX": "outputX",
            "outputY": "outputY",
            "outputZ": "outputZ",
        }
