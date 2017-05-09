def load_data(filepath):
    with open(filepath) as file_handler:
        return file_handler.read()


def text_replace(text):
    text = text.replace('-\n', '')
    text = text.replace('\n', ' ')
    text = text.replace('"', '')
    text = text.replace("'", "")
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text = text.replace('- ', ' ')
    text = text.replace('\u2018', '')
    text = text.replace('\u2019', '')
    text = text.replace('\u00AB', '')
    text = text.replace('\u00BB', '')

    return text


def get_most_frequent_words(text):
    text = text_replace(text)
    words = {word for word in text.split(' ')}
    words -= {''}
    words_and_count = {}
    top_10_words = {}
    count = 0

    for word in words:
        word += ' '
        words_and_count[word.strip()] = text.count(word)

    for word in reversed(sorted(words_and_count, key=words_and_count.get)):
        top_10_words[word] = words_and_count[word]
        count += 1
        if count == 10:
            break

    return top_10_words


if __name__ == '__main__':
    filepath = input('Введите путь к файлу: ')
    top_10_words = get_most_frequent_words(load_data(filepath))
    for word in top_10_words:
        print('{}: {}\n'.format(word, top_10_words[word]))
