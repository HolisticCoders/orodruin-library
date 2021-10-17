import attr
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode


@attr.s
class MatrixInverse(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "inverseMatrix",
            name=self._name,
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {"input": "inputMatrix", "output": "outputMatrix"}
