from bs4 import BeautifulSoup

class Parser:

    def __init__(self, raw):
        self.html = BeautifulSoup(raw, features="lxml")