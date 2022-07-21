# class Sentence:
#     def __init__(self, sentence) -> None:
#         self.sentence = sentence
#         self.words = self.sentence.strip().split(' ')
#         self.length = len(self.words)
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < self.length:
#             cur_word = self.words[self.index]
#             self.index += 1
#             return cur_word 
#         else:
#             raise StopIteration
        

# words = Sentence('This is a sentence')
# for word in words: 
#     print(word)



def sentence(sent):
    words = sent.strip().split(' ')
    for word in words:
        yield word

words = sentence('')
for word in words: 
    print(word)
