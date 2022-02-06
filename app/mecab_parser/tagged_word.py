from dataclasses import dataclass


@dataclass
class TaggedWord:
    input: str


@dataclass
class TaggedWordByMecabIpadicNeologd(TaggedWord):
    """mecab-ipadic-neologd によってタグ付けされた単語

    Attributes
    ----------
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
    """
    part_of_speech: str
    part_of_speech_subtyping: str
    conjugation_type: str
    conjugated_form: str
    original_form: str
    reading: str
    annotations: str
