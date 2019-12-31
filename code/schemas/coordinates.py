from ma import ma
from models.coordinates import CoordinatesModel


class CoordinatesSchema(ma.ModelSchema):
    class Meta:
        load_only = ("real_state", "real_state_id", "id")
        model = CoordinatesModel
        include_fk = True
