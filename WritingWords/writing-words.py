'''
Fox Ciel wants to type a word on her old cell phone. The cell phone
has only one button. The letter A is typed by tapping the button once,
B by tapping it twice in a row, and so on, in alphabetical
order. Thus, the last letter Z is typed by tapping the button 26 times
without a pause.



You are given a String word. Compute and return the answer to the
following question: How many times will Ciel tap the button while
typing this word?
'''

class WritingWords:
    def write(self, word):
        lett = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return sum([lett.index(k) for k in word])
