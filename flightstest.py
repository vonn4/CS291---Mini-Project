import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = r"C:\Users\ethan\Downloads\archive (4)\sampleflights3.csv"
df = pd.read_csv(file_path)

# Check if 'Origin', 'Destination', and 'Distance' columns exist
required_columns = {'Origin', 'Destination', 'Distance'}
if not required_columns.issubset(df.columns):
    raise ValueError("The dataset must have 'Origin', 'Destination', and 'Distance' columns for flight connections.")

# Initialize a directed graph
G = nx.DiGraph()

# Add edges from 'Origin' to 'Destination' with 'Distance' as the weight
for _, row in df.iterrows():
    G.add_edge(row['Origin'], row['Destination'], weight=row['Distance'])

# Plot the graph
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42, k=120)  # Increase 'k' for more spacing

# Draw nodes, edges, and labels
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue", edgecolors="black")
nx.draw_networkx_edges(G, pos, arrowsize=5, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Draw edge labels for distances
edge_labels = nx.get_edge_attributes(G, 'weight')  # Retrieve the 'weight' attribute for edges
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.5)

# Display the graph
plt.title("Flight Connections Graph with Distances")
plt.axis("off")
plt.show()
