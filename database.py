from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)
    pub_date = Column(DateTime)
    source_url = Column(String)
    category = Column(String,default='Others')

# Replace 'your_username', 'your_password', and 'your_database' with your actual PostgreSQL credentials and database name
engine = create_engine('postgresql://postgres:khushidb@localhost/news?client_encoding=utf8')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class NewsDatabase:
    def __init__(self):
        self.session = Session()

    def insert_article(self, article):
        article_id = article['id']
        existing_article = self.session.query(NewsArticle).filter_by(id=article_id).first()
        if not existing_article:
            db_article = NewsArticle(
                id=article_id,
                title=article['title'],
                content=article['content'],
                pub_date=article['pub_date'],
                source_url=article['source_url']
            )
            self.session.add(db_article)
            self.session.commit()
