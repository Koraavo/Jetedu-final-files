import os
import sys

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

    def get_finalurl(self, url, base_language, target_language, word) :
        languages = f'{base_language}-{target_language}'
        final_url = f'{url}/{languages}/{word}'.lower()
        self.urls.append(final_url)
        return self.urls

    def run(self) :
        print("Hello, you're welcome to the translator. Translator supports: ")
        for key, lang in self.language_dict.items() :
            print(key, lang)
        base_number = input('Type the number of your language:\n')
        base_language = self.language_dict.get(base_number).lower()
        tar_number = input('Type the number of a language you want to translate to or "0" to '
                           'translate to all languages:\n')
        word = input('Type the word you want to translate:\n')

        target_languages = [lang.lower() for lang in list(self.language_dict.values())]
        target_languages.remove(base_language)

        if tar_number == '0' and tar_number != base_number:
            for each_language in target_languages:
                self.get_finalurl(self.base_url, base_language, each_language, word)
        else :
            target_language = self.language_dict.get(tar_number)
            self.get_finalurl(self.base_url, base_language, target_language, word)



        # for each_url in final_url:
        #     res = self.fetch(each_url)
        #     if res.ok :
        #         print(res.status_code, 'OK')
        #         self.parse_words(res)
        #         self.parse_sentences(res, each_url)
        #         # time.sleep(2)
        #
        # # for index, words in enumerate(self.trans_words) :
        # #     self.results.append([words[0], self.src_sentences[index][0], self.tar_sentences[index][0]])
        # self.save_astext(word, target_language)
        # self.read_txt(word)

    def create_url_with_args(self, base_url, from_, to_, words) :
        if from_ != 'all' :
            return f'{base_url}/{from_}-{to_}/{words}'
        else :
            for elements in self.language_dict :
                all_urls = f'{base_url}/{from_}-{elements}/{words}'
                self.urls.append(all_urls)

    # def run_args(self):
    #     base_url = f'https://context.reverso.net/translation'
    #     from_ = sys.argv[1]
    #     to_ = sys.argv[2]
    #     words = sys.argv[3]
    #     base_number = input('Type the number of your language:\n')
    #     base_language = self.language_dict.get(base_number)
    #     tar_number = input('Type the number of a language you want to translate to or "0" to '
    #                        'translate to all languages:\n')
    #     word = input('Type the word you want to translate:\n')
    #     final_url = self.get_finalurl(base_url, tar_number, base_number, base_language, word)

    # for i in range(2):
    #     html = self.load_response()
    #     self.parse_words(html)
    #     self.parse_sentences(html)


if __name__ == '__main__' :
    scraper = Basescraper()
    scraper.run()
