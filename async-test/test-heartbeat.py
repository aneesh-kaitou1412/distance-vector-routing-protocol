import asyncio
import random
import time
random.seed(1)

class node:
	def __init__(self, messages):
		self.messages = messages
		self.done = False

	def __str__(self):
		return str(self.messages)

	async def send(self, m):
		await asyncio.sleep(m)

	async def send_all(self):
		await asyncio.gather(self.send(self.messages[0]), self.send(self.messages[1]), self.send(self.messages[2]))
		self.done = True


async def main():
	nodes = [node([random.randint(1, 10) for _ in range(3)]) for _ in range(3)]
	for n in nodes:
		print(n)
	started_at = time.monotonic()
	await asyncio.gather(nodes[0].send_all(), nodes[1].send_all(), nodes[2].send_all())
	total_message_time = time.monotonic() - started_at

	print(f'Time taken for all messages : {total_message_time}')
	print([n.done for n in nodes])

asyncio.run(main())