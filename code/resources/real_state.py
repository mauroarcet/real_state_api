import json
import boto3

from flask import request

from flask_restful import Resource, reqparse
from marshmallow import ValidationError
from models.address import AddressModel
from models.coordinates import CoordinatesModel
from models.real_state import RealStateModel
from schemas.real_state import RealStateSchema

ERROR_INSERTING = "An error occurred while creating the Real State."
NOT_FOUND = "Real state not found."
DELETED = "Real state deleted."

real_state_schema = RealStateSchema()
real_state_list_schema = RealStateSchema(many=True)


class RealState(Resource):
    @classmethod
    def get(cls, id):
        real_state = RealStateModel.find_by_id(id)
        if real_state:
            return real_state_schema.dump(real_state), 200

        return {"message": NOT_FOUND}, 404

    @classmethod
    def post(cls):
        real_state_request = json.dumps(request.get_json())
        real_state = real_state_schema.loads(real_state_request)

        try:
            real_state.save_to_db()
            lambda_client = boto3.client('lambda')
            lambda_client.invoke(
                FunctionName='dataAnalysis',
                InvocationType='Event',
                Payload=''
            )
        except:
            return {"message": ERROR_INSERTING}, 500

        return real_state_schema.dump(real_state), 201

    @classmethod
    def delete(cls, id):
        real_state = RealStateModel.find_by_id(id)
        if real_state:
            real_state.delete_from_db()

        return {"message": DELETED}

    @classmethod
    def put(cls, id):
        real_state_request = request.get_json()
        real_state = RealStateModel.find_by_id(id)
        address = AddressModel.find_by_real_state_id(id)
        coordinates = CoordinatesModel.find_by_real_state_id(id)

        if real_state:
            address = real_state_request["address"]
            coordinates = real_state_request["coordinates"]
            real_state.commercial_description = real_state_request[
                "commercial_description"
            ]
            real_state.gallery = real_state_request["gallery"]
            real_state.name = real_state_request["name"]
            real_state.price = real_state_request["price"]

            try:
                real_state = real_state_schema.load(real_state_request)
            except ValidationError as err:
                return err.messages, 400

        real_state.save_to_db()
        invoke_lambda()

        return real_state_schema.dump(real_state), 200

    @classmethod
    def invoke_lambda(cls):
        lambda_client = boto3.client('lambda')
        lambda_client.invoke(
            FunctionName='dataAnalysis',
            InvocationType='Event',
            Payload=''
        )    


class RealStateList(Resource):
    @classmethod
    def get(cls):
        return (
            {"real_states": real_state_list_schema.dump(
                RealStateModel.find_all())},
            200,
        )
