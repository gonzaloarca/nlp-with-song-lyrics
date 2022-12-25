# Natural Language Processing with Song Lyrics
The aim of this project is to apply Natural Language Processing techniques to a dataset that contains lyrics and titles to popular songs. The dataset is scraped from Billboard Hot 100 (for the popular songs catalogue) and then matched to their respective lyrics using the Genius API.

A brief analysis of the dataset is also performed to find patterns in the lyrics and titles of the songs. The analysis is performed using `pandas`, `matplotlib`, and `nltk`.

Finally, a simple machine learning model consisting of a fine-tuned T5 (Text-to-Text Transfer Transformer) model is trained to generate song titles from the lyrics of the songs. The model is trained using Hugging Face's `transformers` and `pytorch`. 

# Dependencies
* pipenv
* Python 3.10
* Genius API key saved in environment variable `GENIUS_ACCESS_TOKEN`

# How to use scraper
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

# Language Model for Song Title Generation
The language model is created and trained using the `transformers` and `pytorch` libraries within a Jupyter Notebook, hosted in Google Colab.

[Google Colab link](https://colab.research.google.com/drive/1XagZ25GG5bhrkdxLY_JKGmQmJ9klq_pp)