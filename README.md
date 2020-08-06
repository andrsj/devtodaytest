# Challenge code for DevelopsToday

## Overview
 News site API:
 - CRUD posts
 - CRUD comments for posts
 - Endpoint to upvote the post
 - X Background tasks unrealised

## How to run server

```
git clone
virtualenv -p=python3.8 .env
source .env/bin/activate
pip install -r requirements.txt
docker-compose up --build
python manage.py migrate
python manage.py runserver
```


## Checked code 
 Using with:
 - PyCharmIDE 
 - Black [pip install black]
 - Flake8 [pip install flake8]
 (warning on the number of characters in one line is omitted
 in black we can use <88 symbols, on flack8 <79)

### Postman Collection
 - [JSON format](https://www.getpostman.com/collections/46ec6676250af3d0c926)
 - [Web format](https://interstellar-resonance-7867-1.postman.co/collections/10917899-9e03aa1a-3a31-44a1-869b-365f63faf870?workspace=cc6abddb-77bb-4dc1-84d4-f59961809a48)

