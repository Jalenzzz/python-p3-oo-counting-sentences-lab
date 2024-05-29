#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return
        self._value = new_value

    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False
        
    def count_sentences(self):
        sentences = self.value.split('.')
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)
        

s = MyString(value="This is a sentence. This is another sentence.")
print(s.count_sentences())
