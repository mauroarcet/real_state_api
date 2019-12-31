from db import db
from sqlalchemy.orm import relationship


class AddressModel(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(120))
    zip_code = db.Column(db.String(10))
    real_state_id = db.Column(db.Integer, db.ForeignKey("real_states.id"))
    real_state = db.relationship(
        "RealStateModel", back_populates="address", foreign_keys=[real_state_id]
    )

    @classmethod
    def find_by_real_state_id(cls, real_state_id: int) -> "AddressModel":
        return cls.query.filter_by(real_state_id=real_state_id).first()
