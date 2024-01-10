# redirect-service-test
Service that allows for redirecting incoming HTTP traffic to a number of individual hosts / domains
   
## Requirements
* `poetry` - tool for package management

## How to run the application
1. Clone the repository
2. Run `poetry install` in the root directory
3. Run `poetry run flask run --host=0.0.0.0 --debug` in the root directory
4. The application will be available at `http://localhost:5000`
5. Now you can send requests to the application (see below)

## How to send requests to the application
1. Send a request with any method (GET, POST, PUT) to `http://localhost:5000/redirect/<pool_id>`
   
   where `<pool_id>` is the id of the pool of hosts / domains to which the request should be redirected
2. The application will redirect the request to one of the hosts / domains from the pool with the given id

## How to run the tests
1. Run `PYTHONPATH=. poetry run pytest` in the root directory


---

## Notes on Non-Functional Requirements

### Availability
The application is highly available. It can be run in multiple instances behind a load balancer.

### Scalability
The application can be scaled in both vertical and horizontal directions.
Horizontal scaling can be achieved by running multiple pods with the application.
Vertical scaling can be achieved by increasing the resources allocated to the pods.

### Performance
The application is fast and lightweight. It can handle a large number of requests per second.

### Observability
To have alerts about the application's health, we can use Prometheus and Grafana. Logging can be improved to achieve the desired observability. 
