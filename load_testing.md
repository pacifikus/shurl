# Load testing tools review

## [Locust](https://locust.io/)

Locust is an easy to use, scriptable and scalable performance testing tool.

### Features:

- Write test scenarios in plain old Python
- Web-based UI
- Can test any system
- Locust is small and very flexible
- Running in Docker
- Distributed load generation with Terraform/AWS
- Retrieving tests statistics


## [Molotov](https://molotov.readthedocs.io/en/stable/)

Simple Python 3.7+ tool to write load tests.
Based on asyncio, Built with aiohttp 3.x

### Features:

- Simple tests scenarios in pPython
- Flexible setup with fixtures and customization
- Running in Docker
- CLI options

## Comparison

| Feature             | Locust | Molotov | 
|:-------------------:|:------:|:-------:|
| Flexibility         | +      | +       |
| UI                  | +      | -       | 
| CLI                 | +      | +       | 
| Distributed testing | +      | -       | 
| Retrieveing stats   | +      | -       | 
| Running in Docker   | +      | +       | 