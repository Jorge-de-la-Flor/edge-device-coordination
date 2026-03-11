"""
Simple edge node service.

Simulates a device that periodically sends heartbeat signals.
"""

import time


class NodeService:
    """Simulated edge node that periodically emits heartbeat messages.

    The node runs an infinite loop, sending a heartbeat at a fixed interval.
    """

    def __init__(self, node_id: str) -> None:
        """Initialize the node service.

        Args:
            node_id: Unique identifier for this edge node.
        """
        self.node_id = node_id

    def send_heartbeat(self) -> None:
        """Send a heartbeat signal.

        In a real system this would publish to a network endpoint;
        here it is printed to stdout.
        """
        print(f"{self.node_id} sending heartbeat")

    def run(self) -> None:
        """Run the node service loop indefinitely.

        Sends a heartbeat every 2 seconds.
        """
        while True:
            self.send_heartbeat()
            time.sleep(2)


if __name__ == "__main__":
    node = NodeService("edge-node-1")
    node.run()
