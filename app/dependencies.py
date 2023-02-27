from services.security import JwtTokenDecoder
from config.settings import get_settings
from utils.api_errors import ErrorAuthenticationInvalid, Forbidden


def auth_user(token: str):
    settings = get_settings()
    
    jwt = JwtTokenDecoder(
        algorithm=settings.JWT_ALGORITHM,
        audience=settings.JWT_AUDIENCE,
        key=settings.JWT_RSA_KEY,
        issuer=settings.JWT_ISSUER
    )
    _token_type, _token = token.split(" ")
    
    return jwt.decode(_token)


def decode_token(res, req, data=None):
    token = req.get_header("authorization")
    if not token:
        res.write_status(Forbidden.status_code).end(Forbidden.error)
        return False

    try:
        user = auth_user(token)
    except ErrorAuthenticationInvalid as e:
        res.write_status(e.status_code).end(e.error)
        return False

    return user

