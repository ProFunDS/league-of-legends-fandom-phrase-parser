from typing import List, Literal, NamedTuple, Tuple

import eel

from bs4 import BeautifulSoup

from fake_headers import Headers

from requests import get


class Phrase(NamedTuple):
    text: str
    src: str

def get_eng_phrases(buttons) -> List[Phrase]:
    phrases = []

    for button in buttons:
        src = button.find('audio')['src']
        src = src.split('/revision')[0]
        try:
            text = button.find_next_sibling('i').text.strip()
        except AttributeError:
            text = 'Не получилось найти текст :C'
        phrases.append(Phrase(text, src))

    return phrases

def get_rus_phrases(buttons) -> List[Phrase]:
    phrases = []

    for button in buttons:
        src = button.find('audio')['src']
        try:
            text = button.parent.text.split('.ogg')[-1].strip()
        except AttributeError:
            text = 'Не получилось найти текст :C'

        phrases.append(Phrase(text, src))

    return phrases
    

def get_phrases(url: str) -> Tuple[Literal['ru', 'en'], List[Phrase]]:
    
    if 'https://' not in url:
        url = 'https://' + url
    
    headers = Headers().generate()

    result = get(url, headers=headers).text

    soup = BeautifulSoup(result, 'lxml')
    buttons = soup.find_all(class_='audio-button')

    if '/ru/' in url:
        return 'ru', get_rus_phrases(buttons)
    else:
        return 'en', get_eng_phrases(buttons)


def start() -> None:
    eel.init('')

    @eel.expose
    def parse(url: str):
        lang, phrases = get_phrases(url)
        eel.render_phrases(lang, phrases)

    eel.start('index.html', mode='chrome', size=(900, 900))

def main() -> None:
    start()

if __name__ == '__main__':
    main()