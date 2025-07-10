import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('omw-1.4')
nltk.download('punkt_tab')


from nltk.tokenize import word_tokenize
text1= "Tokenization helps break text into smaller pieces like words."
tokens1 = word_tokenize(text1)
print(tokens1)
text2= "Natural Language Processing is a key part of AI and data science."
tokens2 = word_tokenize(text2)
print(tokens2)

#Print each token
print("Tokens:")
for token in tokens2:
    print (token)