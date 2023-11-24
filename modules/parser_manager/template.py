class Template:
    
    def __init__(self) -> None:
        self.template = {
                    "SECURE_CONNECTION": "",
                    "PARSING_PAGES":
                        {
                            "page_name":
                                {   
                                    "PAGE_URL": "",
                                    "MAIN_PARSE_INFO_BLOCK": "",
                                    "INFO_BLOCKS":
                                        [   
                                            ["", "", ""]
                                        ],
                                    "CUSTOM_FIELDS": []
                                }
                        },
                    "PAGINATOR_CLASS_NAME": "",
                    "EXPORT": {
                        "EXCEL": {
                            "EXCEL_COLUMNS_TITLE": [],
                            "ROW_COMMON_TITLES": []
                        },
                        "JSON": ""
                    }
                }
        