#!/usr/bin/env python3
"""
gcode_sender.py – Tiny script to send one or more G-code commands to a
Marlin-compatible printer and echo the printer’s reply.

Usage:
    python gcode_sender.py /dev/ttyUSB0 250000 "G28" "M114"
                           ^port        ^baud     ^commands...
"""

import sys
import time
import serial          # pip install pyserial
from pathlib import Path


def send_gcode(port: str, baud: int, commands: list[str], timeout=5):
    """Open serial, send each command, print printer responses."""
    print(f"Opening {port} @ {baud} baud …")
    with serial.Serial(port, baud, timeout=timeout) as ser:
        # Give the controller a moment to reset on DTR toggle
        time.sleep(2)
        for cmd in commands:
            line = f"{cmd}\n"
            ser.write(line.encode("ascii"))
            #ser.write(b'G0 X200\n') convets to bit
            print(f">> {cmd}")
            # Read until we get 'ok' or timeout
            while True:
                response = ser.readline().decode("utf-8", "ignore").strip()
                if response:
                    print(f"<< {response}")
                if response.lower().startswith("ok"):
                    break
        # Auto-flush and close when leaving the 'with' block
    print("Done.")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        exe = Path(sys.argv[0]).name
        print(f"Usage: python {exe} <port> <baud> <G-code1> [G-code2] …")
        sys.exit(1)

    port_name   = sys.argv[1]
    baud_rate   = int(sys.argv[2])
    gcode_lines = sys.argv[3:]
    send_gcode(port_name, baud_rate, gcode_lines)
    print("Hallo")
    print(sys.argv[1],int(sys.argv[2],sys.argv[3:]))
    # gcode=["G0 X 200","G0 Y 250"]
    # send_gcode('COM10', 9600 ,gcode)
