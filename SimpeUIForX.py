#!/usr/bin/env python3
"""
Very small Tkinter UI for jogging the X-axis of a Marlin/Grbl-style
machine over a serial port.

• Choose COM port and baud rate, press Connect  
• X+, X- step the axis ±10 mm and send “G0 X<pos>”  
• X Home returns to X 0  
"""

import sys
import time
import tkinter as tk
from tkinter import ttk, messagebox

import serial
import serial.tools.list_ports as ports


class JogApp(tk.Tk):
    STEP = 10                    # millimetres per click

    def __init__(self):
        super().__init__()
        self.title("Simple G-code Jogger")

        # ---------------------------------------------------- connection area
        top = ttk.LabelFrame(self, text="Connection")
        top.grid(column=0, row=0, sticky="ew", padx=10, pady=6)

        ttk.Label(top, text="COM port").grid(column=0, row=0, padx=4, pady=2)
        self.port_var = tk.StringVar(value="")                     # will hold COM?
        self._populate_ports()                                     # add list
        self.port_menu = ttk.OptionMenu(top, self.port_var, self.port_var.get(),
                                        *self.ports)
        self.port_menu.grid(column=1, row=0, padx=4, pady=2)

        ttk.Label(top, text="Baud rate").grid(column=2, row=0, padx=4, pady=2)
        self.baud_var = tk.StringVar(value="9600")
        ttk.Entry(top, textvariable=self.baud_var, width=8).grid(
            column=3, row=0, padx=4, pady=2)

        self.connect_btn = ttk.Button(
            top, text="Connect", command=self.toggle_connection)
        self.connect_btn.grid(column=4, row=0, padx=6, pady=2)

        # ---------------------------------------------------- jog area
        jog = ttk.LabelFrame(self, text="Jog X-axis")
        jog.grid(column=0, row=1, sticky="ew", padx=10, pady=6)

        self.xpos = 0
        self.pos_lbl = ttk.Label(jog, text=f"X = {self.xpos} mm", width=14)
        self.pos_lbl.grid(column=1, row=0, padx=10, pady=4)

        self.btn_minus = ttk.Button(jog, text="X-",  command=self.step_minus)
        self.btn_home  = ttk.Button(jog, text="X home", command=self.home_axis)
        self.btn_plus  = ttk.Button(jog, text="X+",  command=self.step_plus)

        self.btn_minus.grid(column=0, row=1, padx=4, pady=4)
        self.btn_home.grid(column=1,  row=1, padx=4, pady=4)
        self.btn_plus.grid(column=2,  row=1, padx=4, pady=4)

        for b in (self.btn_minus, self.btn_home, self.btn_plus):
            b["state"] = "disabled"          # until serial open

        self.bind("<Destroy>", lambda *_: self._close_port())       # tidy exit
        self.ser = None

    # ----------------------------------------------------------------- ports
    def _populate_ports(self):
        self.ports = [p.device for p in ports.comports()] or ["COM1"]

    # -------------------------------------------------------- connect / close
    def toggle_connection(self):
        if self.ser and self.ser.is_open:          # disconnect
            self._close_port()
            self.connect_btn["text"] = "Connect"
            for b in (self.btn_minus, self.btn_home, self.btn_plus):
                b["state"] = "disabled"
        else:                                      # connect
            try:
                self.ser = serial.Serial(
                    self.port_var.get(), int(self.baud_var.get()),
                    timeout=1, dsrdtr=True)       # dsrdtr avoids auto-reset
                time.sleep(2)                     # let board settle
            except serial.SerialException as e:
                messagebox.showerror("Serial error", str(e))
                return
            self.connect_btn["text"] = "Disconnect"
            for b in (self.btn_minus, self.btn_home, self.btn_plus):
                b["state"] = "normal"

    def _close_port(self):
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()
        except serial.SerialException:
            pass

    # ------------------------------------------------------------- g-code send
    def _send(self, cmd: str):
        try:
            self.ser.write(f"{cmd}\n".encode())
            self.ser.flush()
        except serial.SerialException:
            messagebox.showerror("Serial error", "Lost connection.")
            self.toggle_connection()

    # ------------------------------------------------------------ jog actions
    def _update_pos_label(self):
        self.pos_lbl.config(text=f"X = {self.xpos} mm")

    def step_plus(self):
        self.xpos += self.STEP
        self._send(f"G0 X{self.xpos}")
        self._update_pos_label()

    def step_minus(self):
        self.xpos -= self.STEP
        self._send(f"G0 X{self.xpos}")
        self._update_pos_label()

    def home_axis(self):
        self.xpos = 0
        self._send("G28 X")             # or "G0 X0"
        self._update_pos_label()


if __name__ == "__main__":
    JogApp().mainloop()
