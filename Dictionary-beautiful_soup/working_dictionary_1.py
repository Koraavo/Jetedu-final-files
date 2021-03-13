import requests
from bs4 import BeautifulSoup
import json
import csv


class Basescraper:
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    def fetch(self, url):
        print(f'HTTP GET REQUESTS TO URL: {url}', end="")
        res = requests.get(url, headers=self.headers)
        print(f' | STATUS CODE: {res.status_code}')
        return res

    def save_response(self, html):
        with open('reverso.html', 'w', encoding='utf-8') as base_html:
            base_html.write(html.text)

    def load_response(self):
        html = ''
        with open('reverso.html', 'r', encoding='utf-8') as base_html:
            for line in base_html:
                html += line
        return html

    def parse(self, html):
        content = BeautifulSoup(html.text, 'html.parser')
        # print(content.prettify())
        print('Translations')
        trans_words = []
        sentences = []
        translation_content = content.findAll('div', {'id':'translations-content'})
        sentences_content = content.findAll('div', {'class': 'example'})
        for trans in translation_content:
            words = trans.text
            for each_word in words.split():
                trans_words.append(each_word)
        print(trans_words)

        for each_sentence in sentences_content:
            eng = each_sentence.find('div', {'class': 'src ltr'}).text.strip()
            fr = each_sentence.find('div', {'class': 'trg ltr'}).text.strip()
            sentences.append(eng)
            sentences.append(fr)
        print(sentences)


    def run(self):
        base_url = f'https://context.reverso.net/translation'
        base_language = input('Select your base language')
        translate_language = input('Select the language you wish the word translated into')
        languages = f'{base_language}-{translate_language}'
        word = input('Type the word you want to translate:\n')
        final_url = f'{base_url}/{languages}/{word}'
        # test_url = 'https://context.reverso.net/translation/english-french/hello'
        # res = self.fetch(test_url)
        # self.save_response(res)
        # html = self.load_response()
        self.parse(final_url)


if __name__ == '__main__':
    scraper = Basescraper()
    scraper.run()