# News Classification System

The News Classification System is designed to fetch news articles from various RSS feeds, parse them, remove duplicates, and classify them into different categories using a Celery worker for asynchronous processing. The system utilizes PostgreSQL as the database to store news articles and their categories.

## Project Structure

```plaintext
/News-Classification
│
├── main.py                  # Main script for fetching, parsing, and processing news articles
├── celery_worker.py         # Celery worker for asynchronously processing articles
├── database.py              # Database schema and methods for interacting with the database
├── nlp.py                   # NLP module for text preprocessing and article categorization
├── logger.py                # Logging configuration and utility module
├── requirements.txt         # Required Python packages for the project
└── README.md                # Project documentation
```
## Components

1. **main.py:**
   - **Responsibility:**
     - Fetch news articles from multiple RSS feeds.
     - Parse the articles and store them in the database.
     - Remove duplicate articles based on title and source URL.
   - **Dependencies:**
     - `feedparser`: Library for parsing RSS feeds.
     - `datetime`: Module for handling date and time.
     - `urllib.parse`: Module for parsing URLs.
     - `hashlib`: Library for secure hashing.
     - `celery_worker.process_article`: Asynchronous task for processing articles.
     - `database.NewsDatabase`: Interface for interacting with the database.
     - `logger`: Logging module for tracking events and errors.

2. **database.py:**
   - **Responsibility:**
     - Define the SQLAlchemy model for the `NewsArticle` table.
     - Provide a session interface (`NewsDatabase`) for interacting with the database.
   - **Dependencies:**
     - `sqlalchemy`: SQL toolkit and Object-Relational Mapping (ORM) library.
     - `logger`: Logging module.

3. **celery_worker.py:**
   - **Responsibility:**
     - Define a Celery task (`process_article`) for classifying articles asynchronously.
     - Use Natural Language Processing (NLP) techniques for basic article classification.
   - **Dependencies:**
     - `celery`: Distributed task queue for handling asynchronous tasks.
     - `database.NewsArticle`: Model for the `news_articles` table.
     - `nltk`: Natural Language Toolkit for NLP operations.
    
4. **nlp.py:**
   - **Components:**
     - `preprocess_text(text)`: Tokenizes and preprocesses the given text by removing stop words and stemming.
     - `categorize_article(article)`: Categorizes news articles based on a basic positive/negative classification. Modify for advanced NLP-based categorization.
   - **Dependencies:**
     - `nltk.tokenize`: Tokenization library.
     - `nltk.corpus.stopwords`: Stopwords corpus from NLTK.
     - `nltk.stem.PorterStemmer`: Porter Stemmer for word stemming.
     - `logger`: Logging module.
    
5. **logger.py:**
   - **Responsibility:**
     - Configures and provides a logging instance for the project.
   - **Dependencies:**
     - `logging`: Python's built-in logging module.
       
6. **output.csv:**
   - CSV file containing the output of the processed news articles, including fields such as `id`, `title`, `content`, `pub_date`, `source_url`, and `category`.

## Design Choices

1. **Asynchronous Processing:**
   - Utilizes Celery for asynchronous processing to handle article classification in the background.
   - Enables scalability and responsiveness by offloading time-consuming tasks.

2. **Database Design:**
   - PostgreSQL is chosen for its relational database capabilities.
   - `NewsArticle` model includes fields for article details (title, content, pub_date, source_url), an `id` as the primary key, and a `category` for classification.

3. **NLP-based Classification:**
   - Uses a simple NLP-based classification approach in `celery_worker.py` to categorize articles.
   - Positive keyword presence in the article's content determines a "Positive/Uplifting" category; otherwise, articles fall into the "Others" category.

4. **Hash-based Duplicate Removal:**
   - Removes duplicate articles based on the SHA-256 hash of the combination of title and source URL.
   - Ensures uniqueness while avoiding redundant storage of articles.

## Running the System

1. **Setting up PostgreSQL:**
   - Ensure a PostgreSQL database is available and configure the connection in `database.py`.

2. **Running Celery Worker:**
   - Execute `celery -A celery_worker worker --loglevel=info` in the terminal to start the Celery worker.

3. **Running the Main Script:**
   - Execute `python main.py` to fetch, parse, store, and classify news articles.

## Potential Improvements

1. **Advanced NLP Techniques:**
   - Enhance the article classification logic using more sophisticated NLP techniques.

2. **Dynamic Category System:**
   - Implement a dynamic category system with configurable rules for categorization.

3. **User Interface:**
   - Develop a user interface for interaction and visualization of classified news articles.

4. **Error Handling and Logging:**
   - Implement comprehensive error handling and logging for better system monitoring.

## Output

The system generates an `output.csv` file containing the processed news articles with details such as `id`, `title`, `content`, `pub_date`, `source_url`, and `category`.

### Exporting Database to CSV

To export the contents of the `news_articles` table to a CSV file, you can use the following PostgreSQL `COPY` command:
- EXECUTE 'COPY (SELECT * FROM news_articles) TO 'D:/path/output.csv' WITH CSV HEADER;' in psql. 


## Conclusion

The News Classification System provides a foundation for efficiently processing and categorizing news articles. It can be extended and customized based on specific requirements and can serve as a starting point for building more advanced news classification systems.
