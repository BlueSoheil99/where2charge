# where2charge
_Course project for 'CSE583 Software Development for Data Scientists' during the autumn 2024 quarter at the University of Washington._

_Team members: Arsalan Esmaili, Soheil Keshavarz_

## Description: 

`where2charge` is a platform that is aimed to suggest reliable charging station options to EV owners.

This repository contains four main components as below:
- User interface (app.py) 

- Server handler (server.py)

- Control logic (recommender.py)

- Unit tests 

More information on user requirements, component design, structure of this work, and future work
can be seen at `doc/README.md` and `doc/CSE583 where2charge presentation.pptx`



## How to use
This project can be used in three ways: as a web application, as an API, and as a python package. 

Before using our codes, you need to have:

1. A valid Google API key (https://developers.google.com/maps) with access to Places, Distance Matrix, 
and Directions APIs.
2. A valid OpenAI API key (https://platform.openai.com/api-keys)
### Streamlit based web app
1. Update `config.yaml` file with your api keys
```angular2html
GOOGLE_API_KEY: "your_google_api_key"
OpenAI_API_KEY: "your_openai_api_key"
```
2. run `src/main.py` from root directory of this repo.

**TODO: screenshot** 
### API
in case you want to use this work directly as an api instead of a UI.

```angular2html

```
**TODO: screenshot** 

### a Python package

```angular2html
pip install where2charge
```
Sample code:
```angular2html
import where2charge

google_key = 'your_google_api_key'
openai_key = 'your_openai_api_key'

lat, lng = selected_latitude, selected_longitude
connector_type = 'Tesla'
number_of_suggestions = 3

recommender = where2charge.Recommender(google_key, openai_key)
suggestions = recommender.get_suggestions(lat, lng, number_of_suggestions, connector_type)
```