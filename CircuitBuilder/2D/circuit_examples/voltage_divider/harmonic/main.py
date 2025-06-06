
# -----------------------------------------------------------------------------------------------------
# Elmer circuit builder main:
#
# Description:
#                This is a tool to write circuits in Elmer format using pin-connection convention.
#
# Instructions:
#                 1) Import the circuit builder library (from circuit_builder import *)
#                 2) Set output file name as a string (e.g output_file = "string_circuit.definitions")
#                 3) Set number of circuits with number_of_circuits(n) (e.g c = number_of_circuits(1))
#                 4) Set your ground/reference node in the current circuit c[1].ref_node = pin_number
#                 5) Select and configure electrical component
#                     Resistors (R), Inductors (L), Capacitors (C), Voltage Source (V), Current Source (I)
#                     or FEM Component (ElmerComponent)
#                     Arguments needed for R, L, C, V, I is the same. ElmerComponent takes additional arguments
#
#                     Resistor Declaration:
#                             R1 = R(string_resistor_name, int_pin1, int_pin2, int_value (optional. default=None))
#                              int_value is an optional argument. If not set to a value it
#                              needs to be entered manually in the output file.
#
#                     ElmerComponent Declaration:
#                             ElmerCoil1 = ElmerComponent(
#                                                         string_elmercomp_name,
#                                                         int_pin1,
#                                                         int_pin2,
#                                                         int_series_resistor
#                                                         int_component_number
#                                                         int_list_master_bodies
#                                                         string_coil_type
#                                                         int_number_of_turns (optional. default=1)
#                                                         int_coil_length (optional. default=1)
#                                                         int_symmetry (optional. default=1))
#
#                 6) Add circuit components to circuit c[n].components.append([R1, V1, ElmerFemCoil, ...etc])
#                 7) Write circuits generate_elmer_circuits(c, output_file)
#                 8) Output file must be included in .sif file
#
# ------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# Imported Libraries:
from circuit_builder import *

# -----------------------------------------------------------------------------------------------------

def main(argv=None):

    # name output file
    output_file = "harmonic_voltage_divider.definition"

    # initialize circuits: number of circuits - do not remove
    c = number_of_circuits(1)

    # ------------------ Circuit 1 (Voltage Source, Resistor and FEM coil connected in series - Harmonic)---------

    # reference/ground node needed - do not remove.
    c[1].ref_node = 1

    # Components
    phase_degrees = 0.0     # enter phase in degrees
    Vs = 1                  # voltage source amplitude
    Rs = 5.496942336059e-3  # resistor value

    phase = np.radians(phase_degrees)
    V1 = V("V1", 1, 2, Vs*np.exp(phase*1j))
    R1 = R("R1", 2, 3, Rs)
    FEM_Component1 = ElmerComponent("Coil1", 3, 1, 0, 1, [1], "Massive")

    # store components in array components = [comp1, comp2,...] - do not remove
    c[1].components.append([V1, R1, FEM_Component1])

    # --------------------------------------------------

    # generate elmer circuit.definitions - do not remove / do not edit
    generate_elmer_circuits(c, output_file)

    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)

