"""
Changing parser_config.
"""
import json
from app_config.app_notices import SUCCESS, ERROR, WARNING 


class ConfigManager:
    
    def load_template(self):
        with open(r'path', 'r', 'utf-8') as config:
            config_file = json.loads(config)
        return config_file
    
    def set_name(self):
        pass
    
    def save_config(self, file):
        with open(r'path', 'w', 'utf-8') as config:
            json.dumps(file , config)
        return f'[{SUCCESS}] File saved.'

    
