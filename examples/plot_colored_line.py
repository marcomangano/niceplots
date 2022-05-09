"""
Colored line plotting
=====================
An example of the plotColoredLine function, plotting the sine and cosine functions,
colored by their derivatives
"""

# ==============================================================================
# Standard Python modules
# ==============================================================================

# ==============================================================================
# External Python modules
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import niceplots

# ==============================================================================
# Extension modules
# ==============================================================================

niceplots.setRCParams()

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
c = np.cos(x)

fig, ax = plt.subplots()
niceplots.plotColoredLine(x, y, c, cmap="coolwarm", fig=fig, ax=ax, addColorBar=True, cRange=None, cBarLabel="$dy/dx$")
niceplots.plotColoredLine(x, c, -y, cmap="coolwarm", fig=fig, ax=ax)
niceplots.adjust_spines(ax)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$", rotation="horizontal", ha="right")
ax.set_xticks(np.linspace(0, 2, 5) * np.pi)
ax.set_xticklabels([0, r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
ax.set_xlim(0, 2 * np.pi)
fig.savefig("coloredLine.png", dpi=400)
fig.savefig("coloredLine.pdf")

# Use a custom norm to specify the colormap range
divnorm = TwoSlopeNorm(vmin=-1.0, vcenter=0.8, vmax=1.0)
fig, ax = niceplots.plotColoredLine(x, y, c, cmap="coolwarm", norm=divnorm, addColorBar=False, cBarLabel="$dy/dx$")
niceplots.adjust_spines(ax)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$", rotation="horizontal", ha="right")
ax.set_xticks(np.linspace(0, 2, 5) * np.pi)
ax.set_xticklabels([0, r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
ax.set_xlim(0, 2 * np.pi)
fig.savefig("coloredLineCustomNorm.png", dpi=400)
fig.savefig("coloredLineCustomNorm.pdf")
# plt.show()
