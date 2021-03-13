import os

import requests
from bs4 import BeautifulSoup
import time


class Basescraper :
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    urls = []
    base_url = f'https://context.reverso.net/translation'
    language_dict = {'1' : 'Arabic', '2' : 'German', '3' : 'English',
                     '4' : 'Spanish', '5' : 'French', '6' : 'Hebrew',
                     '7' : 'Japanese', '8' : 'Dutch', '9' : 'Polish',
                     '10' : 'Portuguese', '11' : 'Romanian',
                     '12' : 'Russian', '13' : 'Turkish'}
    trans_words = []
    src_sentences = []
    tar_sentences = []
    results = []

    def fetch(self, url) :
        # print(f'HTTP GET REQUESTS TO URL: {url}', end="")
        s = requests.Session()
        res = s.get(url, headers=self.headers)
        # print(f' | STATUS CODE: {res.status_code}')
        return res

    def save_response(self, html) :
        with open('reverso.html', 'w', encoding='utf-8') as base_html :
            base_html.write(html.text)

    def load_response(self) :
        html = ''
        with open('reverso.html', 'r', encoding='utf-8') as base_html :
            for line in base_html :
                html += line
        return html

    def save_astext(self, word, target_language) :
        with open(f'{word}.txt', 'w', encoding='utf-8') as f :
            # f.write(str(self.results))
            for index, words in enumerate(self.trans_words) :
                print(f'{target_language[index]} Translations', file=f)
                print(words[0], file=f)
                print(file=f)
                print(f'{target_language[index]} Example:', file=f)
                print(f'{self.src_sentences[index][0]}:', file=f)
                print(self.tar_sentences[index][0], file=f)
                print(file=f)

    def read_txt(self, word) :
        if os.access(f'{word}.txt', os.R_OK):
            with open(f'{word}.txt', encoding='utf-8') as word_tr :
                print(word_tr.read())
        else:
            print("The word is not translated yet.")

    def parse_words(self, html) :
        content = BeautifulSoup(html.text, 'html.parser')
        translation_content = content.findAll('div', {'id' : 'translations-content'})
        for trans in translation_content :
            words = trans.text.split()
            self.trans_words.append(words)

    def parse_sentences(self, html, each_url) :
        target_language = each_url.split('/')[-2].split('-')[-1]
        base_language = each_url.split('/')[-2].split('-')[0]
        content = BeautifulSoup(html.text, 'html.parser')
        # content = BeautifulSoup(html, 'html.parser')

        # print(content.prettify())
        sentences_content = content.findAll('div', {'class' : 'example'})
        src_list = []
        tar_list = []
        for each_sentence in sentences_content:
            if 'arabic' in base_language :
                src = each_sentence.find('div', {'class' : 'src rtl arabic'}).text.strip()
                src_list.append(src)
                if 'hebrew' in target_language :
                    tar = each_sentence.find('div', {'class' : 'trg rtl'}).text.strip()
                else :
                    tar = each_sentence.find('div', {'class' : 'trg ltr'}).text \
                        .strip() \
                        .replace('[', '') \
                        .replace(']', '')
                tar_list.append(tar)

            elif 'arabic' in target_language :
                tar = each_sentence.find('div', {'class' : 'trg rtl arabic'}).text.strip()
                tar_list.append(tar)
                if 'hebrew' in base_language :
                    src = each_sentence.find('div', {'class' : 'src rtl'}).text \
                        .strip() \
                        .replace('[', '') \
                        .replace(']', '')
                else :
                    src = each_sentence.find('div', {'class' : 'src ltr'}).text \
                        .strip() \
                        .replace('[', '') \
                        .replace(']', '')
                src_list.append(src)

            elif 'hebrew' in base_language :
                src = each_sentence.find('div', {'class' : 'src rtl'}).text \
                    .strip() \
                    .replace('[', '') \
                    .replace(']', '')
                src_list.append(src)
                if 'arabic' in target_language :
                    tar = each_sentence.find('div', {'class' : 'trg rtl arabic'}).text.strip()
                else :
                    tar = each_sentence.find('div', {'class' : 'trg ltr'}).text \
                        .strip() \
                        .replace('[', '') \
                        .replace(']', '')
                tar_list.append(tar)

            elif 'hebrew' in target_language :
                tar = each_sentence.find('div', {'class' : 'trg rtl'}).text \
                    .strip() \
                    .replace('[', '') \
                    .replace(']', '')
                tar_list.append(tar)
                if 'arabic' in base_language :
                    src = each_sentence.find('div', {'class' : 'src rtl arabic'}).text.strip()
                else :
                    src = each_sentence.find('div', {'class' : 'src ltr'}).text \
                        .strip() \
                        .replace('[', '') \
                        .replace(']', '')
                src_list.append(src)

            else :
                src = each_sentence.find('div', {'class' : 'src ltr'}).text.strip().replace('[', '').replace(']', '')
                tar = each_sentence.find('div', {'class' : 'trg ltr'}).text.strip().replace('[', '').replace(']', '')
                src_list.append(src)
                tar_list.append(tar)
        self.src_sentences.append(src_list)
        self.tar_sentences.append(tar_list)


    def combine_url(self, base_language, target_language, url, word):
        languages = f'{base_language}-{target_language}'
        final_url = f'{url}/{languages}/{word}'.lower()
        self.urls.append(final_url)

    def get_finalurl(self, url, tar_number, base_number, base_language, word) :
        if tar_number == '0' :
            for elements in self.language_dict :
                if base_number != elements :
                    target_language = self.language_dict.get(elements)
                    self.combine_url(base_language, target_language, url, word)

        else :
            target_language = self.language_dict.get(tar_number)
            self.combine_url(base_language, target_language, url, word)
        return self.urls

    def run(self) :
        base_url = f'https://context.reverso.net/translation'
        print("Hello, you're welcome to the translator. Translator supports: ")
        for key, lang in self.language_dict.items() :
            print(key, lang)
        base_number = input('Type the number of your language:\n')
        base_language = self.language_dict.get(base_number)
        tar_number = input('Type the number of a language you want to translate to or "0" to '
                           'translate to all languages:\n')
        word = input('Type the word you want to translate:\n')

        final_url = self.get_finalurl(base_url, tar_number, base_number, base_language, word)
        target_language = [each_url.split('/')[-2].split('-')[-1].capitalize() for each_url in final_url]

        for each_url in final_url :
            res = self.fetch(each_url)
            if res.ok :
                print(res.status_code, 'OK')
                self.parse_words(res)
                self.parse_sentences(res, each_url)
                # time.sleep(2)

        for index, words in enumerate(self.trans_words) :
            self.results.append([words[0], self.src_sentences[index][0], self.tar_sentences[index][0]])
        self.save_astext(word, target_language)
        self.read_txt(word)


        # for i in range(2):
        #     html = self.load_response()
        #     self.parse_words(html)
        #     self.parse_sentences(html)


if __name__ == '__main__' :
    scraper = Basescraper()
    scraper.run()