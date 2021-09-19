from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMComponent

@dataclass
class Remap(OMComponent):

    def build(self):
        self._input_node = cmds.createNode(
            "setRange",
            name=self._component.name(),
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input": "valueX",
            "old_min": "oldMinX",
            "old_max": "oldMaxX",
            "new_min": "minX",
            "new_max": "maxX",
            "output": "outValueX"
        }
