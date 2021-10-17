import attr, field

from orodruin_maya import OMGroupNode

from maya import cmds

EXPRESSION_TEMPLATE = """
vector $input = <<{0}.inputX, {0}.inputY, {0}.inputZ>>;
{1}.output = mag($input);
"""


@attr.s
class VectorLength(OMGroupNode):
    _expression_template: str = field(init=False)
    _expression_node: str = field(init=False)

    def build(self) -> None:
        super().build()

        # The orodruin ports are created after the call to `build` but the maya
        # attributes need to exist before the creation of the expression node.
        self._create_maya_attributes()

        self._expression_template = EXPRESSION_TEMPLATE.format(
            self._input_node, self._output_node
        )
        self._expression_node = cmds.expression(
            string=self._expression_template,
            name=self.__class__.__name__ + "_EXP",
        )

    def _create_maya_attributes(self) -> None:
        cmds.addAttr(self._input_node, longName="input", attributeType="double3")
        cmds.addAttr(
            self._input_node,
            longName="inputX",
            attributeType="double",
            parent="input",
        )
        cmds.addAttr(
            self._input_node,
            longName="inputY",
            attributeType="double",
            parent="input",
        )
        cmds.addAttr(
            self._input_node,
            longName="inputZ",
            attributeType="double",
            parent="input",
        )
        cmds.addAttr(self._output_node, longName="output", attributeType="double")
