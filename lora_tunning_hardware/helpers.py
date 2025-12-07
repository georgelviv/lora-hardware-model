import serial
import serial.tools.list_ports

from .utils import format_msg

def modules_reset(port_filter: str = "/dev/cu.usbserial", baudrate: int = 115200, timeout: float = 1.0) -> list[str]:
  """
  Reset all connected modules whose device names start with `port_filter`.

  Returns the list of ports successfully reset. Raises if no ports match or if
  any matched port fails to reset.
  """
  ports = [p.device for p in serial.tools.list_ports.comports() if p.device.startswith(port_filter)]
  if not ports:
    raise RuntimeError(f"No serial ports found matching filter '{port_filter}'")

  successes: list[str] = []
  failures: dict[str, Exception] = {}

  for port in ports:
    try:
      with serial.Serial(port=port, baudrate=baudrate, timeout=timeout) as ser:
        msg = format_msg("CONFIG_RESET")
        ser.write((msg + "\r\n").encode("utf-8"))
        ser.flush()
      successes.append(port)
    except serial.SerialException as exc:
      failures[port] = exc

  if failures:
    failed_ports = ", ".join(f"{p}: {err}" for p, err in failures.items())
    raise RuntimeError(f"Failed to reset ports [{failed_ports}]; successes: {successes}")

  return successes
