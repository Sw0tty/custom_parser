"""
File with help commands
"""


class HelpModule:
    
    def __init__(self) -> None:
        self.__temp_dict = {
            'None-module': {},
            'file-parser': {
                '1': 'get current parse file',
                '2': 'set new parse file',
                '3': 'get name file',
                '4': 'parse the file',
                '5': 'export in excel file',
            },
            'site-parser': {
                '1': 'new parse',
                '2': 'add to export',
                '3': 'export to excel',
                '4': 'get url',
            },
            'rebuilder': {
                '1': 'set file for rebuild',
                '2': 'get parametrs status',
                '3': 'get file name',
                '4': 'check rebuild info',
                '5': 'prepare rebuild to export in excel file',
                '6': 'export rebuild in excel file',
            },
            'manager': {
                '1': 'create new config',
                '2': 'add parsing site',
                '3': 'add parsing site page',
                '4': 'set site config from file',                
            }
        }

        self.__default_commands = {
                'set': 'set module',
                'reset': 'reset current module',
                'exit': 'close parser',
            }
        
        self.help_dict = self.__create_help_dict()

    
    def __create_help_dict(self):
        for key in self.__temp_dict.keys():
            for s_key in self.__default_commands.keys():
                self.__temp_dict[key][s_key] = self.__default_commands[s_key]
        return self.__temp_dict

    def help(self, module):
        for key in self.help_dict[module].keys():
            print(f'\t{key} - {self.help_dict[module][key]}')


MODULES = {
    'rebuilder': 'rebuilding the excel file for template',
    'file-parser': 'parse the file',
    'site-parser': 'parse the site',
    'manager': 'config the config file',
}



# PARSER_COMMANDS_DICT = {
#     '1': 'all commands in current module',
#     '2': 'get actual request type',
#     '3': 'set new request type',
#     '4': 'get actual parse source',
#     '5': 'set new parse source',
#     '6': 'parse the resource',
#     '7': 'get name file',
#     '8': 'export in excel file',
# }
