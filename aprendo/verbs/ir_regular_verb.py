from .regular_verb import RegularVerb

class IRRegularVerb(RegularVerb):
    def __init__(self, word, translation):
        super().__init__(word, translation)
        self.ending = 'ir'

    def get_conjugation(self, pronoun):
        if pronoun == 'yo':
            return self.word + 'o'
        elif pronoun == 'tu':
            return self.word + 'es'
        elif pronoun == 'el':
            return self.word + 'e'
        elif pronoun == 'nosotros':
            return self.word + 'imos'
        elif pronoun == 'vosotros':
            return self.word + 'is'
        elif pronoun == 'ellos':
            return self.word + 'en'
        else:
            return 'Unknown pronoun'