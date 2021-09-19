from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMComponent

@dataclass
class MatrixInverse(OMComponent):

    def build(self):
        self._input_node = cmds.createNode(
            "inverseMatrix",
            name=self._component.name(),
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input": "inputMatrix",
            "output": "outputMatrix"
        }
