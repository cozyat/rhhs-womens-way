import yaml
import json
import configparser
from cryptography.fernet import Fernet

large_json_data = {str(i): {'key_' + str(j): 'value_' + str(j) for j in range(1000)} for i in range(100)}
large_config_parser = configparser.ConfigParser()
for i in range(100):
    large_config_parser['section_' + str(i)] = {'key_' + str(j): 'value_' + str(j) for j in range(100)}

class ConfigurationManager:
    def __init__(self):
        self.config = {}

    def load_configuration(self, file_path):
        with open(file_path, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

    def save_configuration(self, file_path):
        with open(file_path, 'w') as file:
            yaml.dump(self.config, file)

    def get_configuration(self, key):
        return self.config.get(key)

    def set_configuration(self, key, value):
        self.config[key] = value

    def encrypt_data(self, data):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()
