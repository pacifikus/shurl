## Shurl - URL shortener


### Functional Requirements

1. Given a URL, the service generates a shorter and unique alias of it.
2. When users access a short link, the service redirects them to the original link.
3. Users can optionally pick a custom short link for their URL.
4. Users can view stats about token-URL redirections.

### How to run

Simply run `uvicorn main:app --reload`

### Testing

To run unit tests and integration API tests via [pytest](https://pytest.org/) run
`pytest tests`

#### Load testing

To run load tests via [locust](https://locust.io/) run application, then run `locust -f locustfile.py`, go to `localhost:8089` and specify parameters of the test:
- number of users
- spawn rate
- API host

You can observe and download these metrics:
- RPS
- Min/Max/Median response time 
- Request count

[Load testing metrics](https://github.com/pacifikus/shurl/blob/hw2/load_testing_stats.md)

### Documentation

You can find Swagger documentation at the `/docs` endpoint
