class Template:
    
    def __init__(self):
        self.template = {
                    "SECURE_CONNECTION": False,
                    "SITE_URL": "",
                    "PARSING_PAGES":
                        {
                            
                        },
                    
                    "EXPORT": {
                        "EXCEL": {
                            "EXCEL_COLUMNS_TITLE": [],
                            "ROW_COMMON_TITLES": []
                        },
                        "JSON": ""
                    }
                }
        self.page_template = {
            "PAGE_URL": "",
            "MAIN_PARSE_INFO_BLOCK": "",
            "INFO_BLOCKS":
                [   
                    
                ],
            "CUSTOM_FIELDS": [],
            "PAGINATOR_CLASS_NAME": ""
        }
        self.info_block_template = ["", "", ""]
        self.count_main_keys = len(self.template.keys())


if __name__ == '__main__':
    template = Template()
    print(template.count_main_keys)

exclude_words = ["для нужд", "томограф", "для ООО", "мебел", "вентиляц", "видеонаб", "видеооб", "планшет", "проектор", "медицинского", "тонометр", "водян", "вентилятор"]

# Оказание услуг по монтажу водяных тепловых вентиляторов с поставляемым товаром
# self.template = {
#                     "SECURE_CONNECTION": False,
#                     "PARSING_PAGES":
#                         {
#                             "page_name":
#                                 {   
#                                     "PAGE_URL": "",
#                                     "MAIN_PARSE_INFO_BLOCK": "",
#                                     "INFO_BLOCKS":
#                                         [   
#                                             ["", "", ""]
#                                         ],
#                                     "CUSTOM_FIELDS": []
#                                 }
#                         },
#                     "PAGINATOR_CLASS_NAME": "",
#                     "EXPORT": {
#                         "EXCEL": {
#                             "EXCEL_COLUMNS_TITLE": [],
#                             "ROW_COMMON_TITLES": []
#                         },
#                         "JSON": ""
#                     }
#                 }


# {
#     "zakupki.gov.ru": 
#         {
#             "SECURE_CONNECTION": "True",
#             "PARSING_PAGES":
#                 { 
#                     "Закупки":
#                         {   
#                             "PAGE_URL": "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={search_str}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={page}&recordsPerPage=_{self.__RESULTS_PER_PAGE}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}",
#                             "MAIN_PARSE_INFO_BLOCK": "search-registry-entry-block box-shadow-search-input",
#                             "INFO_BLOCKS":
#                                 [   
#                                     ["False", "col-9 p-0 registry-entry__header-top__title text-truncate", "None"],
#                                     ["False", "registry-entry__body-value", "None"],
#                                     ["False", "price-block__value", "None"],
#                                     ["False", "registry-entry__body-href", "None"],
#                                     ["False", "data-block mt-auto", "None"],
#                                     ["True", "'CUSTOM_FIELDS'[0]", "None"],
#                                     ["True", "", "None"],
#                                     ["False", "registry-entry__header-mid__number", "None"]
#                                 ],
#                             "CUSTOM_FIELDS": []
#                         }
#                 },
#             "PAGINATOR_CLASS_NAME": "paginator-block",
#             "EXPORT": {
#                 "EXCEL": {
#                     "EXCEL_COLUMNS_TITLE": ["Закупки по", "Наименование закупки", "Начальная (максимальная) цена контракта",
#                             "Наименование заказчика", "Дата окончания подачи заявок", "Интерес",
#                             "Категория", "Ссылка"],
#                     "ROW_COMMON_TITLES": []
#                 },
#                 "JSON": ""
#             }
#         }
# }
