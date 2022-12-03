#implementing graph coloring using back tracking
#minimum number of colors required for graph coloring

from collections import deque
def minimumColors(nodes, edges, ls_nodes, ls_edges):
	adj = [[] for i in range(nodes)]
	count = [0]*nodes
	colors = [1]*(nodes)
	for i in range(nodes):
		adj[ls_edges[i] - 1].append(ls_nodes[i] - 1)
		count[ls_nodes[i] - 1] += 1

	# Declare queue Q
	Q = deque()
	for i in range(nodes):
		if (count[i] == 0):
			Q.append(i)
	while len(Q) > 0:
		u = Q.popleft()
		for x in adj[u]:
			count[x] -= 1
			if (count[x] == 0):
				Q.append(x)
			if (colors[x] <= colors[u]):
				colors[x] = 1 + colors[u]

	# Stores the minimumColors
	minColor = -1

	# Find the maximum of colors[]
	for i in range(nodes):
		minColor = max(minColor, colors[i])

	# Print the minimum number of colors required.
	print("minimum number of colors required:",minColor)

# Drier code
nodes = 4
edges = 5
ls_nodes = [1, 2, 3, 4, 4]
ls_edges = [3, 2, 4, 4, 5, 5]

minimumColors(nodes, edges, ls_nodes, ls_edges)
