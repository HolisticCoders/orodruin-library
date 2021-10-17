import attr
from typing import Dict
from maya import cmds
from orodruin_maya import OMNode


@attr.s
class VectorDot(OMNode):
    def build(self):
        self._input_node = cmds.createNode(
            "vectorProduct",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node}.operation", 1)

        self._output_node = self._input_node

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
