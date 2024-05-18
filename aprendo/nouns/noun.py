from ..abstract.word import Word

class Noun(Word):
    def __init__(self, word : str, translation : str):
        self.word = word
        self.translation = translation

    def __repr__(self):
        return f"{self.word} - {self.translation}"
    
    def get_word(self):
        return self.word
    
    def get_translation(self):
        return self.translation
    
    def get_example(self):
        pass