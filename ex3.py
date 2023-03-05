# Импортируйте модуль для работы с регулярными выражениями.
import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. ' 
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

results = []
for address in addresses:
    # Напишите регулярное выражение.
    pattern = r'город.? (?P<town>\w+).*улиц.? (?P<street>\w+).*дом.? (?P<house>\d+).*квартир.? (?P<apartment>\d+)'

    
    # Примените метод регулярных выражений, который 
    # найдёт шаблон pattern в строке address.
    address_match = re.search(pattern, address)
    town, street, house, appartment = address_match.groups()
    # Распечатайте названия городов и улиц, номера домов и квартир
    # из обеих строк.
    results.append((town, street, house, appartment))
for row in results:    
    print(*row)