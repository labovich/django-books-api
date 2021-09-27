# Django books api

Simple django application implement a REST API and 2 permission levels for users.

Administrators can create/update items, other users can only read items.

## Running

Create on folder /app file `.env` used `env-example`.

Run `docker-compose up -d`.

For create superuser use command `docker-compose exec app pipenv run python ./manage.py createsuperuser`

You can create other users using the django admin panel using url `http://127.0.0.1:8000/admin/`

## Authentication

You can use JWT tokens for Authentication. Url to get a token `http://127.0.0.1:8000/api/token/`

## Github oAuth

For use Github oAuth for Authentication you need register a new application at GitHub Developers, 
set the callback URL like `http://127.0.0.1:8000/social/complete/github/`. 
This will generate a Client Key and a Client Secret. 
Set Client Key as `SOCIAL_AUTH_GITHUB_KEY` and Client Secret as `SOCIAL_AUTH_GITHUB_SECRET` on `.env` file.
For login you can use url `http://127.0.0.1:8000/social/login/github/`.


## Tests

For running tests use command `docker-compose exec app pipenv run pytest`


## Swagger

Swagger available on the url `http://127.0.0.1:8000/swagger/`

## Postman

Postman collections available on the folder `postman`