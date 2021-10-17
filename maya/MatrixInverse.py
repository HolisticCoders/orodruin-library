from typing import Dict

import attr
from orodruin_maya import OMNode, create_node

from maya import cmds


@attr.s
class MatrixInverse(OMNode):
    def build(self):
        self._input_node = create_node(
            "inverseMatrix",
            name=self._name,
        )

        self._output_node = self._input_node

        self._nodes.append(self._input_node)

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {"input": "inputMatrix", "output": "outputMatrix"}
