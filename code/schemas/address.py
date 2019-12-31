from ma import ma
from models.address import AddressModel


class AddressSchema(ma.ModelSchema):
    class Meta:
        load_only = ("real_state", "real_state_id", "id")
        model = AddressModel
        include_fk = True
