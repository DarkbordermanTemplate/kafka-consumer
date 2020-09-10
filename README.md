# kafka-consumer
A simple Kafka consumer example template using confluent-kafka.

![Integration](https://github.com/DarkbordermanTemplate/kafka-consumer/workflows/Integration/badge.svg)
![Build](https://github.com/DarkbordermanTemplate/kafka-consumer/workflows/Build/badge.svg)

## Development

### Prerequisitive

| Name | Version |
| --- | --- |
| Python | 3.7 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

0. Initialize environment variable

```
cp sample.env .env
```

1. Initialize Python environment

```
make init
```

2. Enter the environment and start developing

```
pipenv shell
```

3. Start kafka-consumer service

```
cd kafka/
python3 kafka/app.py
```
The service will start at 127.0.0.1:9092

### Formatting

This project uses `black` and `isort` for formatting

```
make reformat
```

### Linting

This project uses `pylint` and `flake8` for linting

```
make lint
```

### Testing

This project uses `pytest` and its extension(`pytest-cov`) for testing

## Deployment

### Prerequisitive

| Name | Version |
| --- | --- |
| Docker | 19.03.6 |
| docker-compose | 1.17.1 |

### Building image

```
docker-compose build
```
This will build the image with tag `kafka-consumer:latest`

### Integration testing(with a single-node kafka)

0. Start containers
```
docker-compose up -d
```

1. Enter kafka and create example messages
```
docker exec -it kafka bash
(In kafka container)kafka-producer-perf-test\
 --topic example\
 --throughput -1\
 --num-records 1\
 --record-size 1\
 --producer-props bootstrap.servers=kafka:9092
```

## Contribution

* Darkborderman/Divik(reastw1234@gmail.com)
