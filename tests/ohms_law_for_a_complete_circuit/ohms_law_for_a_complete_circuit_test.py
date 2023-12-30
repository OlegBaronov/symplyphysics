from collections import namedtuple
from pytest import approx, fixture, raises
from symplyphysics import (
    errors,
    units,
    convert_to,
    Quantity,
    SI,
)
from symplyphysics.laws.electricity import ohms_law_for_a_complete_circuit as ohms_law

# Description
## Let's assume that the circuit resistance is 11 ohms, and the source connected to it has an emf of 12 V and an internal resistance of 1 ohm.


@fixture(name="test_args")
def test_args_fixture():
    E = Quantity(12 * units.volt)
    r = Quantity(1 * units.ohm)
    R = Quantity(11 * units.ohm)
    Args = namedtuple("Args", ["E", "r", "R"])
    return Args(E=E, r=r, R=R)


def test_basic_current(test_args):
    result = ohms_law.calculate_current(test_args.E, test_args.r, test_args.R)
    assert SI.get_dimension_system().equivalent_dims(result.dimension, units.current)
    result_current = convert_to(result, units.ampere).evalf(2)
    assert result_current == approx(1.0, 0.01)

#
# def test_bad_voltage(test_args):
#     Vb = Quantity(1 * units.meter)
#     with raises(errors.UnitsError):
#         ohms_law.calculate_current(Vb, test_args.R)
#     with raises(TypeError):
#         ohms_law.calculate_current(100, test_args.R)
#
#
# def test_bad_resistance(test_args):
#     Rb = Quantity(1 * units.meter)
#     with raises(errors.UnitsError):
#         ohms_law.calculate_current(test_args.V, Rb)
#     with raises(TypeError):
#         ohms_law.calculate_current(test_args.V, 100)