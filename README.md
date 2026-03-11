English | [Español](README.es.md)

# Edge Device Coordination

Minimal experiments illustrating coordination patterns for distributed edge devices.

This repository explores simple coordination mechanisms commonly used in distributed embedded systems and edge computing environments.

The examples demonstrate how device registries, heartbeat monitoring, and service nodes can be used to coordinate multiple devices in a distributed system.

## Contents

The `src/` directory contains three minimal experiments:

* `device_registry.py`

  Implements a simple device registry used to track active nodes in a distributed system.

* `heartbeat_monitor.py`

  Simulates heartbeat monitoring used to detect device failures or disconnections.

* `node_service.py`

  Demonstrates a simple node service that periodically registers itself and sends heartbeat signals.

## Purpose

These experiments illustrate engineering concepts relevant to:

* distributed embedded systems
* edge computing architectures
* device coordination
* fault detection in networked systems

## Motivation

Modern robotics and cyber-physical systems increasingly rely on networks of distributed devices operating at the edge.

Coordinating multiple devices requires mechanisms for device discovery, liveness detection, and service coordination.

These patterns are widely used in IoT systems, distributed robotics platforms, and edge computing infrastructures.

## Method

The repository implements simplified coordination mechanisms commonly used in distributed edge systems.

The experiments include:

* device registration and discovery
* heartbeat-based failure detection
* simple node service coordination

These examples are intentionally minimal and illustrate conceptual coordination mechanisms rather than full production networking systems.

## Running the examples

Clone the repository and run any of the scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/edge-device-coordination
cd edge-device-coordination
python src/device_registry.py
```

Each script simulates distributed device coordination and prints system activity in the console.

## Example output

![Device registry example](assets/device_registry.png)
![Heartbeat monitoring example](assets/heartbeat_monitor.png)

## Project tree

```bash
edge-device-coordination
├─ .python-version
├─ LICENSE
├─ README.es.md
├─ README.md
├─ assets
│  ├─ device_registry.png
│  └─ heartbeat_monitor.png
├─ pyproject.toml
├─ src
│  ├─ device_registry.py
│  ├─ heartbeat_monitor.py
│  └─ node_service.py
└─ uv.lock
```

## Requirements

The examples use:

* Python 3.12+

No external dependencies are required.

## References

* Tanenbaum, A. S., & Van Steen, M. (2017).
  *Distributed Systems.*

* Hightower, K., Burns, B., & Beda, J. (2017).
  *Kubernetes: Up and Running.*
