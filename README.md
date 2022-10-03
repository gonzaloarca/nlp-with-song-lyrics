# Natural Language Processing with Song Lyrics

# Dependencies
* pipenv
* Python 3.10
* Genius API key saved in environment variable `GENIUS_ACCESS_TOKEN`

## How to use scraper
First, move to the `scraper` folder of the project and run the following command
```python
pipenv shell
```

This will create a virtual environment for you to run the scraper. Once you are in the virtual environment, run the following command to install the dependencies
```python
pipenv install
```

Once the dependencies are installed, move to the root folder of the project, and then you can run the scraper by running the following command
```python
python -m scraper.get_data 
```

For instructions on how to use the scraper, please refer to the help message by running:
```python
python -m scraper.get_data -h
``` 

> NOTE: Make sure you have a Genius API key saved in the environment variable `GENIUS_ACCESS_TOKEN` before running any of the scripts in the scraper folder.