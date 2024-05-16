from .regular_verb import RegularVerb

class ARRegularVerb(RegularVerb):
    def __init__(self, word, translation):
        super().__init__(word, translation)
        self.ending = 'ar'

    def get_conjugation(self, pronoun):
        if pronoun == 'yo':
            return self.word + 'o'
        elif pronoun == 'tu':
            return self.word + 'as'
        elif pronoun == 'el':
            return self.word + 'a'
        elif pronoun == 'nosotros':
            return self.word + 'amos'
        elif pronoun == 'vosotros':
            return self.word + 'ais'
        elif pronoun == 'ellos':
            return self.word + 'an'
        else:
            return 'Unknown pronoun'