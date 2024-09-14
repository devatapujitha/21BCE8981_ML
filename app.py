from flask import Flask, request, render_template, jsonify
import redis
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Creating a Flask instance 
app = Flask(__name__)

# Connecting to Redis database
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Adding endpoints
@app.route('/')
def index():
    return render_template('index.html')

# Health endpoint - to check the status of the application
@app.route('/health', methods=['GET'])
def health_check():
    responses = ["API is healthy", "All systems are go", "Server is running smoothly"]
    return jsonify({"message": responses[0]}), 200

# Endpoint to store documents
@app.route('/store', methods=['POST'])
def store_document():
    title = request.form['title']
    content = request.form['content']

    # Store the document in Redis
    redis_client.hset("documents", title, content)

    return render_template('index.html', message="Document stored successfully!")

# Endpoint for search
@app.route('/search', methods=['POST'])
def search_document():
    search_query = request.form['search_query']

    # Retrieve all stored documents from Redis
    all_documents = redis_client.hgetall("documents")

    # Create lists for document contents and titles
    documents = []
    titles = []

    for title, content in all_documents.items():
        content_str = content.decode('utf-8')  # Decode bytes to string
        documents.append(content_str)
        titles.append(title.decode('utf-8'))  # Decode bytes to string

    # Append the search query to the documents list for comparison
    documents.append(search_query)
    titles.append("Search Query")  # Add a title for the search query

    # Create TF-IDF vectorizer and fit_transform the documents
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compute cosine similarities
    cosine_similarities = np.dot(tfidf_matrix[-1], tfidf_matrix[:-1].T).toarray()[0]

    # Sort documents by similarity (score, title, content)
    similar_docs = sorted(zip(cosine_similarities, titles, documents[:-1]), reverse=True)

    # Prepare results for display (title, content, similarity score)
    results = [(title, content, score) for score, title, content in similar_docs if score > 0]

    if not results:
        results = [("No results found", "", 0)]

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
