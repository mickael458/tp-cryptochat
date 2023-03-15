import logging 

import dearpygui.dearpygui as dpg 

import os 

from chat_client import ChatClient
from generic_callback import BasicGUI,DEFAULT_VALUES
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.backends import default_backend
from basic_gui import BasicGUI
import tkinter as tk
from tkinter import ttk


class CipheredGUI(BasicGUI):

    def init_(self, key=None):
        super()._init()
        self._key = key


    def _create_connection_window(self):
        window = super()._create_connection_window()
        password_label = ttk.Label(window, text="Password:")
        password_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)
        password_entry = ttk.Entry(window, show="*")
        password_entry.grid(column=1, row=1, sticky="w", padx=5, pady=5)
        return window


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = CipheredGUI()
    client.create()
    client.loop()

