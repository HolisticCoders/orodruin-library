from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode


@dataclass
class Clamp(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "clamp",
            name=self._name,
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {"input": "inputR", "min": "minR", "max": "maxR", "output": "outputR"}
