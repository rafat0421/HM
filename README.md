# REST API

REST Client: client.py

REST Service: server.py

The server will start using the default IP and Port (127.0.0.1:5000).

To make a API call
Use your browser or any API testing tool (e.g. Postman)
The url should look like this - http://127.0.0.1:5000/price?article=1&color=1&week=1
Or open the client.py and run the get_article_price() method with three integer type parameter value (article-id,color-id,week).

Database: A SQLite database(article.db) has been used as the data source.

The error.py file contains a list of errors with customized message. This is used for error-handling.
 
