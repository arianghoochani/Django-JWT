from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.response import Response

def CustomException(exc, context):
    if isinstance(exc, AuthenticationFailed):
        return Response({'status':"0",'description':"failed to authorize.",'username':"",'scope':""}, status=status.HTTP_401_UNAUTHORIZED)
    return exception_handler(exc, context)

