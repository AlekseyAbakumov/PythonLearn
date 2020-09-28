from bs4 import BeautifulSoup
import unittest


def get_imgs_count(body):
    count = 0
    tags = body('img')

    for tag in tags:
        if 'width' in tag.attrs:
            if int(tag['width']) >= 200:
                count += 1
    return count


def get_headers_count(body):
    count = 0
    tags = {}
    for i in range(1, 7):
        tags['h{}'.format(i)] = body('h{}'.format(i))

    for head in tags.keys():
        for tag in tags[head]:
            for child in list(tag.children):
                if str(child.string)[0] in ['E', 'T', 'C']:
                    count += 1

    return count


def get_link_count(links_list):
    max_len = 1

    for i in range(len(links_list)):
        if str(links_list[i])[1] == 'a':
            max_len += 1
        else:
            break

    return max_len

def get_links_len(body):
    link_len = 0
    tags = body('a')
    for tag in tags:
        tmp_len = get_link_count(tag.find_next_siblings())
        if tmp_len > link_len:
            link_len = tmp_len

    return link_len


def get_lists_count(body):
    count = 0
    tags = body.find_all(['ul', 'ol'])

    for tag in tags:
        if not tag.find_parents(['ul', 'ol']):
            count += 1

    return count


def parse(path_to_file):
    with open(path_to_file, encoding='UTF-8') as data:
        soup = BeautifulSoup(data, 'lxml')
    body = soup.find(id='bodyContent')
    imgs = get_imgs_count(body)  # Количество картинок (img) с шириной (width) не меньше 200
    headers = get_headers_count(body)  # Количество заголовков, первая буква текста внутри которого: E, T или C
    linkslen = get_links_len(body)  # Длина максимальной последовательности ссылок, между которыми нет других тегов
    lists = get_lists_count(body)  # Количество списков, не вложенных в другие списки

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()