#!/usr/bin/python
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import numpy as np

def color_scatter(N=1000):
    # Example taken from: https://bokeh.pydata.org/en/latest/docs/gallery/color_scatter.html
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    radii = np.random.random(size=N) * 3
    colors = [
        "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
    ]

    p = figure()
    p.scatter(x, y, radius=radii,
              fill_color=colors, fill_alpha=0.6,
              line_color=None)

    html = file_html(p, CDN, "My colorful scatter plot")
    return html

# For local testing
if __name__ == '__main__':
    with open("color_scatter.html", "w") as f:
        f.write(color_scatter(5))
