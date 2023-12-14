import numpy as np
import matplotlib.pyplot as plt
import json

def particle_movement(t, y, coords, connections, F, restraints):
    # Reshape the vector y into a matrix with 2 columns
    y_matrix = y.reshape(-1, 2)

    # Initialize accelerations
    accelerations = np.zeros_like(y_matrix)

    for i, (coord, connection, force, restraint) in enumerate(zip(coords, connections, F, restraints)):
        # Extract coordinates
        xi, yi = y_matrix[i]

        # Calculate accelerations using DEM equations
        for neighbor in connection[1:]:
            xj, yj = y_matrix[neighbor - 1]  # Fix index by subtracting 1
            rij = np.sqrt((xi - xj)**2 + (yi - yj)**2)
            delta_x = xj - xi
            delta_y = yj - yi

            # DEM equations
            Fi = force[0] * delta_x / rij
            Fj = force[1] * delta_y / rij

            # Apply restraints
            Fi -= restraint[0] * xi
            Fj -= restraint[1] * yi

            # Update accelerations
            accelerations[i, 0] += Fi
            accelerations[i, 1] += Fj

    # Reshape accelerations into a vector
    return accelerations.flatten()

def solve_dem(coords, connections, F, restraints, t_span, h):
    num_particles = len(coords)
    initial_conditions = np.zeros_like(coords).flatten()

    # Time array
    t_values = np.arange(t_span[0], t_span[1] + h, h)

    # Initialize solution array
    solution = np.zeros((len(t_values), 2 * num_particles))
    solution[0] = initial_conditions

    # Solve the ODE using explicit Euler method
    for i in range(1, len(t_values)):
        t_i = t_values[i - 1]
        y_i = solution[i - 1]

        # Update using Euler's method
        y_i_plus_1 = y_i + h * particle_movement(t_i, y_i, coords, connections, F, restraints)

        # Save the updated solution
        solution[i] = y_i_plus_1

    return t_values, solution

with open("input.json", "r") as file:
        input_data = json.load(file)

# Extract input parameters
coords = np.array(input_data["coords"])
connections = np.array(input_data["connections"])
F = np.array(input_data["F"])
restraints = np.array(input_data["restraints"])
# Set the time span and time step for the simulation
t_span = (0, 10)
h = 1

# Solve the DEM
t_values, solution = solve_dem(coords, connections, F, restraints, t_span, h)

# Plot the particle trajectories
for i in range(len(coords)):
    plt.plot(solution[:, i * 2], solution[:, i * 2 + 1], label=f'Particle {i + 1}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Particle Movement using DEM')
plt.legend()
plt.show()
