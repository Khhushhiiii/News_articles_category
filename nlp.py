from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    words = word_tokenize(text)
    filtered_words = [ps.stem(word.lower()) for word in words if word.isalpha() and word.lower() not in stop_words]
    return filtered_words

def categorize_article(article):
   
    terrorism_keywords = ['terrorism', 'protest', 'political unrest', 'riot']
    positive_keywords = ['positive', 'uplifting', 'inspiring']
    natural_disaster_keywords = ['natural disaster', 'earthquake', 'flood', 'hurricane']

 
    processed_content = preprocess_text(article['content'])

    # Check for category-specific keywords
    if any(keyword in processed_content for keyword in terrorism_keywords):
        return 'Terrorism/Protest/Political Unrest/Riot'
    elif any(keyword in processed_content for keyword in positive_keywords):
        return 'Positive/Uplifting'
    elif any(keyword in processed_content for keyword in natural_disaster_keywords):
        return 'Natural Disasters'
    else:
        return 'Others'
