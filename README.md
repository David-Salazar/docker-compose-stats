# docker-compose-stats

This library is a small wrapper around the `docker stats` command. It fires up a live dashboard to check how many resources
your container is using. It also allows you to filter your searches by the docker-compose project name or any string present in
the containers' names. 

## Installation

Once you have installed docker and cloned the repository, run the following commands:

```
docker build -t docker-stats . 
docker container run docker-stats
```

Finally, to see the live dashboard go to [http://localhost:8866/
](http://localhost:8866/) in your browser. 