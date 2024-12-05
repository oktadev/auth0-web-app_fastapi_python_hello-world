from config import app

from auth.routes import auth_router
from webapp.routes import webapp_router


app.include_router(auth_router)
app.include_router(webapp_router)
