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
        """getting the required request with the url"""
        # print(f'HTTP GET REQUESTS TO URL: {url}', end="")
        res = requests.get(url, headers=self.headers)
        # print(f' | STATUS CODE: {res.status_code}')
        return res

    def save_response(self, html) :
        """saving into html so that the website is not hammered"""
        with open('reverso.html', 'w', encoding='utf-8') as base_html :
            base_html.write(html.text)

    def load_response(self) :
        """creating a string file of the saved content"""
        html = ''
        with open('reverso.html', 'r', encoding='utf-8') as base_html :
            for line in base_html :
                html += line
        return html

    def save_astext(self, word, target_language) :
        """saving the final result as text"""
        with open(f'{word}.txt', 'w', encoding='utf-8') as f :
            # f.write(str(self.results))
            for index, words in enumerate(self.trans_words) :
                print(f'{target_language[index]} Translations', file=f)
                print(words[0], file=f)
                print(file=f)
                print(f'{target_language[index]} Example:', file=f)
                print(self.src_sentences[index][0], file=f)
                print(self.tar_sentences[index][0], file=f)
                print(file=f)

    def read_txt(self, word) :
        """reading from the saved text file"""
        if os.access(f'{word}.txt', os.R_OK):
            with open(f'{word}.txt', encoding='utf-8') as word_tr :
                print(word_tr.read())
        else:
            print("The word is not translated yet.")

    def parse_words(self, html) :
        """Actual parsing for words is done here"""
        content = BeautifulSoup(html.content, 'html.parser')
        translation_content = content.findAll('div', {'id' : 'translations-content'})
        for trans in translation_content :
            words = trans.text.split()
            self.trans_words.append(words)

    def parse_sentences(self, html, each_url) :
        """All sentences are parsed here"""
        target_language = each_url.split('/')[-2].split('-')[-1]
        base_language = each_url.split('/')[-2].split('-')[0]
        content = BeautifulSoup(html.content, 'html.parser')
        # print(content.prettify())
        sentences_content = content.findAll('div', {'class' : 'example'})
        src_list = []
        tar_list = []
        for each_sentence in sentences_content:
            # arabic and hebrew as base/target languages have a different class
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

    def get_finalurl(self, url, tar_number, base_number, base_language, word) :
        """get the final list of urls without the same-language duo"""
        if tar_number == '0' :
            for elements in self.language_dict :
                if base_number != elements :
                    target_language = self.language_dict.get(elements)
                    languages = f'{base_language}-{target_language}'
                    final_url = f'{url}/{languages}/{word}'.lower()
                    self.urls.append(final_url)

        else :
            target_language = self.language_dict.get(tar_number)
            languages = f'{base_language}-{target_language}'
            final_url = f'{url}/{languages}/{word}'.lower()
            self.urls.append(final_url)
        return self.urls

    def run(self) :
        """Main running of the program is done here"""

        print("Hello, you're welcome to the translator. Translator supports: ")
        for key, lang in self.language_dict.items() :
            print(key, lang)

        base_number = input('Type the number of your language:\n')
        base_language = self.language_dict.get(base_number)

        tar_number = input('Type the number of a language you want to translate to or "0" to '
                           'translate to all languages:\n')

        word = input('Type the word you want to translate:\n')

        final_url = self.get_finalurl(self.base_url, tar_number, base_number, base_language, word)

        # handled this way since only the languages that we need to translate into need to be selected
        target_language = [each_url.split('/')[-2].split('-')[-1].capitalize() for each_url in final_url]

        for each_url in final_url :
            res = self.fetch(each_url)
            if res.ok :
                print(res.status_code, 'OK')
                self.parse_words(res)
                self.parse_sentences(res, each_url)
                # sleep so as to not hammer the website again
                time.sleep(5)

        # for index, words in enumerate(self.trans_words) :
        #     self.results.append([words[0], self.src_sentences[index][0], self.tar_sentences[index][0]])
        self.save_astext(word, target_language)
        self.read_txt(word)


if __name__ == '__main__' :
    scraper = Basescraper()
    scraper.run()
