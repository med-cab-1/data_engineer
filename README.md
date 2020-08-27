# Med Cabinet

- [Big picture](#big-picture)
- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
- [File structure](#file-structure)
- [More instructions](#more-instructions)
- [Deploying to Heroku](#deploying-to-heroku)

## Big picture
Our goal in this project was to create a medical Cannabis recommendation API. This would receive form input and
send it through a Machine Learning model and would result in a strain of Cannabis best fit to their desired inputs. 


We utilized FastAPI in order to get our app outputting the correct JSON object for our Web counterparts. The similarities
it has to Flask API made it easy for us to understand along with this resource

[Fast API for Flask Users ](https://amitness.com/2020/06/fastapi-vs-flask/)


![](https://user-images.githubusercontent.com/7278219/87967579-a4f16a00-ca84-11ea-9f90-886b3cf1a25c.png)

## Tech stack
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Heroku](https://devcenter.heroku.com/): Platform as a service, hosts your API.
- [Pipenv](https://pipenv.pypa.io/en/latest/): Reproducible virtual environment, manages dependencies.
- [Spacy](https://spacy.io/api/doc): For Natural Language Processing
- [Pandas](): Exploratory Data analysis and data conversion to SQLite3
- [Scikit Learn](): Model Creation and Machine Learning
- [Python](): 3.7 was used for this project


## Getting started

Clone the repo
```
git clone https://github.com/med-cab-1/data_engineer

cd NEW-REPO-NAME
```


## Opening in your environment

Install dependencies
```
pipenv install -r requirements.txt 
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
uvicorn app.main:app --reload
```

Go to `localhost:8000` in your browser.
- Here you can interact with the interactive documentation and test the prediction model, starting with a fixed prediction
can be helpful to make sure the responses are in order. 


### Deploying to Heroku

Prepare Heroku
```
heroku login

heroku create YOUR-APP-NAME-GOES-HERE

heroku git:remote -a YOUR-APP-NAME-GOES-HERE
```

Deploy to Heroku

```
git add *

git commit -m "Deploy to Heroku"

git push heroku
```
Opening your newly created app on the Cloud
```
heroku open
```
