# Distance Vector Routing Protocol

A Python implementation of Distance Vector Routing Protocol.
This is a distributed asynchronous protocol for nodes to find the minimum
cost paths to other nodes in the network.

### Basic Algorithm

The algorithm is a distributed approach of the [**Bellman Ford Algorithm**](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) for shortest paths.

## Ideas to Implement

Using asyncio library, to model the following:
	* Each node runs concurrently
	* Sending of messages has to be done concurrently
	* The receiving of an individual message is finished completely as an atomic operation