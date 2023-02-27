from typing import Dict
from jose import jwt
import jose

from utils.api_errors import ErrorAuthenticationInvalid

class JwtTokenDecoder:
    """Jwt Token Decoder."""

    def __init__(
        self,
        issuer: str,
        algorithm: str,
        audience: str,
        key: Dict
    ):
        """JWT Token Decoder.

        Args:
        ----
            issuer (str): Who generate the token
            algorithm (str): Valid algorithms that should be used to verify the JWS.
            audience (str): The intended audience of the token.
            key (Dict): A key to attempt to verify the payload with.

        """
        self.issuer = issuer
        self.algorithm = algorithm
        self.audience = audience
        self.key = key

    def decode(self, token: str) -> Dict:
        """Decode a JWT string token and returns a Dictionary.

        Args:
        ----
            token (str): a jwt encripted token

        Returns
        -------
            Dict: a dict with values of token

        """

        try:
            unverified_header = jwt.get_unverified_header(token)
        except jose.exceptions.JWTError:
            raise ErrorAuthenticationInvalid


        rsa_key = {}
        for key in self.key["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
                break

        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=self.algorithm,
                audience=self.audience,
                issuer=self.issuer
            )
        except jose.exceptions.JWTError:
            raise ErrorAuthenticationInvalid
        except jose.exceptions.JWKError:
            raise ErrorAuthenticationInvalid
        return payload
