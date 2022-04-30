# aws-lambda-docker
This repository is a plug and play template to create containerized AWS Lambda Functions

**Table of Contents**

[TOC]


# Content Details
| File Name | Description |
| ------------- | ------------------------------ |
| `Dockerfile` | The dockerfile used to create the docker image |
| `app.py` | The code that we want to run in lambda |
| `requirements.txt` | The dependencies required for our code to run |


# How to use it as Plug & Play?

1. On every lambda trigger, the `handler` function in the `app.py` file will be executed. Plug the code in the `app.py` file and make calls to respective modules in the `handler` function.
2. Add the required dependencies in the `requirements.txt` file. 
