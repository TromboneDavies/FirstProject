import nltk
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

file = open("conservative.txt", encoding = "utf-8")
posts = file.read().replace("\n", " ").split("-----")
file.close()

words = []
documents = []
stemmer = nltk.PorterStemmer()

for post in posts:
    documents.append([[stemmer.stem(w) for w in word_tokenize(post) if not w in
    stopwords.words('english') and w.isalnum()], "Con"])
    for word in word_tokenize(post):
        words.append(stemmer.stem(word))

file = open("liberal.txt", encoding = "utf-8")
posts = file.read().replace("\n", " ").split("-----")
file.close()

for post in posts:
    documents.append([[stemmer.stem(w) for w in word_tokenize(post) if not w in
    stopwords.words('english') and w.isalnum()], "Lib"])
    for word in word_tokenize(post):
        words.append(stemmer.stem(word))

all_words = nltk.FreqDist(w.lower() for w in words)

word_features = list(all_words.keys())[:20]

#i = 0
#for word in all_words.keys():
    #print(word)
    #if i == 20:
        ##break
    #i = i + 1
    #word_features.append(word)

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
classifier = nltk.NaiveBayesClassifier.train(featuresets)

classifier.show_most_informative_features(5)
