import marimo

__generated_with = "0.9.17"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from parser import parse_dag_string as parse_dag_string_cell
    from y0.graph import NxMixedGraph
    from matplotlib import pyplot as plt
    return NxMixedGraph, mo, parse_dag_string_cell, plt


@app.cell
def __(parse_dag_string_cell):
    _, p_defs = parse_dag_string_cell.run()
    return (p_defs,)


@app.cell
def __(p_defs):
    parse_dag_string = p_defs['parse_dag_string']
    return (parse_dag_string,)


@app.cell
def __(mo):
    input_graph = mo.ui.text_area(placeholder="x->y")
    return (input_graph,)


@app.cell
def __(NxMixedGraph, input_graph, mo, parse_dag_string, plt):
    graph = parse_dag_string(input_graph.value, NxMixedGraph())
    fig, ax = plt.subplots()
    graph.draw(ax=ax)
    instructions = mo.md('''## Instructions:

    - Use variables and arrow notation to create graphs (e.g., `x->y<-z`)
    - Click anywhere to see the graph rendered''')
    interactive = mo.mpl.interactive(fig)
    mo.vstack([
        mo.md('# Causal Graphs'),
        input_graph,
        mo.hstack([interactive, instructions],widths=[2,1])
    ])
    return ax, fig, graph, instructions, interactive


if __name__ == "__main__":
    app.run()
