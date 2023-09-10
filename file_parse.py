from bs4 import BeautifulSoup


with open('zakup.html', 'r', encoding='utf-8') as file:
    content = file.read()

    soup = BeautifulSoup(content, 'lxml')

    print(soup.li)

