from nltk.tokenize import word_tokenize, sent_tokenize
paragraph = """Hello Welcome, to Syed Ukkashah's NLP Tutorials.
             Follow the entire tutorial! Become an expert."""

print(paragraph)

## Tokenization
## paragraph --> sentences
## sentence --> words
sentences = sent_tokenize(paragraph) #converts to sentences
print(sentences)
words = word_tokenize(paragraph) #converts to words
print(words)

## Stemming -> converts a word to it's root/base word
## Comments of product is a positive review or negative review
## Reviews ----> eating, eat, eaten or going, go, gone

words = ["eating", "eats", "eaten", "writing", "writes", "programming", "programs", "history", "finally", "finalized"]
## PorterStemmer

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

for word in words:
    print(word+"--->"+stemmer.stem(word))

## Major disadvantage of stemming is that stemmed words don't always give a proper meaning
## eaten --> eaten, history --> histori (sometimes they are either unchanged or don't produce valid words)
print(stemmer.stem("congratulations")) #invalid case
print(stemmer.stem("sitting")) #valid case

## Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("going", pos = 'n')) #pos = 'a' (adjective), 'v' (verb), 'n' (noun)

for word in words:
    print(word+"--->"+lemmatizer.lemmatize(word, pos = 'v')) #noun is default so we can change to verb

print(lemmatizer.lemmatize("beautiful", pos = 'a'))

## stopwords
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
stopwords.words('english')
paragraph = """The lion is a wild terrestrial animal called the king of the forest. The lion is a strong animal with a strong body, a big head, 
a majestic mane, and two fierce eyes. Lions are predatory animals and eat only after hunting. 
They have strong claws and sharp teeth, which help them hunt their prey and eat the flesh. 
Lions have yellowish-grey skin colour with smooth hair and an imperious roar which makes a lion unique. 
The footprints of lions are called pug marks. Lions are found chiefly in grasslands, open woodlands, or enclosed in zoos. 
Since they kill their own prey and hunt for food, they have the capacity to run fast."""
words = word_tokenize(paragraph)
#make a list that has all stemmed words that are not present in the stopwords set
words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]

print(words)
stemmed_paragraph = ' '.join(words) #the same sentence, now stemmed and w/o stopwords
print("Stemmed Paragraph: ",stemmed_paragraph)

#now we try with lemmatization
words = word_tokenize(paragraph)
words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
lemmatized_sentence = ' '.join(words)
print("Lemmatized paragraph: ",lemmatized_sentence)

