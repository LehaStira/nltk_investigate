import nltk

word_data = "The best performance can bring in sky high success."
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)
print(type(nltk_tokens))

print(list(nltk.bigrams(nltk_tokens)))

example_list = ['Hello', 'I', 'Love', 'You', 'son', 'of', 'a', 'bitch']

list_token = nltk.word_tokenize(example_list)

print(list(nltk.bigrams(example_list)))
print(list(nltk.bigrams(list_token)))