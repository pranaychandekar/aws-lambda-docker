## AWS Lambda Functions - Docker

This repository is a Plug and Play template to create containerized AWS Lambda Functions. The documentation contains:

1.  Descriptions of the files
2.  Instructions to use the template
3.  Instructions to test the container locally

---

## Content Details

| File Name | Description |
| --- | --- |
| `Dockerfile` | The dockerfile used to create the docker image |
| `app.py` | The code that we want to run in lambda |
| `requirements.txt` | The dependencies required for our code to run |

---

## How to use it as Plug & Play?

1.  On every lambda trigger, the `handler` function in the `app.py` file will be executed. Plug the code into the `app.py` file and make calls to respective modules in the `handler` function.
2.  Add the required dependencies to the `requirements.txt` file.

---

## Testing the Lambda Function container

**Step 01**: Build the docker image of the lambda function

Run the following command in the directory with the Dockerfile

```plaintext
 docker build --network=host -t lambda:v1 .
```

Check the container with the following command

```plaintext
docker images
```

**Step 02**: Run the lambda function container

Run the following command.

```plaintext
docker run --network=host --name=lambda lambda:v1
```

This will create the lambda function container. Now your container is up and running to process the invocation.

**Step 03**: Invoke your lambda function

From another terminal, please execute the below command.

```plaintext
curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"test": "payload"}'
```

This should return a response similar to the following:

```plaintext
{"statusCode": 200, "requestId": "49f8b661-d119-4b54-ad19-ca7591860ef3", "request": {"test": "payload"}}
```

---

**Author**: [Pranay Chandekar](https://linktr.ee/pranaychandekar)