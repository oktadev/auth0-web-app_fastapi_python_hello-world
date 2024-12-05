from config import app

from webapp.routes import webapp_router


app.include_router(webapp_router)
