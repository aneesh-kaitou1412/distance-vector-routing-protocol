"""	Imports """
from collections import defaultdict

""" 
	Node Class for DVRP
		Routing table to be modelled as a default dict
		To be able to send its routing table to all neighbour nodes
		To be able to receive routing table from another node
"""
class Node:
	"""
		class Node
		Arguments:
			* name : name of the node
	"""
	def __init__(self, name):
		self.name = name
		self.neighbours = set()
		self.routing_table = defaultdict(lambda : {'distance': float('inf'), 'next_hop': None})
		self.routing_table[self]['distance'] = 0
		self.routing_table[self]['next_hop'] = None
		self.updated = True

	def __str__(self):
		return str(self.name)

	def set_neighbours(self, neighbours):
		for node in neighbours:
			self.neighbours.add(node)
			self.routing_table[node]

	def set_neighbour_distance(self, node, dist):
		if node in self.neighbours:
			self.routing_table[node]['distance'] = dist
			self.routing_table[node]['next_hop'] = node

	def print_details(self):
		print("""Node:{name}""".format(name=str(self.name)))
		print("""To Transmit:{update}""".format(update=self.updated))
		print("""Routing Table : """)
		print("""Node\t\tDist\t\tNxtHop""")
		for k, v in self.routing_table.items():
			if k in self.neighbours:
				print("""{k} [N]""".format(k=k), end="\t\t")
			else:
				print("""{k}""".format(k=k), end="\t\t")
			print("""{dist}""".format(dist=v['distance']), end="\t\t")
			print("""{nxthop}""".format(nxthop=v['next_hop']))
		print("")
	
	def receive_routing_table(self, node, routing_table):
		for k in routing_table:
			if routing_table[k]['distance'] + self.routing_table[node]['distance'] < self.routing_table[k]['distance']:
				self.routing_table[k]['distance'] = routing_table[k]['distance'] + self.routing_table[node]['distance']
				self.routing_table[k]['next_hop'] = self.routing_table[node]['next_hop']
				self.updated = True

	def send_routing_table(self):
		if self.updated:
			for node in self.neighbours:
				node.receive_routing_table(self, self.routing_table)
			self.updated = False


""" Test """
nodelist = [0, 1, 2, 3]
edgelist = [(0, 1, 3), (0, 2, 23), (1, 2, 2), (2, 3, 5)]

nodes = [Node(i) for i in nodelist]
# print("""{n}""".format(n=nodes[0]))

for u, v, w in edgelist:
	nodes[u].set_neighbours([nodes[v]])
	nodes[u].set_neighbour_distance(nodes[v], w)
	nodes[v].set_neighbours([nodes[u]])
	nodes[v].set_neighbour_distance(nodes[u], w)

iterations = 0
while(all(nodes[i].updated for i in nodelist)):
	iterations += 1
	print("Iteration "+str(iterations))
	for i in nodelist:
		nodes[i].send_routing_table()

print("="*50)
for i in nodelist:
	nodes[i].print_details()
