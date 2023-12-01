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
    

