# Mecab-Parser

You can use part-of-speech and morphological analyzing API server powered by [Mecab](https://taku910.github.io/mecab/) and [mecab-ipadic-NEologd dictionary](https://github.com/neologd/mecab-ipadic-neologd) on a single container.

Mecab および mecab-ipadic-NEologd 辞書を搭載した品詞・形態素解析のAPIサーバーを単一のコンテナで使用することができます。

## Prerequisite

* docker or other container engine installed

## Try it out

```sh
docker run -p "8080:8080" --rm noroch/mecab-parser
```

In the another terminal:

```sh
curl localhost:8080/parse -XPOST -H "Content-Type: application/json" \
  -d '{"texts": ["私はきれいなタヌキです", "あなたはドラえもんに似ているね", "彼はおいしい草を1日3回食べます", "彼女はたまに鹿児島に行きます"]}' | jq
```

The response is like below (truncated):

```json
{
  "ok": true,
  "results": [
    [
      {
        "annotations": "代表表記:私/わたし 漢字読み:訓 カテゴリ:人",
        "conjugated_form": "*",
        "conjugation_type": "*",
        "input": "私",
        "original_form": "私",
        "part_of_speech": "名詞",
        "part_of_speech_subtyping": "普通名詞",
        "reading": "わたし"
      }
    ]
  ]
}
```

Response format of results[]:

```
input: str
    テキスト中の単語
part_of_speech: str
    品詞（名詞、助詞など）
part_of_speech_subtyping: str
    品詞（普通名詞、副助詞など）
conjugation_type: str
    活用型
conjugated_form: str
    活用形
original_form: str
    原形
reading: str
    読み
annotations: str
    注釈（代表表記、反義、カテゴリ、ドメインなど）
```

See also: https://hub.docker.com/r/noroch/mecab-parser

## Run development server

```sh
docker-compose up -d --build
```

## Acknowledgments

Many thanks to people contributing to Mecab and mecab-ipadic-NEologd project.
