import configparser

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils import to_pretty_json


def load_config():
    """
    Loads configuration from .config file
    """
    config = configparser.ConfigParser()
    config.read(".config")
    return config


def create_templates():
    templates = Jinja2Templates(directory="templates")
    templates.env.filters['to_pretty_json'] = to_pretty_json
    return templates


templates = create_templates()


def create_app():
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app

app = create_app()


@app.exception_handler(404)
async def custom_404_handler(request: Request, _):
    """Display a custom 404 page instead of JSON response"""
    return templates.TemplateResponse(
        "404.html",
        {
            "request": request,
            "message": "Not Found"
        }
    )
