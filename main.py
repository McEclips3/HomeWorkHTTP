from yandex import YandexDisk
from heroes import superheroes
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'tokens.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
print(TOKEN)

if __name__ == '__main__':
    print(superheroes(['Thanos', 'Hulk', 'Captain America']))

    ya = YandexDisk(token=TOKEN)
    ya.upload_file('test/anime.txt', 'anime.txt')
