
from cryptography.hazmat.backends import default_backend
from basic_gui import *
import dearpygui.dearpygui as dpg
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import padding
import base64

class CipheredGUI(BasicGUI):

    def init_(self)->None:
        super()._init()
        self._key = None


    def _create_connection_window(self)->None: 
        # windows about connexion
        with dpg.window(label="Connection", pos=(200, 150), width=400, height=300, show=False, tag="connection_windows"):
            
            for field in ["host", "port", "name"]:
                with dpg.group(horizontal=True):
                    dpg.add_text(field)
                    dpg.add_input_text(default_value=DEFAULT_VALUES[field], tag=f"connection_{field}")
            
            self._log.info("Ajout d'un champ mot de passe")
            #ajout d'un mot de passe
            dpg.add_text("password")      
            dpg.add_input_text(password=True,tag="connection_password")
            dpg.add_button(label="Connect", callback=self.run_chat)

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

   
        #Taille de la clé en octets
        key_size = 16
        nb_iterations= 100000
        #Dérivation de clé 
        salt = b"data"
        kdf= PBKDF2HMAC(algorithm=hashes.SHA256(),length = key_size,salt=salt,iterations = nb_iterations)
        b_password = bytes(password,"utf8")
        self._key = kdf.derive(b_password)
        self._log.info(f"self.key {self._key}")
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
        crypt=decryptor.update(ct) + decryptor.finalize()
        self._log.info(f"message crypté{ crypt}")

def decrypt(self, message):
        '''
        message: message à déchiffrer

        Déchiffrer le message avec pkcs7 et retourner le message déchiffré
        '''
        #Récupérer l'iv depuis le tuple en base64
        iv = base64.b64decode(message[0]['data'])
        #Récupérer le message depuis le tuple en base64
        message = base64.b64decode(message[1]['data'])
        # Fonction qui déchiffre un message avec pkcs7
        decryptor = Cipher(
            algorithms.AES(self.key),
            modes.CBC(iv),
            backend=default_backend()
        ).decryptor()

        # Déchiffrer le message
        unpadder = padding.PKCS7(TAILLE_BLOCK).unpadder()
        data = decryptor.update(message) + decryptor.finalize()
        #retourner le message déchiffré
        return unpadder.update(data) + unpadder.finalize()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = CipheredGUI()
    client.create()
    client.loop()




