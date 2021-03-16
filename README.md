# JWA (JSON Web Algorithm) related tools

Simple collection of tools to make my life dealing with JWT/JWK/JWKS easier.

Note: To run without `pipenv run python ...` you need `pipenv-shebang` installed. Install with either `sudo pip install pipenv-shebang` or `pip --user install pipenv-shebang`.

## JWK

### PEM to JWK

`./jwk.py pem-to-jwk --pretty ~/my-key.rsa.pub`

```
{
    "n": "v1ljt5FnLBsMshQtA2jR8z...9NAojndn3umzze2agmOiAV0UGFRY0HeK4o3RxjvYcHbQ",
    "e": "AQAB",
    "kty": "RSA"
}
```
