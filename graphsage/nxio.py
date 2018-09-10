import networkx as nx
def createG():
    G = nx.Graph()
    G.add_nodes_from([2, 3])
    G.add_edge(2,3)
    return G

G = createG()
import json
import networkx as nx
from networkx.readwrite import json_graph
jgraph = json_graph.node_link_data(G)
js = json.dumps(jgraph)

def writejs(js):
    import os
    os.path.append('/home/cai.507/Documents/DeepLearning/GraphSAGE')
    file = '/home/cai.507/Documents/DeepLearning/GraphSAGE/' + 'test_data'
    f = open(file, 'w')
    f.write(js)
    f.close()

f = open(file, 'r')
json_repr = f.read()
assert js == json_repr
f.close()

from networkx.readwrite import json_graph

X = json_graph.node_link_graph(json_repr)
nx.node_

from networkx.readwrite import json_graph
G = createG()
data = json_graph.node_link_data(G)
import pickle
with open('dict', 'wb') as handle:
    pickle.dump(data, handle, protocol=2)
with open('dict', 'rb') as handle:
    data_ = pickle.load(handle)
assert data == data_

H = json_graph.node_link_graph(data_)
