# Questioner
Questioner API using Python Data Structures and Object oriented Programming   
[![Build Status](https://travis-ci.com/Ogutu-Brian/Questioner.svg?branch=develop)](https://travis-ci.com/Ogutu-Brian/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/Ogutu-Brian/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/Ogutu-Brian/Questioner?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/a09c24e8ea08899e153f/maintainability)](https://codeclimate.com/github/Ogutu-Brian/Questioner/maintainability)

## Project Overview
Questioner is an application used by meetup organizers to plan well for meetups and to prioritize what to discuss during the meetup.

## Required Features
1. A user should be able to sign up to Questioner 
2. A user with an account should be able to log into Questioner
3. An administrator should be able to crete a meetup in Questioner
4. A user with an account should be able to post Questions to specific meetups
5. A user should be able to post a question agains a specific meetup
6. A user should be able to get a specific meetup record
7. A user should be able to get all meetup recods
8. A user should be able to upvote or downvote a question
9. A user should be able to give an rsvp for a meetup

# Installation and Setup
Clone the repository.
```bash
git clone https://github.com/Ogutu-Brian/Questioner
```

## Create a virtual environment

```bash
$ python3 -m venv venv;
$ source venv/bin/activate
```
On Windows
```bash
py -3 -m venv venv
```
If you need to install virtualenv because you are on an older version of Python:
```bash
virtualenv venv
```
On Windows
```bash
\Python27\Scripts\virtualenv.exe venv
```

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```bash
source venv/bin/activate
```
On Windows
```bash
venv\Scripts\activate
```

## Install requirements
```bash
$ pip install -r requirements.txt
```

## Running the application
After the configuration, you will run the app 
```bash
$ cd app
$ export FLASK_APP=run.py
$ flask run
```

## Endpoints
All endpoints can be now accessed from the following url on your local computer
```
http://localhost:5000/api/v1/
```
Or from Heroku
```
https://quest-ioner.herokuapp.com/api/v1/
```

## Testing
After successfully installing the application, the endpoints can be tested by running.
```bash
pytest tests/*
```

## Available endpoints
| Method        |  Endpoint                                   |  Description                                           |
| ------------- |  -------------                              |  -------------                                         |
| `POST`        | `/api/v1/meetups`                           |  Creates a meetup record                               |
| `GET`         | `/api/v1/meetups/<meetup-id>`               |  Fetch a specific meetup record                        |
| `GET`         | `/api/v1/meetups/upcomng/`                  |  Fetch all upcoming meetup records                     |
| `POST`        | `/api/v1/questions`                         |  Create a question for a specific meetup               |
| `PATCH`       | `/api/v1/questions/<question-id>/upvote`    |  Upvotes a specific question                           |
| `PATCH`       | `/api/v1/questions/<question-id>/downvote`  |  Downvotest a specific question                        |
| `POST`        | `/api/v1/meetups/<meetup-id>/rsvps`         |  Responds to a meetup Rsvp                             |
| `POST`        | `/api/v1/users/sign-up`                     |  Creates a new user to Questioner                      |
| `POST`        | `/api/v1/users/log-in`                      |  Allows a user with an account to log in               |
# Resources and Documentation

### Pivotal Tracker Project
You can view the [Pivotal Tracker stories](https://www.pivotaltracker.com/n/projects/2235331)

### Research Materials   
1. [Deploying flask application in heroku](https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524)
2. [Flask](http://flask.pocoo.org/docs/1.0/)
