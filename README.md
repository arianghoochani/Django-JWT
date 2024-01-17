# Django-JWT
JWT stands for JSON Web Token, which is a compact and self-contained way to securely transmit information between parties as a JSON object. JWTs are commonly used in web applications as a way to verify the identity of users and ensure that they have the appropriate permissions to access certain resources.
A JWT is comprised of three parts: a header, a payload, and a signature. 
The header contains information about the type of token and the cryptographic algorithm used to generate the signature. For instance:
![alt text](https://github.com/arianghoochani/Django-JWT/blob/main/jwt.PNG "optional title")

The payload contains the actual information being transmitted, such as user data or access permissions. The signature is used to verify that the token has not been tampered with and that the data contained in it is authentic.
The signature in a JSON Web Token (JWT) is a crucial component that ensures the integrity and authenticity of the token. It is used to verify that the contents of the JWT have not been changed during transmission and that the token was indeed issued by a trusted party.

The project in this Repository is an authorization service that i deveoped it with DRF(Django RestFramework). For easier using I dockerized it and all you need is installing docker on your Machine, clone this repository, go to the jwtService directory, run the command: 
```
docker-compose build
```
and wait for building the image compeletly and after that enter:
```
docker-compose up -d
```
and it is done, your authorization service is ready to use :))

In the next paragrtaphs I will give more details about mechanism, configuration and guidance for usage of this service.

## **Endpoints**
| Name | Address | method | Description |
|:---------|:---------|:---------|:---------|
| Login | http://localhost_url/jwt/login/ | POST | gives access and refresh token to the valid users  |
| authorization | http://localhost_url/jwt/verifytoken/ | POST | checks if a user with a specific token has the credential to work with the system  |
| refresh | http://localhost_url/jwt/refresh/ | POST | replaces expired access token with the new one by receiving valid refresh token  |
| register user | http://localhost_url/jwt/register/ | POST | adds new users to the system  |

for more clearence in using authorization service sample of input and output of all 4 endpoints of our system are shown below in the postman respectively:

![alt text](https://github.com/arianghoochani/Django-JWT/blob/main/login-method.png "login method")
