from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_largest_holds(html: urlopen.read().decode('utf-8')):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('div', class_='largest-holds')