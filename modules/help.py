"""
File with help commands
"""


class HelpModule:
    
    def __init__(self) -> None:
        self.help_dict = {
            'None-module': {
                'set': 'set module',
                'exit': 'close master',
            },
            'file-parser': {
                '1': 'get current parse file',
                '2': 'set new parse file',
                '3': 'get name file',
                '4': 'parse the file',
                '5': 'export in excel file',
                'reset': 'reset current module',
            },
            'site-parser': {
                '1': 'new parse',
                '2': 'add to export',
                '3': 'export to excel',
                '4': 'get url',
                'reset': 'reset current module',
            },
            'rebuilder': {
                '1': 'set file for rebuild',
                '2': 'get parametrs status',
                '3': 'get file name',
                '4': 'check rebuild info',
                '5': 'prepare rebuild to export in excel file',
                '6': 'export rebuild in excel file',
                'reset': 'reset current module',
            },
            'manager': {
                '1': 'create new config',
                '2': 'add parsing site',
                'reset': 'reset current module',
            }
        }

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
