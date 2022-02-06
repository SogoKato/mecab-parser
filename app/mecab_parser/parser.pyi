from typing import Literal, overload

from .tagged_word import TaggedWordByMecabIpadicNeologd


class _ParserWithMecabIpadicNeologd:
    """
    Parameters
    ----------
    text: str
        Specify a text to parse.

    Returns
    -------
    tagged_words: list[TaggedWordByMecabIpadicNeologd]
    """
    def __init__(self, dic: str) -> None: ...
    def __call__(self, text: str) -> list[TaggedWordByMecabIpadicNeologd]: ...


class MecabParserFactory:
    """Parser インスタンスを作成します
    
    Parser インスタンスは `__call__` で呼び出すことができます
    """
    @staticmethod
    # @overload  # MEMO: If additional dic added, use @overload to define interface.
    def create(
        dic: Literal["mecab-ipadic-neologd"],
    ) -> _ParserWithMecabIpadicNeologd: ...
