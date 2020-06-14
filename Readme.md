# NewsCLI

A simple command line interface for querying the New York Times, created using Python and Click.

<img width="1149" alt="Screenshot 2020-06-14 at 19 27 44" src="https://user-images.githubusercontent.com/43610663/84601001-2433c280-ae75-11ea-9abd-3f3c10755650.png">

## Setup

1. Make a free New York Times Developer Account at developer.nytimes.com.
2. Create an API key with the following permissions: Most Popular API, Times Wire API, Article Search API, Books API and Top Stories API.
3. Set your api_key to your API key.
4. To try the CLI in a virtualenv make a new virtualenv and install the package. The --editable option allows you to make changes to the CLI. 

```
$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
```
## Usage

```news --help``` 

Shows the main help page and all options and commands available.

More specific help pages for each command can be accessed using: ``` news COMMAND --help``` 

```news topstories```

Returns the current top story. Additional top stories can be returned using the ```--count``` option and ```--type``` can be used to specify the type of top stories returned. Available options are  main (default), arts,
                   business, health, politics, science, tech and world 
                   
e.g. ```news topstories --count=4 --type=politics```

```news search KEYWORD```

e.g. ```news search home --count=4```

Searches for articles related to the given keyword argument. By default only one story is returned however, the user can request additional stories using the ```--count``` option.

```news mostviewed```

Returns the most viewed article. The user can request additional popular articles using the ```--count``` option.

e.g. ```news mostviewed --count=2```

```news mostrecent```

Returns the most recent article. The user can request additional recent articles using the ```--count``` option.
              
e.g. ```news mostrecent --count=2```

```news books```

Returns books from the NYT bestseller lists. By default, if no option ```--type``` is provided fiction books are provided. Alternatively, the user can specify fiction or non-fiction using the ```-type``` option. The number of books returned can be specified using the ```--count``` option, by default one book is returned. 


![poweredby_nytimes_150c](https://user-images.githubusercontent.com/43610663/84601042-6f4dd580-ae75-11ea-9f6b-119ef9bc592d.png)