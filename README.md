# Converting ```.parguet``` file to ```.csv``` file

## Overview

Use Python to convert a parquet format file to a csv format file.

### Environment

- Docker version 20.10.11
- Python 3.10.1
- pandas 1.3.5
- pyarrow 6.0.1


## Prepare ```.parquet``` file

Place the file in parquet directory.


## Build Docker image & Run container

```shell
docker-compose up -d --build
```

- Enter the launched container

```shell
docker-compose exec python3 bash
```

## Execute

- Change to src directory
```shell
cd src/
```

- Convert to CSV file
```shell
python main.py
```

🙌

The converted CSV file will be output to the src directory.


## Clean up

- Exit the container
```shell
docker-compose down
```

- Check the docker image id
```shell
docker images -a
```

```
REPOSITORY                                                          TAG            IMAGE ID       CREATED          SIZE
parquet_to_csv_python3                                                latest         XXXXXXXXXXX   33 minutes ago   1.28GB
```

-  Remove the docker image
```shell
docker rmi [IMAGE ID]
```
