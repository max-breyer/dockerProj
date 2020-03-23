# dockerProj

This is a repository for ideas about applying principles of reproducable computing to genetics.

## Getting Started

### Prerequisites

To run this project you will need to install docker which you can get [here](https://www.docker.com/).

### Set up

Set the environment variables to be passed into the docker container by filling in the env.list file.

Build the docker image like:

```
docker build -t my-image .
```

### Run the analysis

Run the docker image like the following replacing HOSTVOLUME with an absolute path to the directory where the data to be analysed is.

```
docker run \
  --env-file env.list \
  -v HOSTVOLUME:/dat \
  my-image
```

### That's all

Your results will be in a folder named results in the HOSTVOLUME directory.
