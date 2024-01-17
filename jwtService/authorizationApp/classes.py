
class AuthorizingResponse():
    def __init__(self,user,exception):
        self.status = "1"
        self.description = exception.exceptionDesc
        if user:
            self.username = user.username
            self.scope = user.scope
        else:
            self.username = ""
            self.scope = ""

class AuthorizationException:
    database = {
        "successful" :
        {
            "exceptionDesc"	: "successful",
        },
        "username" :
        {
            "exceptionDesc"	: "invalid or empty username",
        },
        "password" :
        {
            "exceptionDesc"	: "invalid or empty password",
        },
        "user_not_found_error" :
        {
            "exceptionDesc"	: "user is not found",
        },
        "invalid_tokenType_error" :
        {
            "exceptionDesc"	: "token type is not bearer.",
        },
        "invalid_token_error" :
        {
            "exceptionDesc"	: "token is invalid",
        },
        "user_not_exists_error" :
        {
            "exceptionDesc"	: "user with this id does not exist.",
        },
        "scope" :
        {
            "exceptionDesc"	: "invalid scope",
        },
        "is_superuser" :
        {
            "exceptionDesc"	: "invalid is_superuser",
        },
        "failed_to_register_new_user" :
        {
            "exceptionDesc"	: "failed to register new user",
        },
        "user_allready_exists":{
            "exceptionDesc"	: "user allready exists",
        },
        "inadequate_credentials":{
            "exceptionDesc"	: "you do not have credentials to do",
        },
        "initial_error"	: 
        {
            "exceptionDesc"	: "unknown error",
        },
        "initial_error"	: 
        {
            "exceptionDesc"	: "unknown error",
        },
         "unknown_error"	: 
        {
            "exceptionDesc"	: "unknown error",
        },

    }
        

    def __init__(self, errorKey,  exceptionDesc="",):
        self.errorKey = errorKey
        self.exceptionDesc = exceptionDesc

    def read(self):
        self.exceptionDesc = AuthorizationException.database[self.errorKey]["exceptionDesc"]
        return self
    
class RegisterUserRequest():
    def __init__(self,username,password,scope,is_superuser):
        self.username = username
        self.password = password
        self.scope = scope
        self.is_superuser = is_superuser

class RegisterUserResponse():
    def __init__(self,exception,code):
        self.code = code
        self.message = exception.exceptionDesc