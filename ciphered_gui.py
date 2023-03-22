from cryptography.hazmat.backends import default_backend
from basic_gui import *
import dearpygui.dearpygui as dpg
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
import os
import base64

from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import padding
import base64
class CipheredGUI(BasicGUI):

    def init_(self, key=None):
        super()._init()
        self._key = key


    def _create_connection_window(self):
        # windows about connexion
        with dpg.window(label="Connection", pos=(200, 150), width=400, height=300, show=False, tag="connection_windows"):
            
            for field in ["host", "port", "name"]:
                with dpg.group(horizontal=True):
                    dpg.add_text(field)
                    dpg.add_input_text(default_value=DEFAULT_VALUES[field], tag=f"connection_{field}")
            
            #ajout d'un mot de passe
            dpg.add_text("password")      
            dpg.add_input_text(password=True,tag="connection_password")
            dpg.add_button(label="Connect", callback=self.run_chat)

    def run_chat(self, sender, app_data)->None:
        # callback used by the connection windows to start a chat session
        host = dpg.get_value("connection_host")
        port = int(dpg.get_value("connection_port"))
        name = dpg.get_value("connection_name")
        password = dpg.get_value("connection_password")
        self._log.info(f"Connecting {name}@{host}:{port}")

        self._callback = GenericCallback()

        self._client = ChatClient(host, port)
        self._client.start(self._callback)
        self._client.register(name)

   
        #Taille de la clé en octets
        key_size = 32
        nb_iterations= 100000
        #Dérivation de clé 
        salt = b"data"
        key= PBKDF2HMAC(algorithm=hashes.SHA256(),length = key_size,salt=salt,iterations = nb_iterations,backend=default_backend()).derive(password.encode())
        b_password = bytes(password,"utf8")
        self.key = key.derive(b_password)
        self.log.info()
        dpg.hide_item("connection_windows")
        dpg.show_item("chat_windows")
        dpg.set_value("screen", "Connecting")

    def encrypt(self,message: str)-> tuple[bytes, bytes]:
        #choix clé de chiffrement
        iv=os.urandom(16)
        key = os.urandom(32)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(b"a secret message") + encryptor.finalize()
        decryptor = cipher.decryptor()
        decryptor.update(ct) + decryptor.finalize()



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = BasicGUI()
    client.create()
    client.loop()




