"""
Validate parser_config before save or use.
"""
from template import Template
from app_config.app_notices import SUCCESS, ERROR, WARNING 


class Validator(Template):

    @staticmethod
    def validate_template(load_template, template) -> bool:
        if load_template() == template:
            return True
        return False

    @staticmethod
    def validate_secure_connection(connection) -> bool:
        return isinstance(connection, bool)

    @staticmethod
    def validate_name(name) -> bool:
        return isinstance(name, str)
    
    def validate_data(self):
        pass
    

