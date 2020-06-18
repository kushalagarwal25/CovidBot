

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords





# Init Objects
tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
# en_stopwords = en_stopwords - {'is','of','are'}
ps = PorterStemmer()




def getClearReview(review):
    
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    #Tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    # stemmed_tokens = [ps.stem(token) for token in new_tokens]
    cleaned_review = ' '.join(new_tokens)
    
    return cleaned_review
    



