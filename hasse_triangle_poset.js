
function getTriangleHasseGraph(n_val) {
    var hasse_graph = { nodes: [], edges: [] };
    // add nodes
    var ns = [];
    for (i = 1; i <= n_val; i++) {
        /////////////////////////
        // FILL IN CODE HERE
        ///////////////////////
    }
    console.log("nodes: " + ns);
    // add edges
    var adj_list = {};
        /////////////////////////
        // FILL IN CODE HERE
        ///////////////////////
    console.log(adj_list);
    return hasse_graph;
}

function getDivHasseGraph(n_val) {
    var hasse_graph = { nodes: [], edges: [] };
    // add nodes
    var ns = [];
    for (i = 1; i <= n_val; i++) {
        const node = {
            id: i,
            label: String(i)
        };
        hasse_graph.nodes.push(node);
        ns.push(i);
    }
    console.log("nodes: " + ns);

    // add edges
    var adj_list = {};
    // iterate through "upper" node
    for (j = 1; j <= n_val; j++) {
        const n = j;
        adj_list[n] = [];
        var grandchildren = [];
        // iterate through "lower" node
        for (i = 1; i < j; i++) {
            const d = n - i;
            var addEdge = false;
            if (n % d == 0) {
                addEdge = true;
                // add children of d to grandchildren
                grandchildren = grandchildren.concat(adj_list[d])
                if (grandchildren.length > 0) {
                    console.log("current gchildren of " + n + ": " + grandchildren)
                }
            }
            if (grandchildren.includes(d)) {
                addEdge = false;
            }
            if (addEdge) {
                adj_list[n].push(d);
                const edge = { 
                    from: n, 
                    to: d,
                    id: String(d) + " \u22D6 " + String(n),
                };
                hasse_graph.edges.push(edge)
            }
        }
    }
    console.log(adj_list);
    return hasse_graph;
}

/**
 * @param path
 * @param success
 * @param error
 */
function loadJSON(path, success, error) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          success(JSON.parse(xhr.responseText));
        } else {
          error(xhr);
        }
      }
    };
    xhr.open("GET", path, true);
    xhr.send();
  }