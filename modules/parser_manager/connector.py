from app_config.app_notices import SUCCESS, ERROR, WARNING, INFO


# class ConfigArgs:

#     def __init__(self) -> None:
#         self.main_site = None
        

class ConfigConnector:
    
    def __init__(self) -> None:
        self.connected = False
        self.site_name = None
    
    def connect(self):
        pass

    def check_connection(self):
        if self.connected:
            return f"[{INFO}] Now connected to '{self.site_name}'."
        return f"[{ERROR}] No connected to any site config."
    

