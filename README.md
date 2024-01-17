# Django-JWT
JWT stands for JSON Web Token, which is a compact and self-contained way to securely transmit information between parties as a JSON object. JWTs are commonly used in web applications as a way to verify the identity of users and ensure that they have the appropriate permissions to access certain resources.
A JWT is comprised of three parts: a header, a payload, and a signature. 
The header contains information about the type of token and the cryptographic algorithm used to generate the signature. For instance:
![alt text](https://github.com/arianghoochani/Django-JWT/blob/main/jwt.PNG "optional title")

The payload contains the actual information being transmitted, such as user data or access permissions. The signature is used to verify that the token has not been tampered with and that the data contained in it is authentic.
The signature in a JSON Web Token (JWT) is a crucial component that ensures the integrity and authenticity of the token. It is used to verify that the contents of the JWT have not been changed during transmission and that the token was indeed issued by a trusted party.
