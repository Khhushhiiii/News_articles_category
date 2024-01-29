from celery import Celery
from database import NewsArticle, Session
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Celery('news_processing', broker='pyamqp://guest:guest@localhost//')

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    words = word_tokenize(text)
    filtered_words = [ps.stem(word.lower()) for word in words if word.isalpha() and word.lower() not in stop_words]
    return filtered_words

def categorize_article(article):
   
    return 'Positive/Uplifting' if 'positive_keyword' in preprocess_text(article['content']) else 'Others'

@app.task
def process_article(article_id):
    session = Session()  # Create a new session for each task
    article = session.query(NewsArticle).filter_by(id=article_id).first()
    if article:
        category = categorize_article(article)
        article.category = category
        session.commit()


# celery -A celery_worker worker --loglevel=info
