""" 
	Node Class for DVRP 
"""

class Node:
	"""
		class Node
		Arguments:
			* name : name of the node
			* neighbours : list of neighbours of this node
	"""
	def __init__(self, name, neighbours):
		self.name = name
		self.neighbours = neighbours.copy()

	def __str__(self):
		string_rep = """ Name : {name} \n Neighbours : {neighbours} """
		return string_rep.format(name=self.name, neighbours=self.neighbours)