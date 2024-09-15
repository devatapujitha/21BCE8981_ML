**Project Description** : Document Search Application
This project is a Document Search Application built with Flask. It allows users to store and search for documents efficiently.
This project is a web scraper and caching-enabled Flask application that scrapes document information using search strategy and the concepts of TF-IDF to retrieve the document by using search. It provides a user-friendly API to access the data. The application utilizes caching strategies to enhance performance and ensure efficient handling of web requests.

**Key Features**:
1.Store Documents: Users can enter a title and content to save their documents.
2.Search Functionality: Users can search for documents using specific queries, and the app will return relevant results.
3.Health Check Endpoint: A special feature that checks if the API is running smoothly and responds with a message.

**Technologies Used**:
Flask: For building the web application.
HTML/CSS: For the front-end user interface.
Docker: For packaging the application into a container, making it easy to deploy

**Caching Strategy**:
To enhance the performance of the Document Search Application, we implemented a caching mechanism to ensure faster retrieval of search results. For this scenario, I opted for Redis(which is an in-memory database) as my caching solution. 

**Steps to Run the code**:
1.Clone the repository
2.install the packages in requirement.txt
-->pip install -r requirements.txt
3.Set up redis
-->docker run --name redis -d -p 6379:6379 redis
4.Run the flask application 
-->flask run
5.Run the docker file
-->docker build -t flask-trademarkia .
docker run -p 5000:5000 flask-trademarkia


  
