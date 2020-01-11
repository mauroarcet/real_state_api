# Real State API

A basic API written in Flask, it handles the administration of real state properties.

## Tech Stack

The real state API is a Flask application that communicates to an RDS with a Postgresql database.
SQLAlchemy is used as ORM to handle the communication with the database.
Marshmallow is used to serialize the data handled on the application.

Endpoints:

GET
/real_states

POST
/real_state

GET, PUT, DELETE
/real_state/id

Url To Test:
http://elb-true-home-416357538.us-east-2.elb.amazonaws.com
