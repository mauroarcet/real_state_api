from ma import ma
from models.address import AddressModel
from models.real_state import RealStateModel
from schemas.address import AddressSchema
from schemas.coordinates import CoordinatesSchema


class RealStateSchema(ma.ModelSchema):
    address = ma.List(ma.Nested(AddressSchema))
    coordinates = ma.List(ma.Nested(CoordinatesSchema))

    class Meta:
        model = RealStateModel
        load_only = ("approval_state", "real_state_id")
        dump_only = ("id", "created_at")
        include_fk = True
