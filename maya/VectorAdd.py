from typing import Dict

import attr
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class VectorAdd(OMNode):
    def build(self):
        self._input_node = self.create_node(
            "plusMinusAverage",
            name=self._name,
        )
        cmds.setAttr(f"{self._input_node.name()}.operation", 1)

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input1": "input3D[0]",
            "input1X": "input3D[0].input3Dx",
            "input1Y": "input3D[0].input3Dy",
            "input1Z": "input3D[0].input3Dz",
            "input2": "input3D[1]",
            "input2X": "input3D[1].input3Dx",
            "input2Y": "input3D[1].input3Dy",
            "input2Z": "input3D[1].input3Dz",
            "output": "output3D",
            "outputX": "output3Dx",
            "outputY": "output3Dy",
            "outputZ": "output3Dz",
        }
