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

    def initial_questionairre(self) :
        """Initial questions to get the base, target, list_of_languages and the word"""
        target_languages = list(self.language_dict.values())
        print("Hello, you're welcome to the translator. Translator supports: ")
        [print(key, value) for key, value in self.language_dict.items()]
        base_number = input('Type the number of your language:\n')
        base_language = self.language_dict.get(base_number)
        tar_number = input('Type the number of a language you want to translate to or "0" to '
                           'translate to all languages:\n')
        word = input('Type the word you want to translate:\n')
        target_languages.remove(base_language)
        return [base_language, base_number, target_languages, tar_number, word]

    def fetch(self, url) :
        """Get the url"""
        # print(f'HTTP GET REQUESTS TO URL: {url}', end="")
        s = requests.Session()
        res = s.get(url, headers=self.headers)
        # print(f' | STATUS CODE: {res.status_code}')
        if res.status_code == 404 :
            print(f'Sorry, unable to find {url.split("/")[-1]}')
            sys.exit()
        elif res.status_code != 200:
            print('Something wrong with your internet connection')
        else :
            return res

    def save_response(self, html) :
        """Initial saving the response to not hammer the website"""
        with open('reverso.html', 'w', encoding='utf-8') as base_html :
            base_html.write(html.text)

    def load_response(self) :
        """Loading the saved response"""
        html = ''
        with open('reverso.html', 'r', encoding='utf-8') as base_html :
            for line in base_html :
                html += line
        return html

    def save_astext(self, word, target_language) :

        """Saving the output in a text file"""
        with open(f'{word}.txt', 'w', encoding='utf-8') as f :
            # f.write(str(self.results))
            for index, words in enumerate(self.trans_words) :
                if len(self.urls) > 1 :
                    print(f'{target_language[index]} Translations:\n'
                          f'{words[0]}\n\n'
                          f'{target_language[index]} Example:\n'
                          f'{self.src_sentences[index][0]}:\n'
                          f'{self.tar_sentences[index][0]}\n', file=f)
                else :

                    print(f'{target_language} Translations:', file=f)
                    print(*words[:5], sep='\n', end='\n\n', file=f)
                    print(f'{target_language} Example:', file=f)
                    for i in range(5) :
                        print(self.src_sentences[index][i], file=f)
                        print(self.tar_sentences[index][i], file=f)
                        print(file=f)

    def read_txt(self, word) :
        """reading from the text file"""
        if os.access(f'{word}.txt', os.R_OK) :
            with open(f'{word}.txt', encoding='utf-8') as word_tr :
                print(word_tr.read())
        else :
            print("The word is not translated yet.")

    def parse_words(self, html) :
        """Parsing words"""
        content = BeautifulSoup(html.text, 'html.parser')
        try :
            translation_content = content.findAll('div', {'id' : 'translations-content'})
            for trans in translation_content :
                words = trans.text.split()
                self.trans_words.append(words)
        except :
            print("Word not found")

    def parse_sentences(self, html, each_url) :
        """Parsing sentences"""
        target_language = each_url.split('/')[-2].split('-')[-1]
        base_language = each_url.split('/')[-2].split('-')[0]

        content = BeautifulSoup(html.content, 'html.parser')
        # content = BeautifulSoup(html, 'html.parser')

        # print(content.prettify())
        sentences_content = content.findAll('div', {'class' : 'example'})
        new_src_list = []
        new_tar_list = []
        for each_sentence in sentences_content :
            if 'arabic' in base_language :
                src = each_sentence.find('div', {'class' : 'src rtl arabic'}).text.strip()
            elif 'hebrew' in base_language :
                src = each_sentence.find('div', {'class' : 'src rtl'}).text \
                    .strip() \
                    .replace('[', '') \
                    .replace(']', '')
            else :
                src = each_sentence.find('div', {'class' : 'src ltr'}).text \
                    .strip() \
                    .replace('[', '') \
                    .replace(']', '')
            new_src_list.append(src)

            if 'arabic' in target_language :
                tar = each_sentence.find('div', {'class' : 'trg rtl arabic'}).text.strip()
            elif 'hebrew' in target_language :
                tar = each_sentence.find('div', {'class' : 'trg rtl'}).text \
                    .strip() \
                    .replace('[', '') \
                    .replace(']', '')
            else :
                tar = each_sentence.find('div', {'class' : 'trg ltr'}).text.strip().replace('[', '').replace(']', '')
            new_tar_list.append(tar)
        self.src_sentences.append(new_src_list)
        self.tar_sentences.append(new_tar_list)

    def get_urls(self, url, base_language, target_language, word) :
        """concat to get the urls"""
        languages = f'{base_language}-{target_language}'
        final_url = f'{url}/{languages}/{word}'.lower()
        self.urls.append(final_url)
        return self.urls

    def one_or_all(self, base_language, base_number, target_languages, tar_number, word) :
        """Is it just one url or a list of urls?"""
        if tar_number == '0' or sys.argv[2] == 'all' and tar_number != base_number :
            for each_language in target_languages :
                self.get_urls(self.base_url, base_language, each_language, word)
        else :
            target_language = self.language_dict.get(tar_number)
            self.get_urls(self.base_url, base_language, target_language, word)

    def run(self) :
        """Main parsing and fetching"""
        for each_url in self.urls :
            res = self.fetch(each_url)
            if res.ok :
                # print(res.status_code, 'OK')
                self.parse_words(res)
                self.parse_sentences(res, each_url)
                time.sleep(2)

    def with_args(self) :
        base_language = sys.argv[1].capitalize()
        target_language = sys.argv[2].capitalize()
        word = sys.argv[3]
        target_languages = list(self.language_dict.values())
        target_languages.remove(base_language)
        if base_language not in list(self.language_dict.values()) :
            print(f"Sorry, the program doesn't support {base_language.lower()}")
        elif target_language != 'All' and target_language not in list(self.language_dict.values()) :
            print(f"Sorry, the program doesn't support {target_language.lower()}")
        else :
            if target_language == 'all'.capitalize():
                for each_language in target_languages :
                    self.get_urls(self.base_url, base_language, each_language, word)
            else :
                target_language = sys.argv[2].capitalize()
                self.get_urls(self.base_url, base_language, target_language, word)

            self.run()

            if target_language == 'all'.capitalize() :
                self.save_astext(word, target_languages)
            else :
                self.save_astext(word, target_language)
            self.read_txt(word)


if __name__ == '__main__' :
    scraper = Basescraper()
    """If the scraper is run without args"""
    if len(sys.argv) == 4:
        scraper.with_args()
    else:
        base_language, base_number, target_languages, tar_number, word = scraper.initial_questionairre()
        scraper.one_or_all(base_language, base_number, target_languages, tar_number, word)
        scraper.run()
        scraper.save_astext(word, target_languages)
        scraper.read_txt(word)
