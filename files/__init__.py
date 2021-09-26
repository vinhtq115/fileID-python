import io
from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def get_score(self, f: io.BufferedReader):
        """
        Read file and determine its score.
        :param f: File handler
        :return: Score
        """
        pass


# File-types
from files.FLAC import FLAC
from files.IPA import IPA
from files.PE import PE
from files.WAVE import WAVE
from files.ZIP import ZIP

FILETYPES = [FLAC, IPA, PE, WAVE, ZIP]
