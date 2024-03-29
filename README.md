[![codecov](https://codecov.io/gh/2Cheetah/my_test_website/graph/badge.svg?token=RHXRLBO590)](https://codecov.io/gh/2Cheetah/my_test_website)

# Purpose

The purpose of the project is to improve knowledge of web development by using following tools:
- Docker
- docker-compose
- Fast API
- uvicorn
- terraform
- k8s?
- nginx
- yaml
- deployment with Github Actions
- postgresql
- TDD

# Project description

Run a web site with dummy content - 2 pages:
- ./ -> Hello World
- ./about -> about page with this README file

The web site is to be hosted on AWS Lightsail.

# High-level architecture

```mermaid
graph LR;
	user<-->nginx
	subgraph AWS Lightsail
	nginx<-->webapp
	webapp<-->postgres
	end
```

