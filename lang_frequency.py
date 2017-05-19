import re
from collections import Counter


def load_data(filepath):
    with open(filepath) as file_handler:
        return file_handler.read()


def text_replace(text):
    text = text.replace('-\n', '')
    text = text.replace('\n', ' ')
    r_ex = re.compile(r'[\w]{3,}')
    words = r_ex.findall(text)

    return words


def get_most_frequent_words(text, count):
    words = text_replace(text)
    return Counter(words).most_common(count)


if __name__ == '__main__':
    filepath = input('Введите путь к файлу: ')
    top_words = get_most_frequent_words(load_data(filepath), 10)
    for word, count in top_words:
        print('{}: {}\n'.format(word, count))
