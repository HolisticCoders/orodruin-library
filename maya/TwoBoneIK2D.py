import attr
import cmdx
from orodruin_maya import OMGroupNode

from maya import cmds

EXPRESSION_TEMPLATE = """
float $pi = 3.141592654;

vector $base = <<{0}.baseX, {0}.baseY, {0}.baseZ>>;
vector $handle = <<{0}.handleX, {0}.handleY, {0}.handleZ>>;
float $bone_a_length = {0}.bone_a_length;
float $bone_b_length = {0}.bone_b_length;


// Compute the IK effector position.
vector $base_handle_vec = $handle - $base;
float $chain_length = $bone_a_length + $bone_b_length;
float $effector_vector_length = min($chain_length, mag($base_handle_vec));
vector $effector = unit($base_handle_vec) * $effector_vector_length;
float $effector_length = mag($effector);

// Compute the angle of the "a" point
float $cos_angle_a = ($bone_a_length * $bone_a_length + $effector_length * $effector_length - $bone_b_length * $bone_b_length) / (2 * $bone_a_length * $effector_length);
$cos_angle_a = clamp(-1, 1, $cos_angle_a);
float $angle_a = acos($cos_angle_a);

// Compute the angle of the "b" point
float $cos_angle_b = ($bone_a_length * $bone_a_length + $bone_b_length * $bone_b_length - $effector_length * $effector_length) / (2 * $bone_a_length * $bone_b_length);
$cos_angle_b = clamp(-1, 1, $cos_angle_b);
float $angle_b = acos($cos_angle_b);

{1}.angle_a = rad_to_deg($angle_a);
{1}.angle_b = rad_to_deg($angle_b - $pi);
"""


@attr.s
class TwoBoneIK2D(OMGroupNode):
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
        self._expression_node = cmdx.encode(
            cmds.expression(
                string=self._expression_template,
                name=self.__class__.__name__ + "_EXP",
            )
        )
        self._nodes.append(self._expression_node)

    def _create_maya_attributes(self) -> None:
        cmds.addAttr(self._input_node.name(), longName="base", attributeType="double3")
        cmds.addAttr(
            self._input_node.name(),
            longName="baseX",
            attributeType="double",
            parent="base",
        )
        cmds.addAttr(
            self._input_node.name(),
            longName="baseY",
            attributeType="double",
            parent="base",
        )
        cmds.addAttr(
            self._input_node.name(),
            longName="baseZ",
            attributeType="double",
            parent="base",
        )

        cmds.addAttr(
            self._input_node.name(), longName="handle", attributeType="double3"
        )
        cmds.addAttr(
            self._input_node.name(),
            longName="handleX",
            attributeType="double",
            parent="handle",
        )
        cmds.addAttr(
            self._input_node.name(),
            longName="handleY",
            attributeType="double",
            parent="handle",
        )
        cmds.addAttr(
            self._input_node.name(),
            longName="handleZ",
            attributeType="double",
            parent="handle",
        )

        cmds.addAttr(
            self._input_node.name(), longName="bone_a_length", attributeType="double"
        )
        cmds.addAttr(
            self._input_node.name(), longName="bone_b_length", attributeType="double"
        )

        cmds.addAttr(
            self._output_node.name(), longName="angle_a", attributeType="double"
        )
        cmds.addAttr(
            self._output_node.name(), longName="angle_b", attributeType="double"
        )
