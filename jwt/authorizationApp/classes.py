
class AuthorizationException:
    database = {
        "successful" :
        {
            "exceptionCode" : "1",
            "exceptionDesc"	: "successful",
        },
        "username" :
        {
            "exceptionCode" : "2",
            "exceptionDesc"	: "invalid or empty username",
            "exceptionFarsiMsg"	: "نام کاربری نامعتبر یا خالی است"
        },
        "password" :
        {
            "exceptionCode" : "3",
            "exceptionDesc"	: "invalid or empty password",
            "exceptionFarsiMsg"	: "رمز عبور نامعتبر یا خالی است"
        },
        "user_not_found_error" :
        {
            "exceptionCode" : "4",
            "exceptionDesc"	: "user is not found",
            "exceptionFarsiMsg"	: "کاربری با این نام پیدا نشد"
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
        

    def __init__(self, errorKey, exceptionCode="", exceptionDesc="", exceptionFarsiMsg=""):
        self.errorKey = errorKey
        self.exceptionDesc = exceptionDesc

    def read(self):
        self.exceptionDesc = AuthorizationException.database[self.errorKey]["exceptionDesc"]
        return self