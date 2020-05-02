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
			* neighbours : dict of neighbours of this node (node, cost)
	"""
	def __init__(self, name, neighbours):
		self.name = name
		self.neighbours = neighbours.copy()
		self.routing_table = defaultdict(lambda : {'distance': float('inf'), 'next_hop': None})
		for node in self.neighbours:
			self.routing_table[node]['distance'] = neighbours[node]
			self.routing_table[node]['next_hop'] = node

	def __str__(self, *args, **kwargs):
		string_rep = """Name : {name} \n"""
		string_rep = string_rep.format(name=self.name)

		string_rep += """Neighbours : {neighbours} \n""".format(neighbours=self.neighbours)
		
		string_rep += """Routing Table : \nNode\tDist\tNxtHop \n"""
		for k, v in self.routing_table.items():
			string_rep += """{k}\t{dist}\t{next_hop} \n""".format(k=k, dist=v['distance'], next_hop=v['next_hop'])
		
		return string_rep

	def send_routing_table(self):
		pass



""" Test """
neighlist = ['2', '5', '6']
costlist = [12, 5, 8]
neighbours = dict(zip(neighlist, costlist))
n = Node('1', neighbours)
print(n)