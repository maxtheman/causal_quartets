import marimo

__generated_with = "0.9.17"
app = marimo.App(width="medium")


@app.cell
def __():
    from y0.graph import NxMixedGraph
    return (NxMixedGraph,)


@app.cell
def __(NxMixedGraph, parse_dag_string):
    def test_dag_parser():

        # Test case 1: Single path with bidirectional arrows
        g1 = parse_dag_string("u->x->y<-u", NxMixedGraph())
        
        # Test case 2: List of paths
        g2 = parse_dag_string(["u->x->y", "u->y"], NxMixedGraph())
        
        # Test case 3: Multiline string
        g3 = parse_dag_string("""u->x->y
                                u->y""", NxMixedGraph())
        
        # Helper function to compare graphs
        def graphs_equal(g1, g2):
            return set(g1.directed.edges()) == set(g2.directed.edges()) and set(g1.directed.nodes()) == set(g2.directed.nodes())
        
        # Print results
        print("Graph 1 edges:", g1.directed.edges())
        print("Graph 2 edges:", g2.directed.edges())
        print("Graph 3 edges:", g3.directed.edges())
        
        print("\nAre all graphs equivalent?")
        print("g1 == g2:", graphs_equal(g1, g2))
        print("g2 == g3:", graphs_equal(g2, g3))
        print("g1 == g3:", graphs_equal(g1, g3))
    return (test_dag_parser,)


@app.cell
def parse_dag_string():
    def parse_dag_string(input_str, graph):
        """
        Parse a string or list of strings into a DAG.
        Accepts formats:
        - Single path: "u->x->y<-u"
        - List of paths: ["u->x->y", "u->y"]
        - Multiline string: '''u->x->y
                               u->y'''
        """    
        # Convert input to list of strings to process
        if isinstance(input_str, list):
            paths = input_str
        else:
            # Split multiline string into separate lines
            paths = input_str.strip().split('\n')
        
        for path in paths:
            # Handle bidirectional arrows first
            segments = path.split('<-')
            if len(segments) > 1:
                # Process right-to-left edges
                for i in range(len(segments)-1):
                    right = segments[i].strip().split('->')[-1]  # Get the rightmost node
                    left = segments[i+1].strip().split('->')[0]  # Get the leftmost node
                    graph.add_directed_edge(left, right)
            
            # Process left-to-right edges in each segment
            for segment in segments:
                nodes = segment.strip().split('->')
                for i in range(len(nodes)-1):
                    if nodes[i] and nodes[i+1]:  # Ensure both nodes exist
                        graph.add_directed_edge(nodes[i].strip(), nodes[i+1].strip())
        
        return graph
    return (parse_dag_string,)


@app.cell
def __(test_dag_parser):
    test_dag_parser()
    return


if __name__ == "__main__":
    app.run()
