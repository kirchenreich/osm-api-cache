import os

import click

from .db import engine
from .parser import OSMParser

@click.group()
def base():
    pass

@base.command()
def initdb():
    from models import Base
    Base.metadata.create_all(engine)
    click.echo("db created (if needed)")

@base.command()
@click.argument('osm-file', type=click.File('rb'))
def import_osm(osm_file):
    OSMParser(osm_file).parse()

def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@base.command()
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to drop the db?')
def dropdb():
    from models import Base
    Base.metadata.drop_all(engine)
    click.echo("all tables dropped")
