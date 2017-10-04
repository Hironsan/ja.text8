import linecache
import random
import MeCab

random.seed(42)
filename = 'tmp.txt'
save_file = 'ja.text8'
LIMIT_BYTES = 100000000
t = MeCab.Tagger('-Owakati')


def get_byte_num(s):
    return len(s.encode('utf-8'))


if __name__ == '__main__':
    num_lines = sum(1 for line in open(filename))
    indices = list(range(num_lines))
    random.shuffle(indices)

    with open(save_file, 'w') as f:
        count_byte = 0
        for i in indices:
            print('{} bytes'.format(count_byte))
            text = linecache.getline(filename, i)
            text = text.strip()
            text = t.parse(text).strip()
            f.write(text)
            count_byte += get_byte_num(text)
            if count_byte >= LIMIT_BYTES:
                break
