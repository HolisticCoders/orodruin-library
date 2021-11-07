from typing import Dict

import attr
import cmdx
from orodruin.core import Port
from orodruin.core.utils import get_most_upstream_port
from orodruin_maya import OMNode

from maya import cmds


@attr.s
class Control(OMNode):
    def build(self):
        self._input_node = cmdx.encode(
            cmds.circle(
                constructionHistory=False,
                name=self._name,
            )[0]
        )

        self._output_node = self._input_node

        self._nodes.append(self._input_node)

    @staticmethod
    def maya_attribute_map() -> Dict[str, str]:
        """Return a dictionary mapping the ports names and their maya attributes."""
        return {
            "translate": "translate",
            "translateX": "translateX",
            "translateY": "translateY",
            "translateZ": "translateZ",
            "rotate": "rotate",
            "rotateX": "rotateX",
            "rotateY": "rotateY",
            "rotateZ": "rotateZ",
            "scale": "scale",
            "scaleX": "scaleX",
            "scaleY": "scaleY",
            "scaleZ": "scaleZ",
            "rest_matrix": "offsetParentMatrix",
            "inherits_transform": "inheritsTransform",
            "world_matrix": "worldMatrix[0]",
            "matrix": "matrix",
        }

    def on_connection_received(self, port: Port) -> None:
        if port.name() == "parent":
            upstream_port = get_most_upstream_port(port)
            parent_node = self._om_state.get_om_node(upstream_port.node())
            parent_maya_node = parent_node.input_node()

            if isinstance(parent_maya_node, cmdx.DagNode):
                parent_maya_node.add_child(self._input_node)

    def on_connection_removed(self, port: Port) -> None:
        if port.name() == "parent" and self._input_node.parent():
            cmds.parent(self._input_node.path(), world=True)
