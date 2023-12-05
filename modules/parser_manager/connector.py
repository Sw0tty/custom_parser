from app_config.app_notices import SUCCESS, ERROR, WARNING, INFO


# class ConfigArgs:

#     def __init__(self) -> None:
#         self.main_site = None
        

class ConfigConnector:
    
    # def __init__(self) -> None:
    config = None
    site_config = None
    connected = False
    site_name = None
    
    def connect(self, config):
        self.site_name = config[1]
        self.connected = True
        self.config = config[0]

    def reset(self):
        config_dict = enumerate(self.config.keys())
        print(config_dict)
        for site in config_dict.keys():
            print(f"{site} - {config_dict[site]}")
        answer = input("Print a number of site name: ")
        if answer and answer in config_dict.keys():
            print(123123)
            # self.connect()
        return f"[{WARNING}] Cancelled."
    
    def check_connection(self):
        if self.connected:
            return f"[{INFO}] Now connected to '{self.site_name}'."
        return f"[{ERROR}] No connected to any site config."
    

