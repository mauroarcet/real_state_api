import datetime

from db import db
from sqlalchemy.sql import func
from typing import List

from models.helper import get_timestamp


class RealStateModel(db.Model):
    __tablename__ = "real_states"

    id = db.Column(db.Integer, primary_key=True)
    address = db.relationship(
        "AddressModel",
        order_by="AddressModel.id",
        back_populates="real_state",
        lazy="dynamic",
    )
    approval_state = db.Column(db.Boolean())
    commercial_description = db.Column(db.String(300))
    coordinates = db.relationship(
        "CoordinatesModel",
        order_by="CoordinatesModel.id",
        back_populates="real_state",
        lazy="dynamic",
    )
    created_at = db.Column(db.String(10), default=get_timestamp())
    gallery = db.Column(db.String(200))
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=3))

    @classmethod
    def find_by_id(cls, id: int) -> "RealStateModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["RealStateModel"]:
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        