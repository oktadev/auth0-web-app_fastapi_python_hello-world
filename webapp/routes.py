from fastapi import APIRouter, Depends, Request

from auth.dependencies import protected_endpoint
from config import templates
from services.message_service import MessageService


webapp_router = APIRouter()


@webapp_router.get("/")
def home(request: Request):
    """home endpoint"""
    features = [{
        "title": "Identity Providers",
        "description":
            "Auth0 supports social providers such as Google, Facebook, and Twitter, along with Enterprise providers "
            "such as Microsoft Office 365, Google Apps, and Azure. You can also use any OAuth 2.0 Authorization "
            "Server.",
        "resourceUrl": "https://auth0.com/docs/connections",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/identity-providers-logo.svg",
    }, {
        "title": "Multi-Factor Authentication",
        "description":
            "You can require your users to provide more than one piece of identifying information when logging in. "
            "MFA delivers one-time codes to your users via SMS, voice, email, WebAuthn, and push notifications.",
        "resourceUrl": "https://auth0.com/docs/multifactor-authentication",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/mfa-logo.svg",
    }, {
        "title": "Attack Protection",
        "description":
            "Auth0 can detect attacks and stop malicious attempts to access your application such as blocking traffic "
            "from certain IPs and displaying CAPTCHA. Auth0 supports the principle of layered protection in security "
            "that uses a variety of signals to detect and mitigate attacks.",
        "resourceUrl": "https://auth0.com/docs/attack-protection",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/advanced-protection-logo.svg",
    }, {
        "title": "Serverless Extensibility",
        "description":
            "Actions are functions that allow you to customize the behavior of Auth0. Each action is bound to a "
            "specific triggering event on the Auth0 platform. Auth0 invokes the custom code of these Actions when the "
            "corresponding triggering event is produced at runtime.",
        "resourceUrl": "https://auth0.com/docs/actions",
        "icon": "https://cdn.auth0.com/blog/hello-auth0/private-cloud-logo.svg",
    }]

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "features": features
        }
    )


@webapp_router.get("/profile", dependencies=[Depends(protected_endpoint)])
def profile(request: Request):
    """
    Profile endpoint, should only be accessible after login
    """
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "userinfo": request.session['userinfo']
        }
    )


@webapp_router.get("/public")
def public(request: Request):
    """
    Public endpoint, anyone can access this
    """
    return templates.TemplateResponse(
        "public.html",
        {
            "request": request,
            "message": MessageService().public_message()
        }
    )


@webapp_router.get("/protected", dependencies=[Depends(protected_endpoint)])
def protected(request: Request):
    """
    Protected endpoint, should only be accessible after login
    """
    access_token = request.session['access_token']
    return templates.TemplateResponse(
        "protected.html",
        {
            "request": request,
            "message": MessageService().protected_message(access_token)
        }
    )


@webapp_router.get("/admin", dependencies=[Depends(protected_endpoint)])
def admin(request: Request):
    """
    Admin endpoint, should only be accessible after login if the user has the admin permissions
    """
    access_token = request.session['access_token']
    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            "message": MessageService().admin_message(access_token)
        }
    )
