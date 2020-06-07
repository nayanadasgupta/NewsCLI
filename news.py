import click
import requests
from pyfiglet import figlet_format

api_key = "7Rli8AUFCxc0wmSEf8CxAp9AUp86Iejh"

@click.group()
def cli():
    """
    Simple CLI for querying the top New York Times stories. Data provided by The New York Times.
    Find out more by entering news COMMAND --help.
    """
    click.echo(figlet_format("News CLI"))
    click.echo("Data provided by The New York Times.\n")
    pass

@click.command()
@click.option("--count", default=1, help="Number of top stories.",type=int)
@click.option('--type', default='main', help="Type of top stories. Options are main, arts, business, health, politics, science," +
                                             "tech and world. Default is main.")
def topStories(count,type):
    """
    Top Stories.
    """
    if type == 'arts':
        click.echo("Top Stories in Arts\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/arts.json?api-key=' + api_key
    elif type == 'business':
        click.echo("Top Stories in Business\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/business.json?api-key=' + api_key
    elif type == 'health':
        click.echo("Top Stories in Health\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/health.json?api-key=' + api_key
    elif type == 'politics':
        click.echo("Top Stories in Politics\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/politics.json?api-key=' + api_key
    elif type == 'science':
        click.echo("Top Stories in Science\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/science.json?api-key=' + api_key
    elif type == 'tech':
        click.echo("Top Stories in Technology\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=' + api_key
    elif type == 'world':
        click.echo("Top World Stories\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/world.json?api-key=' + api_key
    else:
        click.echo("Top Stories\n")
        url = 'https://api.nytimes.com/svc/topstories/v2/home.json?api-key=' + api_key
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        click.echo("An error has occurred - please wait 30 seconds before trying again.")
    else:
        try:
            for i in range(count):
                click.echo(response.json()['results'][i]['title'])
                click.echo(response.json()['results'][i]['abstract'])
                click.echo(response.json()['results'][i]['url'])
                click.echo(response.json()['results'][i]['updated_date'] + "\n")
        except IndexError:
            click.echo("No remaining news stories in this category\n")

@click.command()
@click.option("--count", default=1, help="Number of popular stories.",type=int)
def mostviewed(count):
    """
        Most viewed articles in the last seven days.
    """
    url = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=" + api_key
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        click.echo("An error has occurred - please wait 30 seconds before trying again.")
    else:
        try:
            for i in range(count):
                click.echo(response.json()['results'][i]['title'])
                click.echo(response.json()['results'][i]['abstract'])
                click.echo(response.json()['results'][i]['url'])
                click.echo(response.json()['results'][i]['updated'] + "\n")
        except IndexError:
            click.echo("No remaining news stories in this category\n")

@click.command()
@click.option("--count", default=1, help="Number of popular stories.",type=int)
def mostrecent(count):
    """
        Most recent articles published.
    """
    url = "https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=" + api_key
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        click.echo("An error has occurred - please wait 30 seconds before trying again.")
    else:
        try:
            for i in range(count):
                click.echo(response.json()['results'][i]['title'])
                click.echo(response.json()['results'][i]['abstract'])
                click.echo(response.json()['results'][i]['url'])
                click.echo(response.json()['results'][i]['updated_date'] + "\n")
        except IndexError:
            click.echo("No remaining news stories in this category\n")

@click.command()
@click.argument("keyword")
@click.option("--count", default=1, help="Number of stories.",type=int)
def search(keyword,count):
    """
    Search articles by a keyword
    """
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + keyword + "&api-key=" + api_key
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        click.echo("An error has occurred - please wait 30 seconds before trying again.")
    else:
        try:
            for i in range(count):
                click.echo(response.json()['response']['docs'][i]['abstract'])
                click.echo(response.json()['response']['docs'][i]['lead_paragraph'])
                click.echo(response.json()['response']['docs'][i]['web_url'])
                click.echo(response.json()['response']['docs'][i]['pub_date'] + "\n")
        except IndexError:
            click.echo("No remaining news stories in this category\n")

cli.add_command(topStories)
cli.add_command(mostviewed)
cli.add_command(mostrecent)
cli.add_command(search)

