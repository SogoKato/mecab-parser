from abc import ABCMeta, abstractmethod
from typing import Literal

from flask import current_app
import MeCab

from .tagged_word import (
    TaggedWord, TaggedWordByMecabIpadicNeologd,
)


class MecabParserFactory:
    @staticmethod
    def create(dic: Literal["mecab-ipadic-neologd"]):
        if dic == "mecab-ipadic-neologd":
            return _ParserWithMecabIpadicNeologd(dic)


class _MecabParser(metaclass=ABCMeta):
    """
    Wrapper class for parsing with Mecab.

    Attributes
    ----------
    mecab : MeCab.Tagger
    """

    @abstractmethod
    def __init__(self, dic: str):
        """
        Parameters
        ----------
        dic: str
            Specify a dictionary name for parsing.
        """
        self.dic = dic
        self.mecab = MeCab.Tagger(dic)

    @abstractmethod
    def __call__(self, text: str) -> list[TaggedWord]:
        """
        Parameters
        ----------
        text: str
            Specify a text to parse.
        """

    def _parse(self, text: str) -> list[tuple[str, list[str]]]:
        """
        Parameters
        ----------
        text: str
            Specify a text to parse.

        Returns
        -------
        outputs: list[tuple[str, list[str]]]
        """
        output: str = self.mecab.parse(text)
        outputs_tmp0 = [row for row in output.split("\n") if row and not row == "EOS"]
        outputs_tmp1 = [o.split('\t') for o in outputs_tmp0]
        outputs_formatted = [(o[0], o[1].split(",")) for o in outputs_tmp1]
        current_app.logger.debug(outputs_formatted)
        return outputs_formatted


class _ParserWithMecabIpadicNeologd(_MecabParser):

    def __init__(self, dic: str):
        super().__init__(dic)

    def __call__(self, text: str) -> list[TaggedWordByMecabIpadicNeologd]:
        outputs = self._parse(text)
        return [
            TaggedWordByMecabIpadicNeologd(
                input=o[0],
                part_of_speech=o[1][0],
                part_of_speech_subtyping=o[1][1],
                conjugation_type=o[1][2],
                conjugated_form=o[1][3],
                original_form=o[1][4],
                reading=o[1][5],
                annotations=o[1][6],
            )
            for o in outputs
        ]
