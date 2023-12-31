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
        self.info_block_template = ["", ["", ""]]  # class_name, stylers_names
        self.count_main_keys = len(self.template.keys())


if __name__ == '__main__':
    template = Template()
    print(template.count_main_keys)

    class Status:
        def __init__(self, name: str, selection: set) -> None:
            self.name = name
            self.selection = selection

    class SelectionStyler:
        def __init__(self, *args) -> None:
            pass
    

exclude_words = ["для нужд", "медицинских издел", "допплерограф", "томограф", "для ооо", "мебел", "вентиляц", "строительство", "фотовидеофикс", "экстренных", "типограф",
                 "видеонаб", "видеооб", "планшет", "проектор", "медицинского", "тонометр", "водян", "вентилятор", "радиостанц", "гликем", "полиграф", "помещен",
                 "киоск", "лингафон"]

# For status = 1
status_1 = ["развитию и модернизации", "выполнение работ по развитию", "выполнение работ по расширению", "модернизации и развитию програм", "созданию системы",
            "модификации информационной сис"]

# For status = 2
status_2 = ["адаптации и сопровождению", "техническому сопровождению комплекса", "оказание услуг по поддержке", "заправка картриджей", "техническое обслуживание и ремонт",
            "сопровождение справочно-правовой системы", "внедрению и сопровождению", "сопровождению программного продукта", "планового обслуживания", "ремонту оргтехники",
            "сопровождению и обновлению", "услуги консульта", "обслуживанию оргтехники", "восстановлению картриджей", "техническому обслуживанию инфо", "ремонту офисной техники",
            "оказание услуг по сопровождению автоматизированной системы", "сопровождению и развитию", "оказание услуг по предоставлению неисключительных", "размещению сервер",
            "ремонту картриджей", "оказание услуг по сопровождению", "оказание услуг по предоставлению сертифик", "услуги по техническому  сопровождению эксплуатации федер",
            "адаптация и сопровождение экземпляров", "услуги по сопровождению экземпляров", "оказание услуг по предоставлению доступа сети", "обновление и сопровождение продуктов",
            "обслуживанию копировально-множительной техники", "техническое обслуживание принтеров", "услуги по сопровождению по", "развитию и сопровождению гос",
            "на условиях простой (неисключительной)", "обслуживанию и ремонту компь", "оказание услуг по техническому сопровождению", "аналитическому сопровождению",
            "оказание услуг на продление прав", "сопровождению сервера", "ремонт оргтехники", "заправке компьютерной оргтехники", "продление действия серт",
            "сопровождению и эксплуа", "технической поддержке и систем", "технической поддержке и обнов", "заправке картриджей", "продлению лицен", "ремонта компью",
            "сопровождению программного комп", "восстановление картриджей", "сопровождения экземпляров", "обслуживанию печатно-множитель", "продлению лицензий на програм",
            "ремонту вычислительной и оргтех", "продление прав на использ", "техническое обслуживание оргтех", "поставке обновлений програм", "техническому обслуживанию програм",
            "техническому обслуживанию компью", "обслуживанию единой информац", "оказание услуг по обслуживанию лицен", "услуги по сопровождению единого комплекс",
            "оказание информационных услуг с использ"]

# For status = 3
status_3 = ["поставка компью", "поставка клавиатур", "поставка монитор", "поставка мыш", "системные блоки", "монитор", "передаче лицензии", "предоставлению простых",
            "приобретению неисключительного права", "компьютерной периферии", "поставка оргтехники", "предоставление права использования", "услуги по передаче",
            "серверного оборудования", "поставка сервера", "неисключительных прав", "моноблока", "поставка запасных частей для компью", "поставка офисной и компью",
            "поставка комплектующих для персональных компью", "поставка бумаги для офис", "предоставлению лицензий на право исполь", "компьютеры и перифер",
            "закупка комплектующих для компью", "компьютерное оборудов", "компьютерного оборудование", "поставка периферийного оборуд",
            "поставка комплектующих к оргтехнике", "приобретение лицензий антивирусной защиты", "приобретение права на использование"]

# For FilterStyler
accepted_words = ["компью", "сервер", "оргтехник", "клавиатур", "моноблок", "перифер", "мфу", "монитор", "мыш", "лиценз", "картридж",
                  "поддержк", "обслуживан", "сопровожден", "модернизац", "програм", "ремонт", "поставк", "обслуживан", "продлен",
                  "неисключитель", "копировально-множитель", "принтер", "внедрен", "печатно-множитель", "вычислитель", "1с", "1c",
                  "kaspersky", "консультант плюс", "консультантплюс", "многофункц", "факс", "копир", "скан", "a4", "а4", "office",
                  "windows", "microsoft", "свт", "систем"]

status_1_mod = ["развити", "модернизац", "адаптаци", "развити", "автоматизаци", "разработ"]
status_2_mod = ["поддержк", "обслуживан", "сопровожден", "ремонт", "продлен", "замен", "консультац", "обработк", "доступ", "восстановлен", "заправ", "информацион"]
status_3_mod = ["поставк", "предоставлен", "закупк", "передач", "приобретен"]


def get_correct_words(*args: list) -> list:
    correct_words = list()
    for list_ in args:
        correct_words.extend(list_)
    return correct_words

correct_words = get_correct_words(status_1, status_2, status_3)

# while True:
    
#     input_word = input("Some: ").strip().lower()

#     def check(input_word):
#         for word in accepted_words:
#             if word in input_word:
#                 return True
#         return False
    
#     def set_status(input_word):
#         for status in status_1_mod:
#             if status in input_word:
#                 return print("Status: 1")
#         for status in status_2_mod:
#             if status in input_word:
#                 return print("Status: 2")
#         for status in status_3_mod:
#             if status in input_word:
#                 return print("Status: 3")
#         return "Status: Undefined"
    
#     if check(input_word):
#         print(set_status(input_word))
#     else:
#         print("Bad data!")

    




# Status field Styler
# Version 1: Take words (set words) from set and printing status in field
# Example: 
# status_1 = ["word", "set words in string"]
# status = "1" if word in status_1 else "Another status"

# Version 2 (mod version 1): Take words (only 1 word in string) from set 
# Example: 
# selection_words = ["word", "string", "some"]
# status_1 = ["making", "building"]
# for selection in selection_words:
#   if selection in some_data:
#       for status in status_1:
#           status = "1" if status in some_data else "Another status" 

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
