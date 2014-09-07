import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from credentials import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DBNAME

d = {'NAME': POSTGRES_USERNAME,
     'PASSWORD': POSTGRES_PASSWORD,
     'DBNAME': POSTGRES_DBNAME}

engine = create_engine('postgresql://{NAME}:{PASSWORD}@localhost:5432/{DBNAME}'.format(**d))
session = sessionmaker(bind=engine)()


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    from models import Base
    Base.metadata.create_all(engine)
    click.echo("db created (if needed)")

@cli.command()
@click.argument('osm-file', type=click.File('rb'))
def import_osm(osm_file):
    from parser import OSMParser
    OSMParser(osm_file).parse()

def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@cli.command()
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to drop the db?')
def dropdb():
    from models import Base
    Base.metadata.drop_all(engine)
    click.echo("all tables dropped")


if __name__ == '__main__':
    cli()
