from dataclasses import dataclass
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode

@dataclass
class Guide(OMNode):

    def build(self):
        self._input_node = cmds.spaceLocator(
            name=self._name,
        )[0]

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "translate": "translate",
            "rotate": "rotate",
            "scale": "scale",
            "rest_matrix": "offsetParentMatrix",
            "inherits_transform": "inheritsTransform",
            "world_matrix": "worldMatrix",
            "matrix": "matrix",
        }

