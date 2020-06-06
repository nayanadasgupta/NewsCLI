import click
import requests
from pyfiglet import figlet_format

api_key = "7Rli8AUFCxc0wmSEf8CxAp9AUp86Iejh"

@click.group()
def cli():
    """
    Simple CLI for querying the top New York Times stories. Data provided by The New York Times.
    """
    click.echo(figlet_format("News CLI"))
    click.echo("Data provided by The New York Times.\n")
    pass

@click.command()
@click.option("--count", default=1, help="Number of news stories.")
@click.option('--type', default='main', help="Type of top stories. Options are main, arts, business, health, politics, science," +
                                             "technology and word")
def topStories(count,type):
    if (type == 'main'):
        url = 'https://api.nytimes.com/svc/topstories/v2/home.json?api-key=' + api_key
    response = requests.get(url)
    for i in range(count):
        click.echo(response.json()['results'][i]['title'])
        click.echo(response.json()['results'][i]['abstract'])
        click.echo(response.json()['results'][i]['url'])
        click.echo(response.json()['results'][i]['updated_date'] + "\n")

cli.add_command(topStories)

if __name__ == "__main__":
    cli()

