from .verb import Verb
from .er_regular_verb import ERRegularVerb
from .ir_regular_verb import IRRegularVerb
from .ar_regular_verb import ARRegularVerb

class RegularVerb(Verb):
    def __init__(self, word, translation):
        super().__init__(word, translation)

    @classmethod
    def factory(word, translation):
        if word.endswith('ar'):
            return ARRegularVerb(word, translation)
        elif word.endswith('er'):
            return ERRegularVerb(word, translation)
        elif word.endswith('ir'):
            return IRRegularVerb(word, translation)
        else:
            return None