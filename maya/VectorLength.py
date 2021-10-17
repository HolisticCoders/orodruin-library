import attr
from orodruin_maya import OMGroupNode, get_mobject

from maya import cmds

EXPRESSION_TEMPLATE = """
vector $input = <<{0}.inputX, {0}.inputY, {0}.inputZ>>;
{1}.output = mag($input);
"""


@attr.s
class VectorLength(OMGroupNode):
    _expression_template: str = attr.ib(init=False)
    _expression_node: str = attr.ib(init=False)

    def build(self) -> None:
        super().build()

        # The orodruin ports are created after the call to `build` but the maya
        # attributes need to exist before the creation of the expression node.
        self._create_maya_attributes()

        self._expression_template = EXPRESSION_TEMPLATE.format(
            self._input_node.name(), self._output_node.name()
        )
        self._expression_node = get_mobject(
            cmds.expression(
                string=self._expression_template,
                name=self.__class__.__name__ + "_EXP",
            )
        )

        self._nodes.append(self._expression_node)

    def _create_maya_attributes(self) -> None:
        cmds.addAttr(self._input_node.name(), longName="input", attributeType="double3")
        cmds.addAttr(
            self._input_node.name(),
            longName="inputX",
            attributeType="double",
            parent="input",
        )
        cmds.addAttr(
            self._input_node.name(),
            longName="inputY",
            attributeType="double",
            parent="input",
        )
        cmds.addAttr(
            self._input_node.name(),
            longName="inputZ",
            attributeType="double",
            parent="input",
        )
        cmds.addAttr(
            self._output_node.name(), longName="output", attributeType="double"
        )
