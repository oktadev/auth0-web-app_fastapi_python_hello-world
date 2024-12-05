# FastAPI/Python: User Authentication Code Sample

This Python code sample demonstrates how to build web applications using FastAPI.

Visit the ["FastAPI/Python Security: Application Developer Guides"](https://developer.auth0.com/resources/guides/web-app?language=python) section of the ["Auth0 Developer Resources"](https://developer.auth0.com/resources) to explore how you can secure FastAPI applications written in Python by implementing user authentication with Auth0.

## Why Use Auth0?
Auth0 is a flexible solution to add authentication and authorization services to your applications. Your team and organization can avoid the cost, time, and risk that come with building your own solution to authenticate and authorize users. We offer tons of guidance and SDKs for you to get started and integrate Auth0 into your stack easily.

## Set Up and Run the FastAPI Project

To set up and run the project, you'll have to first set up a new virtual environment:

```console
python3 -m venv .env
```

Then, you can activate the environment:

```console
source .env/bin/activate
```

And finally install the dependencies:

```console
pip install -r requirements.txt
```

## Run the Project

To run the project and start the web app, make sure you are in the root directory, then run:

```console
uvicorn main:app --reload --port 4040
```

Visit [http://localhost:4040/](http://localhost:4040/) to access the starter web application.
