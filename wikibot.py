import click
from mylib.bot import scrape

@click.command() 
@click.option('--name', prompt='Wikipedia Page To Scrape',
              help='Entity from wiki to be scraped')

def cli(name):
    result = scrape(name='Mircosoft')
    click.echo(click.style(f"{result}:", bg ='green', fg='white'))

if __name__ == '__main__':
    cli()