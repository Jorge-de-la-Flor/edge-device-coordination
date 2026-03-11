Español | Inglés (README.es.md)

# Coordinación de Dispositivos de Borde

Experimentos mínimos que ilustran patrones de coordinación para dispositivos de borde distribuidos.

Este repositorio explora mecanismos de coordinación simples que se utilizan comúnmente en sistemas integrados distribuidos y entornos de computación de borde.

Los ejemplos demuestran cómo se pueden utilizar los registros de dispositivos, la monitorización de latidos y los nodos de servicio para coordinar múltiples dispositivos en un sistema distribuido.

## Contenido

El directorio `src/` contiene tres experimentos mínimos:

* `device_registry.py`

    Implementa un registro de dispositivos simple que se utiliza para rastrear nodos activos en un sistema distribuido.

* `heartbeat_monitor.py`

    Simula la monitorización de latidos para detectar fallos o desconexiones de dispositivos.

* `node_service.py`

    Demostración de un servicio de nodo simple que se registra periódicamente y envía señales de latidos.

## Propósito

Estos experimentos ilustran conceptos de ingeniería relevantes para:

* Sistemas integrados distribuidos
* Arquitecturas de computación en el borde
* Coordinación de dispositivos
* Detección de fallos en sistemas en red

## Motivación

La robótica moderna y los sistemas ciberfísicos dependen cada vez más de redes de dispositivos distribuidos que operan en el borde.

La coordinación de múltiples dispositivos requiere mecanismos para el descubrimiento de dispositivos, la detección de actividad y la coordinación de servicios.

Estos patrones se utilizan ampliamente en sistemas de IoT, plataformas de robótica distribuida e infraestructuras de computación en el borde.

## Método

El repositorio implementa mecanismos de coordinación simplificados que se utilizan comúnmente en sistemas distribuidos en el borde.

Los experimentos incluyen:

* Registro y descubrimiento de dispositivos
* Detección de fallos basada en latidos
* Coordinación de servicios de nodos simples

Estos ejemplos son intencionadamente minimalistas e ilustran mecanismos de coordinación conceptuales en lugar de sistemas de redes de producción completos.

## Ejecución de los ejemplos

Clonar el repositorio y ejecutar cualquiera de los scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/edge-device-coordination
cd edge-device-coordination
python src/device_registry.py
```

Cada script simula la coordinación distribuida de dispositivos e imprime la actividad del sistema en la consola.

## Árbol del proyecto

```bash
edge-device-coordination
├─ .python-version
├─ LICENSE
├─ README.es.md
├─ README.md
├─ pyproject.toml
├─ src
│  ├─ device_registry.py
│  ├─ heartbeat_monitor.py
│  └─ node_service.py
└─ uv.lock
```

## Requisitos

Los ejemplos utilizan:

* Python 3.12+

No se requieren dependencias externas.

## Referencias

* Tanenbaum, A. S. y Van Steen, M. (2017).
*Sistemas distribuidos.*

* Hightower, K., Burns, B. y Beda, J. (2017).
*Kubernetes: en funcionamiento.*
