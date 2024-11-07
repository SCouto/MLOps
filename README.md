# MLOps

This repo contains 3 projects.

Each project have a Dockerfile, and two of them a webapp in Flask

## Project 1: Jupyter_docker

This is just a jupyter notebook environment. It has preloaded two scripts, one for each of the other projects

| File                                  | Description                                                                                                                                                               |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| plot_digits_classification.ipynb      | Script that download the source data, prepare it and train the model to identify digits from an image                                                                     |
| plot_multiouput_face_completion.ipynb | Script to download the source data, prepare it and train 4 models to complete a face from the top half of a provided one. It traing 4 models to compare different outputs |

### Running the project

```shell
docker build -t jupyter-local .
docker run -p 8888:8888 -v "$(pwd)":/home/jovyan/work jupyter-local
```

Then access http://localhost:8888

## Project 1: digits

This project is a webapp that allows the user to upload an image and the model will identify the digits in the image. Model should be downloaded from the jupyter notebook and copy to the `digits` folder

### Running the project

```shell
docker build -t digits-app .
docker run -p 5005:5000 -v digits-app
```

Then access http://localhost:5005

## Project 2: faces

This project is a webapp that allows the user to upload an image of a face and the model will take the top half of the given face and predict the bottom half with 4 different models. Again, the models should be downloaded and copied to the models folder

### Running the project

```shell
docker build -t faces-app .
docker run -p 5010:5000 -v faces-app
```
Then access http://localhost:5010

