from sympy import (Eq, solve)
from symplyphysics import (units, Quantity, Symbol, print_expression, validate_input,
    validate_output)

# Description
## the current strength is directly proportional to the sum of the EMF of the circuit, and inversely proportional to the sum of the resistances of the source and circuit
## Ohm's law: I = E / r + R
## Where I is the current strength
## E is the Electromotive force
## r is internal resistance source
## R is circuit resistance

current = Symbol("current", units.current)
electromotive_force = Symbol("Electromotive_force", units.voltage)
resistance_source = Symbol("resistance_source", units.impedance)
circuit_resistance = Symbol("circuit_resistance", units.impedance)
law = Eq(current, electromotive_force / (resistance_source + circuit_resistance))


def print_law() -> str:
    return print_expression(law)


@validate_input(electromotive_force_=electromotive_force, resistance_source_=resistance_source, circuit_resistance_=circuit_resistance)
@validate_output(current)
def calculate_current(electromotive_force_: Quantity, resistance_source_: Quantity, circuit_resistance_: Quantity) -> Quantity:
    result_current_expr = solve(law, current, dict=True)[0][current]
    result_expr = result_current_expr.subs({electromotive_force: electromotive_force_, resistance_source: resistance_source_, circuit_resistance: circuit_resistance_})
    return Quantity(result_expr)