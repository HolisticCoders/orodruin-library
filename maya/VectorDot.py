from typing import Dict

import attr
from orodruin_maya import OMNode, create_node

from maya import cmds


@attr.s
class VectorDot(OMNode):
    def build(self):
        self._input_node = create_node(
            "vectorProduct",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node.name()}.operation", 1)

        self._output_node = self._input_node
        self._nodes.append(self._input_node)

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input1": "input1",
            "input1X": "input1X",
            "input1Y": "input1Y",
            "input1Z": "input1Z",
            "input2": "input2",
            "input2X": "input2X",
            "input2Y": "input2Y",
            "input2Z": "input2Z",
            "output": "output",
            "normalize": "normalizeOutput",
        }
