from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from .error_codes import INVALID_TOKEN
class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except AuthenticationFailed as e:
            return self.handle_failed_authentication(e)

    def handle_failed_authentication(self, exc):
        raise AuthenticationFailed(Response(INVALID_TOKEN,status=status.HTTP_401_UNAUTHORIZED)) 
