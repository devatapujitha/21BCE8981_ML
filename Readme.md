# h1 Project Description: Document Search Application
This project is a Document Search Application built with Flask. It allows users to store and search for documents efficiently.
This project is a web scraper and caching-enabled Flask application that scrapes document information using search strategy and the concepts of TF-IDF to retrieve the document by using search. It provides a user-friendly API to access the data. The application utilizes caching strategies to enhance performance and ensure efficient handling of web requests.

---
 
# h3 Key Features:
1.Store Documents: Users can enter a title and content to save their documents.
2.Search Functionality: Users can search for documents using specific queries, and the app will return relevant results.
3.Health Check Endpoint: A special feature that checks if the API is running smoothly and responds with a message.

# h3 Technologies Used:
Flask: For building the web application.
HTML/CSS: For the front-end user interface.
Docker: For packaging the application into a container, making it easy to deploy
Redis: In-memory Database.

# h3 Caching Strategy:
To enhance the performance of the Document Search Application, we implemented a caching mechanism to ensure faster retrieval of search results. For this scenario, I opted for Redis(which is an in-memory database) as my caching solution. 

# h3 Steps to Run the code:
#Lists
- Clone the repository
- install the packages in requirement.txt 
-->pip install -r requirements.txt
- Set up redis
-->docker run --name redis -d -p 6379:6379 redis
  Make sure redis is running
- Run the flask application 
-->flask run
-Run the docker file
-->docker build -t flask-trademarkia .
docker run -p 5000:5000 flask-trademarkia

# Document Search and Management System

## Project Description
The Document Search and Management System is a web application designed to efficiently store, retrieve, and manage documents. Leveraging modern technologies like Flask, Redis, and Docker, this system provides a user-friendly interface for document management and ensures high performance and scalability.

## Features

### Document Storage
- Successfully implemented a robust document storage feature that allows users to add, store, and manage documents with titles and content.
- Documents are stored persistently in Redis, ensuring data durability and reliability.

### Search Functionality
- Developed an efficient search mechanism that retrieves relevant documents based on user queries.
- The search feature employs similarity scoring to rank results, providing users with the most relevant information.

### Health Check Endpoint
- Implemented a health check endpoint (`/health`) to monitor the status of the API, allowing for proactive maintenance and ensuring the system is operational.

### Caching Mechanism
- Integrated caching strategies using Redis to improve response times for frequently accessed data, resulting in faster retrieval and enhanced user experience.
- The caching approach reduces the load on the database and optimizes performance, making the application more responsive.

### API Rate Limiting
- Implemented a rate limiting feature that restricts users to a maximum of five requests to prevent abuse and ensure fair usage of the API.
- This functionality enhances security and maintains system integrity.

### User Analytics
- Incorporated user request tracking, enabling the system to monitor API usage and user behavior.
- This information can be utilized for further enhancements and improvements based on user interaction patterns.



  
