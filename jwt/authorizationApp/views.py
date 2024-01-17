from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from django.conf import settings
import jwt
import logging



def tokenVerified(exception,loginRequestHeader):
    token = ""
    try:
        token_type, token = loginRequestHeader.split(' ')
        if token_type == 'BEARER':
            token = token
        else:
            exception.errorKey = 'invalid_tokenType_error'
            logging.info("error={error} exceptionCode={code} desc={desc}".format(error="type of token is not bearer. type of token is : {token_type}".format(token_type=token_type), code=exception.read().exceptionCode, desc=exception.exceptionDesc))
    except:
        exception.errorKey = 'invalid_token_error'
        logging.warning("error={error} exceptionCode={code} desc={desc}".format(error="entered token is invalid", code=exception.read().exceptionCode, desc=exception.exceptionDesc))
    return token

def getUser(exception,token):
    user = ""
    if not token == "":
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            userId = decoded_token['user_id']
        except:
            pass
        try:
            user = CustomUser.objects.get(pk=userId)
        except CustomUser.DoesNotExist:
            exception.errorKey = 'user_not_exists_error'
            logging.warning("error={error} exceptionCode={code} desc={desc}".format(error="entered token is invalid", code=exception.read().exceptionCode, desc=exception.exceptionDesc)) 
    return user

@api_view(['POST'])
def authorizing(request):
    exception = AuthorizationException(errorKey="initial_error")
    user = ""
    loginRequestHeader = request.headers.get('Authorization')
    token = tokenVerified(exception,loginRequestHeader)
    if token:
        user = getUser(exception,token)
    if user:
        exception.errorKey = "successful"

    exception.read()
    authorizingResponse = authorizingResponse(user,exception)
    serializer = AuthorizingResponseSerializer(authorizingResponse)

    return Response(serializer.data)