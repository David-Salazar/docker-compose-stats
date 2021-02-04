# docker-compose-stats

This library is a small wrapper around the `docker stats` command. It fires up a live dashboard to check how many resources
your container is using. It also allows you to filter your searches by the docker-compose project name or any string present in
the containers' names. 

## Installation

This project uses conda as a package manager. Therefore, once you have cloned the repository, run the following commands to install 
the required packages for this application in a separate conda environment:

```
conda env create -f environment.yml
conda activate docker-stats
```

Each time you want to run the dashboard, you'll have to activate the conda environment. Finally, launch the dashboard thus:

```
voila user_interface.ipynb
```

Finally, to see the live dashboard go to [http://localhost:8866/
](http://localhost:8866/) in your browser. 