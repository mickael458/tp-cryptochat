from ciphered_gui import *
import dearpygui.dearpygui as dpg

from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
import base64
from basic_gui import *
from cryptography.fernet import Fernet
import hashlib
from generic_callback import GenericCallback

class FernetGUI(CipheredGUI):


    def run_chat(self, sender, app_data)->None:
        # callback uskeyed by the connection windows to start a chat session
        host = dpg.get_value("connection_host")
        port = int(dpg.get_value("connection_port"))
        name = dpg.get_value("connection_name")
        password = dpg.get_value("connection_password")
        self._log.info(f"Connecting {name}@{host}:{port}")

        self._callback = GenericCallback()

        self._client = ChatClient(host, port)
        self._client.start(self._callback)
        self._client.register(name)
         # generating key
        self.key = hashlib.sha256(password.encode("utf-8").digest())
        self.key = base64.b64encode(self.key)
      
        dpg.hide_item("connection_windows")
        dpg.show_item("chat_windows")
        dpg.set_value("screen", "Connecting")



    def encrypt(self, message):
        '''
        chiffre le message avec Fernet
        '''
        message_bytes = bytes(message,'utf-8')
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(message_bytes)
        return cipher_text

    def decrypt(self, message: bytes):
        cipher_suite= Fernet(self.key)
        text_bytes = cipher_suite.decrypt(message.encode('utf-8'))
        plain_text = text_bytes.decode('utf-8')
        return plain_text
    
if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = FernetGUI()
    client.create()
    client.loop()




