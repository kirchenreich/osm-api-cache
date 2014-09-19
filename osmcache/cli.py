import os
import multiprocessing

import click

from .db import engine
from .parser import OSMParser
from .consumer import consume_item

@click.group()
def base():
    pass

@base.command()
def initdb():
    from models import Base
    Base.metadata.create_all(engine)
    click.echo("db created (if needed)")

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

@base.command()
@click.argument('osm-file', type=click.File('rb'))
def import_osm(osm_file):
    osm_parser = OSMParser(osm_file)

    consumer_pool = multiprocessing.Pool(2)
    consumer_pool.imap(consume_item, osm_parser.iterparser(), 5000)

    consumer_pool.close()
    consumer_pool.join()
