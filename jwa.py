#!/usr/bin/env pipenv-shebang
import json
import time

import click
from authlib.jose import jwk, jwt


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.group(name="jwk")
def jwk_command():
    pass


@jwk_command.command()
@click.argument("input", type=click.Path(exists=True))
@click.option("--pretty/--no-pretty", default=False)
@click.pass_context
def from_pem(ctx, input, pretty):
    with open(input) as content:
        jwk_dict = jwk.dumps(content.read(), kty="RSA")
        jwk_serialized = str(jwk_dict)
        if pretty:
            jwk_serialized = json.dumps(jwk_dict, indent=4)

        click.echo(jwk_serialized)


@cli.group(name="jwt")
def jwt_command():
    pass


@jwt_command.command()
@click.argument("input", type=click.Path(exists=True))
@click.option("-i", "--issuer")
@click.option("-s", "--subject")
@click.option("-a", "--audience")
@click.option("-e", "--expiration", type=int, default=600)
@click.pass_context
def signed_by_pem(ctx, input, issuer, subject, audience, expiration):
    with open(input) as content:
        jwk_dict = jwk.dumps(content.read(), kty="RSA")
        header = {"alg": "RS256"}
        payload = {
            "exp": int(time.time()) + expiration,
            "aud": audience,
            "sub": subject,
            "iss": issuer,
        }
        jwt_base64 = jwt.encode(header, payload, jwk_dict).decode("ascii")
        click.echo(jwt_base64)


if __name__ == "__main__":
    cli()
