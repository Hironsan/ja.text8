# ja.text8
ja.text8 is a small (100MB) text corpus from the web (japanese wikipedia).


You can download ja.text8 corpus from the following link:

* [ja.text8.zip](https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/ja.text8.zip)


# Usage
You can train word2vec by ja.text8.
After downloading ja.text8, run the following code.
It takes about 2 minutes to finish training:

```python
import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
sentences = word2vec.Text8Corpus('ja.text8')
model = word2vec.Word2Vec(sentences, size=200)
```

After the training, you can test the model as follows:

```python
>>> model.most_similar(['日本'])
[('中国', 0.598496675491333),
 ('韓国', 0.5914819240570068),
 ('アメリカ', 0.5286925435066223),
 ('英国', 0.5090063810348511),
 ('台湾', 0.4761126637458801),
 ('米国', 0.45954638719558716),
 ('アメリカ合衆国', 0.45181626081466675),
 ('イギリス', 0.44740626215934753),
 ('ソ連', 0.43657147884368896),
 ('海外', 0.4325913190841675)]
```

Great!

# Requirements
* Python 3.x
* MeCab
* virtualenv

# Make corpus by yourself
You can download ja.text8.
But you can make the corpus by yourself.

Simply run:

```commandline
$ ./setup.sh
```


# License
[CC-BY-SA](https://ja.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License)