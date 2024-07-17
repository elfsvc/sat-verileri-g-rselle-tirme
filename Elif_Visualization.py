import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#DATA'nın Okunması
df = pd.read_excel('/content/sample_data/detailed_data_v2.xlsx')
G = nx.Graph()

#Düğüm ve köşeler eklenmesi
for index, row in df.iterrows():
    product = row['Product']
    category = row['Category']
    origin = row['Origin']

    G.add_node(product, category=category, origin=origin)
    G.add_edge(product, category)
    G.add_edge(product, origin)

plt.figure(figsize=(15, 10))
# k kadar spring et
pos = nx.spring_layout(G, seed=42, k=1, iterations=100)


category_nodes = [node for node, data in G.nodes(data=True) if data.get('category') and not data.get('origin')]
origin_nodes = [node for node, data in G.nodes(data=True) if data.get('origin') and node not in category_nodes]
product_nodes = [node for node in G.nodes() if node not in category_nodes and node not in origin_nodes]

# Düğümlerin çizilmesi
nx.draw_networkx_nodes(G, pos, nodelist=category_nodes, node_color='lighgreen', node_size=500, alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=origin_nodes, node_color='skyblue', node_size=200, alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=product_nodes, node_color='purple', node_size=500, alpha=0.8)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.0, alpha=0.5, edge_color='grey')

labels = {node: node for node in product_nodes + origin_nodes}
nx.draw_networkx_labels(G, pos, labels, font_color = 'black', font_size=5)

plt.title('Ebebek Satış Verileri Ağırlıklandırma İle Ağ Görüntülemesi')
plt.axis('off')
plt.show()