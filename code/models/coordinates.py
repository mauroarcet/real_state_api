from db import db
from sqlalchemy.orm import relationship


class CoordinatesModel(db.Model):
    __tablename__ = "coordinates"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    real_state_id = db.Column(db.Integer, db.ForeignKey("real_states.id"))
    real_state = db.relationship(
        "RealStateModel", back_populates="coordinates", foreign_keys=[real_state_id]
    )

    @classmethod
    def find_by_real_state_id(cls, real_state_id: int) -> "CoordinatesModel":
        return cls.query.filter_by(real_state_id=real_state_id).first()
