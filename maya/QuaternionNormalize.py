from typing import Dict

import attr
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class QuaternionNormalize(OMNode):
    def build(self):
        self._input_node = self.create_node(
            "quatNormalize",
            name=self._name,
        )

        self._output_node = self._input_node

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "input": "inputQuat",
            "inputX": "inputQuatX",
            "inputY": "inputQuatY",
            "inputZ": "inputQuatZ",
            "inputW": "inputQuatW",
            "output": "outputQuat",
            "outputX": "outputQuatX",
            "outputY": "outputQuatY",
            "outputZ": "outputQuatZ",
            "outputW": "outputQuatW",
        }
