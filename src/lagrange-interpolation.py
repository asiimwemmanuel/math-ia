import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Font size variables for modularity
factor = 1.2
font_size_title = 20 * factor
font_size_legend = 16 * factor
annotation_font_size = 20 * factor
font_size_label = 16 * factor

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
    colormap = cm.get_cmap('viridis', len(x_points))
    if plot_type == "basis":
        for j in range(len(x_points)):
            y_basis = lagrange_basis_polynomials(x, x_points, j)
            ax.plot(x, y_basis, label=f"$l_{j}(x)$", color=colormap(j))
            # Highlight and label intersections with y = 1
            for xi in x_points:
                yi = lagrange_basis_polynomials(xi, x_points, j)
                if np.isclose(yi, 1, atol=1e-2):
                    ax.scatter(xi, 1, color=colormap(j), zorder=10)
                    # Calculate luminance of the text color
                    text_color = colormap(j)
                    luminance = 0.2126 * text_color[0] + 0.7152 * text_color[1] + 0.0722 * text_color[2]

                    # Choose background color based on luminance
                    if luminance > 0.5:  # If the text color is light
                        background_color = "black"  # Use dark background
                    else:
                        background_color = "white"  # Use light background

                    ax.annotate(
                        f"$l_{j}(x) = 1$",
                        (xi, 1),
                        textcoords="offset points",
                        xytext=(0, 10),
                        ha="center",
                        fontsize=annotation_font_size,
                        color=text_color,
                        backgroundcolor=background_color,  # Set contrasting background color
                    )
        ax.scatter(x_points, np.zeros_like(x_points), color="black", zorder=5)
        ax.set_ylabel("$l_j(x)$", fontsize=font_size_label)
        ax.set_title("Lagrange Basis Polynomials", fontsize=font_size_title)
        ax.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=font_size_legend)
    elif plot_type == "interpolating":
        y_dense = lagrange_interpolating_polynomial(x, x_points, y_points)
        ax.plot(x, y_dense, label="$P(x)$", color="red")
        ax.scatter(x_points, y_points, color="red", zorder=5)
        ax.set_ylabel("$P(x)$", fontsize=font_size_label)
        ax.set_title("Lagrange Interpolating Polynomial", fontsize=font_size_title)
        ax.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=font_size_legend)

    ax.axhline(y=1, color="grey", linestyle="--")
    ax.set_xlabel("$x$", fontsize=font_size_label)
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=font_size_legend)
    ax.grid(True)

# Sample points input from terminal
x_input = input("Enter x points separated by commas (e.g., 1,2,3,4): ")
y_input = input("Enter y points separated by commas (e.g., 1,4,9,16): ")

# Convert input strings to numpy arrays
x_points = np.array([float(x) for x in x_input.split(",")])
y_points = np.array([float(y) for y in y_input.split(",")])

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
