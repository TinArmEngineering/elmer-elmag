
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
#                 6) Add circuit components to circuit c[n].components.append([R1, V1, ElmerFemCoil, ...etc])
#                 7) Write circuits generate_elmer_circuits(c, output_file)
#                 8) Output file must be included in .sif file
#
# ------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# Imported Libraries:
import sys
from elmer_circuitbuilder import *

# -----------------------------------------------------------------------------------------------------

def main(argv=None):

    # name output file
    output_file = "harmonic_current_divider.definition"

    # initialize circuits: number of circuits - do not remove
    c = number_of_circuits(1)

    # ------------------ Circuit 1 (Current Divider (Parallel Connection) - Harmonic)---------------------

    # reference/ground node needed - do not remove.
    c[1].ref_node = 1

    # Components
    phase_degrees = 0.0     # enter phase in degrees
    Is = 1                  # voltage source amplitude
    Rs = 5.496942336059e-3  # resistor value

    phase = np.radians(phase_degrees)
    I1 = I("I1", 2, 1, Is*np.exp(phase*1j))
    R1 = R("R1", 2, 1, Rs)
    FEM_Wire_1 = ElmerComponent("FEM_Wire_1", 2, 1, 1, [1])

    # store components in array components = [comp1, comp2,...] - do not remove
    c[1].components.append([I1, R1, FEM_Wire_1])

    # --------------------------------------------------

    # generate elmer circuit.definitions - do not remove / do not edit
    generate_elmer_circuits(c, output_file)

    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)

