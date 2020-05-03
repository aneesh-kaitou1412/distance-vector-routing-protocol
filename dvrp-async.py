"""	Imports """
from collections import defaultdict
import asyncio
import time

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
		print(f"Node:{str(self.name)}")
		print(f"To Transmit Again:{self.updated}")

		print("Routing Table : ")
		print("Node\t\tDist\t\tNxtHop")
		
		for k, v in self.routing_table.items():
			if k in self.neighbours:
				print(f"{k} [N]\t\t{v['distance']}\t\t{v['next_hop']}")
			else:
				print(f"{k}\t\t{v['distance']}\t\t{v['next_hop']}")
		
		print("")
	
	def receive_routing_table(self, node, routing_table):
		while True:
			flag = True
			for k in routing_table:
				if routing_table[k]['distance'] + self.routing_table[node]['distance'] < self.routing_table[k]['distance']:
					flag = False
					self.routing_table[k]['distance'] = routing_table[k]['distance'] + self.routing_table[node]['distance']
					self.routing_table[k]['next_hop'] = self.routing_table[node]['next_hop']
					self.updated = True
			if flag:
				break

	async def send_individual_routing_table(self, receiving_node):
		# await asyncio.sleep(1)
		await asyncio.sleep(self.routing_table[receiving_node]['distance'])
		receiving_node.receive_routing_table(self, self.routing_table)

	async def send_routing_table(self):
		if self.updated:
			self.updated = False
			for node in self.neighbours:
				task = asyncio.create_task(self.send_individual_routing_table(node))
				await task

""" Test """
nodelist = [0, 1, 2, 3, 4]
edgelist = [(0, 1, 3), (0, 2, 12), (1, 2, 2), (2, 3, 5), (3, 4, 4)]

nodes = [Node(i) for i in nodelist]

for u, v, w in edgelist:
	nodes[u].set_neighbours([nodes[v]])
	nodes[u].set_neighbour_distance(nodes[v], w)
	nodes[v].set_neighbours([nodes[u]])
	nodes[v].set_neighbour_distance(nodes[u], w)

async def simulation():
	iterations = 0
	while any(nodes[i].updated for i in nodelist):
		iterations += 1
		print(f"Iteration {iterations}")

		started_at = time.monotonic()
		for i in nodelist:
			task = asyncio.create_task(nodes[i].send_routing_table())
			await task
		total_message_time = time.monotonic() - started_at

		print(f"Time taken for all messages : {total_message_time}")
			
asyncio.run(simulation())

print("="*50)
for i in nodelist:
	nodes[i].print_details()