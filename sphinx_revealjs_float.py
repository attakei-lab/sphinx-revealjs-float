"""Custom directives for Reveal.js."""
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx


class revealjs_float(nodes.General, nodes.Element):  # noqa: D101
    pass


class RevealjsFloat(Directive):  # noqa: D101
    has_content = True
    option_spec = {
        "drag": directives.unchanged,
        "drop": directives.unchanged,
        "bg": directives.unchanged,
    }

    def run(self):  # noqa: D102
        node = revealjs_float()
        node.attributes = self.options
        node.content = "\n".join(self.content or [])
        self.state.nested_parse(self.content, self.content_offset, node)
        return [
            node,
        ]


def visit_revealjs_float(self, node: revealjs_float):  # noqa: D103
    import string

    styles = {
        "position": "fixed",
    }
    if "bg" in node.attributes:
        styles["background-color"] = node.attributes["bg"]
    if "drag" in node.attributes:
        x, y = node.attributes["drag"].split()
        styles["width"] = x if x[-1] not in string.digits else f"{x}%"
        styles["height"] = y if y[-1] not in string.digits else f"{y}%"
    if "drop" in node.attributes:
        x, y = node.attributes["drop"].split()
        if x[0] == "-":
            styles["right"] = x[1:] if x[-1] not in string.digits else f"{x[1:]}%"
        else:
            styles["left"] = x if x[-1] not in string.digits else f"{x}%"
        if y[0] == "-":
            styles["bottom"] = y[1:] if y[-1] not in string.digits else f"{y[1:]}%"
        else:
            styles["top"] = y if y[-1] not in string.digits else f"{y}%"
    style = "; ".join([f"{k}: {v}" for k, v in styles.items()])
    style = f'style="{style}"'
    self.body.append(f"<div {style}>")


def depart_revealjs_float(self, node: revealjs_float):  # noqa: D103
    self.body.append("</div>\n")


def not_write(self, node):
    """visit/depart function for declare "no write"."""
    pass


def setup(app: Sphinx):
    app.add_node(
        revealjs_float,
        html=(not_write, not_write),
        revealjs=(visit_revealjs_float, depart_revealjs_float),
    )
    app.add_directive("revealjs-float", RevealjsFloat)
