# parser_with_authorization.py
import requests
from bs4 import BeautifulSoup

session = requests.session() 

LOGIN_URL = 'http://51.250.32.149/login/'
response = session.get(LOGIN_URL)

soup = BeautifulSoup(response.text, features='lxml')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
print(session.cookies.get_dict()) 


if __name__ == '__main__':
    data = {
        'username': 'test_parser_user',
        'password': 'testpassword',
        'csrfmiddlewaretoken': csrf_token,
    }

    response = session.post(LOGIN_URL, data=data)
    
    response.encoding = 'utf-8'
    print(response.text) 