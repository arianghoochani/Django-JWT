from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ValidationError 
from .models import CustomUser
from .classes import AuthorizationException,AuthorizingResponse
from .serializers import AuthorizingResponseSerializer
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

def verifyRegisterUserRequest(exception, request):
    data = request.data
    registerUserRequest = "" 
    authorization_header = request.headers.get('Authorization')
    token_type, token = authorization_header.split(' ')
    user = getUser(exception,token)
    if (token_type.lower() == 'bearer'):
        if (user.is_superuser):
            try:
                serializer = RegisterUserRequestSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                registerUserRequest = serializer.save()
            except ValidationError :
                attributeName = list(serializer.errors.keys())[0]
                exception.errorKey = attributeName
                try:
                    logging.info("error={error} value={value}".format(error=str(ValidationError), value=data[attributeName]))
                except:
                    logging.warning("error={error}  {attribute} is empty".format(error=str(ValidationError), attribute = attributeName))
            except Exception as unknownException :
                exception.errorKey = "system_error"
                logging.error("error={error} exceptionCode={code} desc={desc}".format(error=unknownException, code=exception.read().exceptionCode, desc=exception.exceptionDesc))
        else:
            exception.errorKey = "inadequate_credentials"
    else:
        exception.errorKey = "invalid_tokenType_error"
    return registerUserRequest


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





@api_view(['POST'])  
def registerUser(request):
    returnFlag = "0"
    exception = AuthorizationException(errorKey="initial_error")
    registerUserRequest = verifyRegisterUserRequest(exception,request)
    if (registerUserRequest):
        try:
            if CustomUser.objects.filter(username = registerUserRequest.username).exists():
                exception.errorKey = "user_allready_exists"
            else:
                user = CustomUser(username = registerUserRequest.username,scope = registerUserRequest.scope,is_superuser = registerUserRequest.is_superuser)
                user.set_password(registerUserRequest.password)
                user.save(force_insert=True)
                returnFlag = "1"
                exception.errorKey = "successful"
        except:
            exception.errorKey = "failed_to_register_new_user"

    exception.read()
    registeruserResponse = RegisterUserResponse(exception,returnFlag)
    serializer = RegisterUserResponseSerializer(registeruserResponse)
    return Response(serializer.data)

class RegisterUserRequest():
    def __init__(self,username,password,scope,is_superuser):
        self.username = username
        self.password = password
        self.scope = scope
        self.is_superuser = is_superuser