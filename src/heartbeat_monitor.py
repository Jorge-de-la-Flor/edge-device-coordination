"""
Heartbeat monitoring simulation.

Detects inactive devices using periodic heartbeat signals.
"""

from dataclasses import dataclass, field
import time


@dataclass
class HeartbeatMonitor:
    """Monitor that tracks device heartbeats and detects timeouts.

    Each device is associated with its last heartbeat timestamp, and any
    device that exceeds the configured timeout is considered inactive.
    """

    timeout: float = 3.0
    heartbeats: dict[str, float] = field(default_factory=dict)

    def receive_heartbeat(self, device_id: str) -> None:
        """Record a heartbeat from a device.

        Args:
            device_id: Unique identifier of the device sending the heartbeat.
        """
        self.heartbeats[device_id] = time.time()
        print(f"Heartbeat received from {device_id}")

    def check_devices(self) -> None:
        """Check for devices that have missed their heartbeat deadline.

        Devices whose last heartbeat timestamp is older than the timeout
        are reported and removed from the active registry.
        """
        now = time.time()

        for device, timestamp in list(self.heartbeats.items()):
            if now - timestamp > self.timeout:
                print(f"Device timeout detected: {device}")
                del self.heartbeats[device]


if __name__ == "__main__":
    monitor = HeartbeatMonitor()

    monitor.receive_heartbeat("sensor-node-1")
    time.sleep(1)
    monitor.receive_heartbeat("sensor-node-2")

    time.sleep(4)

    monitor.check_devices()
