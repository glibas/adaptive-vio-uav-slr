"""Colour palettes for the SLR figures.

Categorical cycles, sequential ramps, and divergent pairs chosen to stay
readable in greyscale print and under common forms of colour-vision
deficiency.

Usage
-----
    import palette as pal

    # set a default categorical cycle for all plots
    pal.use("divergent4")          # or any key in CYCLES

    # grab a sequential colormap for heatmaps
    cmap = pal.SEQUENTIAL["blue"]  # a matplotlib LinearSegmentedColormap

    # grab a discrete list for manual coloring
    colors = pal.CYCLES["emphasis_blue_red"]
"""

from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib as mpl


# ---------------------------------------------------------------
# Categorical cycles (discrete, ordered for max separation)
# Each is grayscale- and colorblind-aware.
# ---------------------------------------------------------------
CYCLES = {
    # two-colour emphasis pairs
    "emphasis_blue_red":    ["#1a80bb", "#a00000"],
    "emphasis_blue_orange": ["#1a80bb", "#ea801c"],
    "emphasis_blue_yellow": ["#1a80bb", "#f2c45f"],
    "emphasis_teal_gold":   ["#298c8c", "#f1a226"],
    "emphasis_teal_magenta":["#298c8c", "#800074"],

    # three-colour divergent sets with neutral grey
    "divergent3_a": ["#1a80bb", "#ea801c", "#b8b8b8"],
    "divergent3_b": ["#298c8c", "#a00000", "#b8b8b8"],
    "divergent3_c": ["#5e4c5f", "#999999", "#ffbb6f"],

    # four-colour divergent sets
    "divergent4":   ["#0000a2", "#bc272d", "#e9c716", "#50ad9f"],
    "divergent4_b": ["#4a2377", "#8cc5e3", "#f55f74", "#0d7d87"],
    "divergent4_c": ["#d31f11", "#f47a00", "#62c8d3", "#007191"],

    # greyscale fallbacks
    "grayscale":   ["#707070", "#b8b8b8"],
    "gray_blue":   ["#384860", "#97a6c4"],
}


# ---------------------------------------------------------------
# Sequential ramps -> continuous LinearSegmentedColormap
# (light -> dark; reverse with cmap.reversed() if needed)
# ---------------------------------------------------------------
_SEQ_STOPS = {
    "blue":   ["#8cc5e3", "#3594cc", "#2066a8"],
    "red":    ["#d8a6a6", "#c46666", "#a00000"],
    "teal":   ["#9fc8c8", "#54a1a1", "#1f6f6f"],
    "orange": ["#f0b077", "#ea801c", "#c2660f"],
    "brown":  ["#eddca5", "#c99b38", "#8a6420"],
    "ylgnbu": ["#ffffcc", "#c7e9b4", "#7fcdbb",
               "#41b6c4", "#2c7fb8", "#253494"],  # for heatmaps
}

SEQUENTIAL = {
    name: LinearSegmentedColormap.from_list(f"seq_{name}", stops, N=256)
    for name, stops in _SEQ_STOPS.items()
}

# discrete 3-step versions of the same ramps (for stacked bars, etc.)
SEQUENTIAL_DISCRETE = {
    name: ListedColormap(stops, name=f"seq_{name}_d")
    for name, stops in _SEQ_STOPS.items()
}


# ---------------------------------------------------------------
# Light/dark divergent pairs -> four-colour cycles
# ---------------------------------------------------------------
CYCLES.update({
    "pair_blue_orange": ["#3594cc", "#8cc5e3", "#ea801c", "#f0b077"],
    "pair_brown_teal":  ["#c99b38", "#eddca5", "#00b0be", "#8fd7d7"],
    "pair_teal_red":    ["#0d7d87", "#99c6cc", "#c31e23", "#ff5a5e"],
})


# ---------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------
def use(cycle_name):
    """Set a categorical palette as the global matplotlib color cycle."""
    if cycle_name not in CYCLES:
        raise KeyError(f"{cycle_name!r} not in CYCLES: {list(CYCLES)}")
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=CYCLES[cycle_name])
    return CYCLES[cycle_name]


def listed(cycle_name):
    """Return a ListedColormap from a categorical cycle."""
    return ListedColormap(CYCLES[cycle_name], name=cycle_name)


if __name__ == "__main__":
    # quick self-check
    print("categorical cycles:", len(CYCLES))
    print("sequential cmaps:  ", list(SEQUENTIAL))
    use("divergent4")
    print("active cycle set to divergent4:",
          [c["color"] for c in mpl.rcParams["axes.prop_cycle"]])
