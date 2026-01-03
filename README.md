# lora-hardware-model

Python wrapper for the `lora-tunning-firmware` that speaks to the device over a serial port. It exposes a small async-friendly API to read the current radio configuration, push new parameters, and ping the firmware for health/telemetry data.

## Installation

```bash
pip install .
# or with Poetry
poetry install
```

Requirements: Python 3.12+, `pyserial`.

## License

MIT License — see `LICENSE`.
