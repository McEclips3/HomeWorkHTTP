from yandex import YandexDisk
from heroes import superheroes


TOKEN = ''

if __name__ == '__main__':
    print(superheroes(['Thanos', 'Hulk', 'Captain America']))

    ya = YandexDisk(token=TOKEN)
    ya.upload_file('test/anime.txt', 'anime.txt')
