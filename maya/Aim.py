from dataclasses import dataclass
from typing import Dict

from orodruin_maya import OMNode

from maya import cmds


@dataclass
class Aim(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "aimMatrix",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node}.primaryMode", 2)
        cmds.setAttr(f"{self._input_node}.secondaryMode", 2)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "base_matrix": "inputMatrix",
            "output": "outputMatrix",
            "aim_axis": "primaryInputAxis",
            "aim_axisX": "primaryInputAxisX",
            "aim_axisY": "primaryInputAxisY",
            "aim_axisZ": "primaryInputAxisZ",
            "aim_vector": "primaryTargetVector",
            "aim_vectorX": "primaryTargetVectorX",
            "aim_vectorY": "primaryTargetVectorY",
            "aim_vectorZ": "primaryTargetVectorZ",
            "up_axis": "secondaryInputAxis",
            "up_axisX": "secondaryInputAxisX",
            "up_axisY": "secondaryInputAxisY",
            "up_axisZ": "secondaryInputAxisZ",
            "up_vector": "secondaryTargetVector",
            "up_vectorX": "secondaryTargetVectorX",
            "up_vectorY": "secondaryTargetVectorY",
            "up_vectorZ": "secondaryTargetVectorZ",
        }
