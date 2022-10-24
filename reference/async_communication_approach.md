We can implement url shortener with microservice async-communication approach.
For example, a monolithic service can be divided in two separate parts:
- url shortener, that will create a short version of the long url and save a pair short-long url in the persistence storage ([MongoDB](https://www.mongodb.com/))
- url redirector, that will redirect the user by short url, stored in [Redis](https://redis.io/) in order to fast url read

It's clear that in the case of creating a new short url we need to put it in Redis through the url redirector. 
Thus communication between services will be built in async way via [RabbitMQ](https://www.rabbitmq.com/)

