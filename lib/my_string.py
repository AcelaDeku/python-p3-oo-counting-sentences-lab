# lib/my_string.py

import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        
        modified_value = re.sub(r'[.!?]+', '.', self.value)
        
        sentences = [sentence for sentence in modified_value.split('.') if sentence.strip()]
        return len(sentences)


if __name__ == "__main__":
    string = MyString("This is a string! It has three sentences. Right?")
    print(string.is_sentence())         # Output: False
    print(string.is_question())         # Output: True
    print(string.is_exclamation())      # Output: False
    print(string.count_sentences())     # Output: 3
