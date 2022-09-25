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

### Documentation

You can find Swagger documentation at the `/docs` endpoint