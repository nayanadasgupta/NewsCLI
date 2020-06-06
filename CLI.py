import click
import requests

api_key = "7Rli8AUFCxc0wmSEf8CxAp9AUp86Iejh"

@click.group()
def main():
    """
    Simple CLI for querying the top New York Times stories. Data provided by The New York Times.
    """
    pass

@main.command()
@click.option("--count", default=1, help="Number of top stories.")
def topStories(count):
    url = 'https://api.nytimes.com/svc/topstories/v2/home.json?api-key=' + api_key
    response = requests.get(url)
    for i in range(count):
        click.echo(response.json()['results'][i]['title'])
        click.echo(response.json()['results'][i]['abstract'])
        click.echo(response.json()['results'][i]['url'])
        click.echo(response.json()['results'][i]['updated_date'])

if __name__ == "__main__":
    topStories()

