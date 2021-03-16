#!/usr/bin/env pipenv-shebang
import json

import click
from authlib.jose import jwk


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command()
@click.argument("input", type=click.Path(exists=True))
@click.option("--pretty/--no-pretty", default=False)
@click.pass_context
def pem_to_jwk(ctx, input, pretty):
    with open(input) as content:
        jwk_dict = jwk.dumps(content.read(), kty="RSA")
        jwk_serialized = str(jwk_dict)
        if pretty:
            jwk_serialized = json.dumps(jwk_dict, indent=4)

        click.echo(jwk_serialized)


if __name__ == "__main__":
    cli()
