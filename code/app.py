from flask import Flask

from flask_marshmallow import Marshmallow
from flask_restful import Api
from ma import ma
from resources.real_state import RealState, RealStateList

connection_string = (
    "postgresql"
    + "+psycopg2"
    + "://"
    + "postgres:"
    + "^kq55QAuIwr#"
    + "@real-state-dev-db.canrzxdvzoof.us-east-2.rds.amazonaws.com"
    + ":5432"
    + "/"
    + "realStateDb"
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "mau"
api = Api(app)

# Run first time in order to create the db to be used by the API
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(RealState, "/real_state", "/real_state/<string:id>")
api.add_resource(RealStateList, "/real_states")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
