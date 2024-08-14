import numpy as np
import matplotlib.pyplot as plt


def lagrange_basis_polynomials(x, x_points, j):
    basis_poly = 1
    for m in range(len(x_points)):
        if m != j:
            basis_poly *= (x - x_points[m]) / (x_points[j] - x_points[m])
    return basis_poly


def lagrange_interpolating_polynomial(x, x_points, y_points):
    polynomial = 0
    for j in range(len(x_points)):
        polynomial += y_points[j] * lagrange_basis_polynomials(x, x_points, j)
    return polynomial


def plot_lagrange(ax, x, x_points, y_points=None, plot_type="basis"):
    if plot_type == "basis":
        for j in range(len(x_points)):
            y_basis = lagrange_basis_polynomials(x, x_points, j)
            ax.plot(x, y_basis, label=f"Basis polynomial $l_{j}(x)$")
        ax.scatter(x_points, np.zeros_like(x_points), color="black", zorder=5)
        ax.set_ylabel("$l_j(x)$")
        ax.set_title("Lagrange Basis Polynomials")
    elif plot_type == "interpolating":
        y_dense = lagrange_interpolating_polynomial(x, x_points, y_points)
        ax.plot(x, y_dense, label="Interpolating polynomial $P(x)$")
        ax.scatter(x_points, y_points, color="red", zorder=5)
        ax.set_ylabel("$P(x)$")
        ax.set_title("Lagrange Interpolating Polynomial")

    ax.axhline(y=1, color="grey", linestyle="--")
    ax.set_xlabel("$x$")
    ax.legend()
    ax.grid(True)


# Sample points
x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 8, 27, 64])

# Create a dense range of x values for plotting
x_dense = np.linspace(min(x_points) - 1, max(x_points) + 1, 400)

# Create a figure with side-by-side subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot Lagrange basis polynomials
plot_lagrange(ax1, x_dense, x_points, plot_type="basis")

# Plot the full interpolating polynomial
plot_lagrange(ax2, x_dense, x_points, y_points=y_points, plot_type="interpolating")

# Adjust layout
plt.tight_layout()
plt.show()
