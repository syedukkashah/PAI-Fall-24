import nltk, re
from nltk.tokenize import word_tokenize, sent_tokenize #for tokenization

from nltk.stem import PorterStemmer# for stemming

from nltk.stem import WordNetLemmatizer #for lemmatization
from nltk.corpus import wordnet, stopwords

nltk.download('omw-1.4')

text = "this is a sample sentence. Tokenize me. please."
words= word_tokenize(text) #all words tokenized
sentence = sent_tokenize(text) #sentence seperated after the period
print(words)
print(sentence)

#Removing last part or letters of a word is stemming
stemmer = PorterStemmer()
words = ["jumping", "jumps", "jumped", "running", "runner", "easily"]
stemmed_words = [stemmer.stem(word) for word in words]
print("original: ", words)
print(stemmed_words)

#converting a word to it's meaningful base form(called lemma) considering it's context is called lemmatization

lemmatizer = WordNetLemmatizer()
words = ["jumping", "jumps", "jumped", "running", "runner", "easily"]
lemmatize_words_n = [lemmatizer.lemmatize(word) for word in words]
lemmatize_words_v = [lemmatizer.lemmatize(word, pos = "v") for word in words] #applying lemmatization specifying the part of speech as verb(POS = 'v')
print(words)
print("lemmatized words as noun: ",lemmatize_words_v)
print("lemmatized words as verb: ",lemmatize_words_n)

para = "my name is ukkashah and i love to listen to music and watch movies to relax"
sentences = nltk.sent_tokenize(para)
for i in range(len(sentences)):
    words= nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = ' '.join(words)

print(sentences)

para = "my name is ukkashah and i love to listen to music and watch movies to relax"
sentence = nltk.sent_tokenize(para)
lemmatizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = ' '.join(words)

print(sentences)
para = "Pakistan was established in 1947"
ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences= nltk.sent_tokenize(para)
corpus = []
for i in range(len(sentences)):
    review = re.sub()
