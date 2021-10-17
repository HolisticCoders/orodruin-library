from typing import Dict

import attr
from orodruin_maya import OMNode, create_node

from maya import cmds


@attr.s
class MatrixMultiply(OMNode):
    def build(self):
        self._input_node = create_node(
            "multMatrix",
            name=self._name,
        )

        self._output_node = self._input_node

        self._nodes.append(self._input_node)

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {"input1": "matrixIn[0]", "input2": "matrixIn[1]", "output": "matrixSum"}
