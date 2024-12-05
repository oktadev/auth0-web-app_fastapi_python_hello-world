from fastapi import Request, HTTPException, status


def protected_endpoint(request: Request):
    """
    This Dependency protects an endpoint and it can only be accessed if the user has an active session
    """
    if 'id_token' not in request.session:  # it could be userinfo instead of id_token
        # this will redirect people to the login after if they are not logged in
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            detail="Not authorized",
            headers={
                "Location": "/login"
            }
        )
