"""
Simple device registry for distributed edge systems.

Simulates registration and tracking of active devices in a network.
"""

from dataclasses import dataclass, field
import time


@dataclass
class DeviceRegistry:
    """Registry for tracking active devices.

    Stores device identifiers along with their last seen timestamp.
    """

    devices: dict = field(default_factory=dict)

    def register(self, device_id: str) -> None:
        """Register or update a device in the registry.

        Args:
            device_id: Unique identifier of the device.
        """
        self.devices[device_id] = time.time()
        print(f"Registered device: {device_id}")

    def list_devices(self) -> None:
        """Print all active devices and their last seen timestamps."""
        print("Active devices:")
        for device, timestamp in self.devices.items():
            print(f"{device} (last seen {timestamp:.2f})")


if __name__ == "__main__":
    registry = DeviceRegistry()

    registry.register("sensor-node-1")
    time.sleep(1)
    registry.register("camera-node-2")

    registry.list_devices()
