"""
"""


class MainMethods:

    def __init__(self, commands: dict):
        self.__commands = commands
        # self.EXPORT_DATA = deepcopy(EXCEL_TEMPLATE)
        # self.OPEN_ = deepcopy(OPENPX_EXCEL_TEMPLATE)

    def help(self):
        for key in self.__commands.keys():
            print(f'\t{key} - {self.__commands[key]}')

