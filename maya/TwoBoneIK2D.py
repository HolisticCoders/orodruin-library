from dataclasses import dataclass, field

from orodruin_maya import OMGroupNode

from maya import cmds

EXPRESSION_TEMPLATE = """
float $pi = 3.141592654;

vector $a = <<{0}.point_aX, {0}.point_aY, {0}.point_aZ>>;
vector $b = <<{0}.point_bX, {0}.point_bY, {0}.point_bZ>>;
vector $c = <<{0}.point_cX, {0}.point_cY, {0}.point_cZ>>;
vector $handle = <<{0}.handleX, {0}.handleY, {0}.handleZ>>;

vector $ab = $b - $a;
vector $bc = $c - $b;
vector $ac = $c - $a;

// Compute the IK effector position.
float $chain_length = mag($ab) + mag($bc);
float $effector_vector_length = min($chain_length, mag($handle));
vector $effector = unit($handle) * $effector_vector_length;
vector $effector_vector = $effector - $a;

float $ab_length = mag($ab);
float $bc_length = mag($bc);
float $effector_length = mag($effector_vector);

// Compute the angle of the "a" point
float $cos_angle_a = ($ab_length * $ab_length + $effector_length * $effector_length - $bc_length * $bc_length) / (2 * $ab_length * $effector_length);
$cos_angle_a = clamp(-1, 1, $cos_angle_a);
float $angle_a = acos($cos_angle_a);

// Compute the angle of the "b" point
float $cos_angle_b = ($ab_length * $ab_length + $bc_length * $bc_length - $effector_length * $effector_length) / (2 * $ab_length * $bc_length);
$cos_angle_b = clamp(-1, 1, $cos_angle_b);
float $angle_b = acos($cos_angle_b);

{1}.angle_a = rad_to_deg($angle_a);
{1}.angle_b = rad_to_deg($angle_b - $pi);
"""


@dataclass
class TwoBoneIK2D(OMGroupNode):
    _expression_template: str = field(init=False)
    _expression_node: str = field(init=False)

    def build(self) -> None:
        super().build()

        # The creation of the expression nodes needs the maya attributes to exist
        # so we create them before the orodruin ports are created.
        self._create_maya_attributes()

        self._expression_template = EXPRESSION_TEMPLATE.format(
            self._input_node, self._output_node
        )
        self._expression_node = cmds.expression(
            string=self._expression_template,
            name=self.__class__.__name__ + "_EXP",
        )

    def _create_maya_attributes(self) -> None:
        cmds.addAttr(self._output_node, longName="angle_a", attributeType="double")
        cmds.addAttr(self._output_node, longName="angle_b", attributeType="double")

        cmds.addAttr(self._input_node, longName="point_a", attributeType="double3")
        cmds.addAttr(
            self._input_node,
            longName="point_aX",
            attributeType="double",
            parent="point_a",
        )
        cmds.addAttr(
            self._input_node,
            longName="point_aY",
            attributeType="double",
            parent="point_a",
        )
        cmds.addAttr(
            self._input_node,
            longName="point_aZ",
            attributeType="double",
            parent="point_a",
        )

        cmds.addAttr(self._input_node, longName="point_b", attributeType="double3")
        cmds.addAttr(
            self._input_node,
            longName="point_bX",
            attributeType="double",
            parent="point_b",
        )
        cmds.addAttr(
            self._input_node,
            longName="point_bY",
            attributeType="double",
            parent="point_b",
        )
        cmds.addAttr(
            self._input_node,
            longName="point_bZ",
            attributeType="double",
            parent="point_b",
        )

        cmds.addAttr(self._input_node, longName="point_c", attributeType="double3")
        cmds.addAttr(
            self._input_node,
            longName="point_cX",
            attributeType="double",
            parent="point_c",
        )
        cmds.addAttr(
            self._input_node,
            longName="point_cY",
            attributeType="double",
            parent="point_c",
        )
        cmds.addAttr(
            self._input_node,
            longName="point_cZ",
            attributeType="double",
            parent="point_c",
        )

        cmds.addAttr(self._input_node, longName="handle", attributeType="double3")
        cmds.addAttr(
            self._input_node,
            longName="handleX",
            attributeType="double",
            parent="handle",
        )
        cmds.addAttr(
            self._input_node,
            longName="handleY",
            attributeType="double",
            parent="handle",
        )
        cmds.addAttr(
            self._input_node,
            longName="handleZ",
            attributeType="double",
            parent="handle",
        )
