# Document Search and Management System

## Project Description
The Document Search and Management System is a web application designed to efficiently store, retrieve, and manage documents. Leveraging modern technologies like Flask, Redis, and Docker, this system provides a user-friendly interface for document management and ensures high performance and scalability.

## Key Features
1. **Store Documents**: Users can enter a title and content to save their documents.
2. **Search Functionality**: Users can search for documents using specific queries, and the app will return relevant results.
3. **Health Check Endpoint**: A special feature that checks if the API is running smoothly and responds with a message.

## Technologies Used
- **Flask**: For building the web application.
- **HTML/CSS**: For the front-end user interface.
- **Docker**: For packaging the application into a container, making it easy to deploy.
- **Redis**: In-memory database for caching.

## Installation Instructions
To run the Document Search and Management System locally, follow these steps:

### Steps to Run the Code
- Clone the repository
- install the packages in requirement.txt 
- **pip install -r requirements.txt**
- Set up redis
- **pip install redis**
- **pip install flask**
- **docker run --name redis -d -p 6379:6379 redis**
- Make sure redis is running
- Run the flask application 
- **flask run**
- Run the docker file
- **docker build -t flask-trademarkia .**
- **docker run -p 5000:5000 flask-trademarkia**

## Project Outcome

The Document Search Application successfully achieved the following outcomes:

### Document Storage
- Implemented a robust document storage feature that allows users to add, store, and manage documents with titles and content.
- Ensured documents are stored persistently in Redis, providing data durability and reliability.

### Search Functionality
- Developed an efficient search mechanism that retrieves relevant documents based on user queries.
- Utilized similarity scoring to rank search results, offering users the most relevant information.

### Health Check Endpoint
- Created a health check endpoint (`/health`) to monitor the API's status, facilitating proactive maintenance and ensuring the system remains operational.

### Caching Mechanism
- Integrated caching strategies using Redis to enhance response times for frequently accessed data, resulting in faster retrieval and an improved user experience.
- Reduced the load on the database, optimizing performance and making the application more responsive.

### API Rate Limiting
- Implemented a rate limiting feature, restricting users to a maximum of five requests to prevent abuse and ensure fair API usage.
- Enhanced security and maintained system integrity through this functionality.

### User Analytics
- Incorporated user request tracking to monitor API usage and user behavior.
- Collected insights that can be utilized for further enhancements and improvements based on user interaction patterns.


This project demonstrates a solid implementation of document storage, search functionality, and performance optimization techniques, making it a valuable tool for managing and retrieving documents efficiently.


