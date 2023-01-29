# fastapi_test
## Run

``docker-compose up --build``

### Try it using:

```http://localhost:8019/24.148.0.133```

## PyTest 

``docker-compose -f docker-compose-tests.yml up --build``


## Advanced Features
* Support Dependency Injection
* Redis Cache
* Configurable API endpoints (see services.json)
* Container based
* Includes a basic test as example template



## Resources
Tests

https://www.starlette.io/testclient/

https://docs.pytest.org/en/7.2.x/

https://stackoverflow.com/questions/24617397/how-to-print-to-console-in-pytest

DI

https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

https://python-dependency-injector.ets-labs.org/examples/fastapi.html

Docker

https://testdriven.io/blog/fastapi-docker-traefik/

https://gist.github.com/sbv-trueenergy/a9a6971778a01d1acd3c466719e690b8

Redis with docker-compose

https://cloudinfrastructureservices.co.uk/run-redis-with-docker-compose/

Other

https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183
