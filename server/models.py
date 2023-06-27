from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from flask import Flask 

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Audio2Text(db.Model, SerializerMixin):
    __tablename__ = 'audio2texts'

    id = db.Column(db.Integer, primary_key=True)
    audio_file_path = db.Column(db.String(500), unique=True, nullable=False)
    transcript_text = db.Column(db.Text, unique=False, nullable=False)

    def __repr__(self):
        return f"Audio2Text # {self.id}: {self.audio_file_path}"


class Text2Text(db.Model, SerializerMixin):
    __tablename__ = 'text2texts'

    id = db.Column(db.Integer, primary_key=True)
    transcript_text = db.Column(db.Text, nullable=False)
    prompt = db.Column(db.Text)
    response = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Text2Text # {self.id}: {self.prompt}"


class Text2Image(db.Model, SerializerMixin):
    __tablename__ = 'text2images'

    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String)

    def __repr__(self):
        return f"Text2Image # {self.id}: {self.prompt}"



""" 
class Audio2Text(db.Model, SerializerMixin):
    __tablename__ = 'audio2texts'

    id = db.Column(db.Integer, primary_key=True)
    audio_file_path = db.Column(db.String, nullable=False)
    transcript_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Audio2Text # {self.id}: {self.audio_file_path}"

class Text2Text(db.Model, SerializerMixin):
    __tablename__ = 'text2texts'

    id = db.Column(db.Integer, primary_key=True)
    transcript_text = db.Column(db.Text, nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Text2Text # {self.id}: {self.prompt}"

class Text2Image(db.Model, SerializerMixin):
    __tablename__ = 'text2images'

    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Text2Image # {self.id}: {self.prompt}"
""" 
"""

class Hotel(db.Model, SerializerMixin):
    __tablename__ = 'hotels'

    serialize_rules = ('-reviews',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    image = db.Column(db.String, nullable=False)

    reviews = db.relationship('Review', back_populates='hotel')

    customers = association_proxy('reviews', 'customer',
        creator=lambda c: Review(customer=c))

    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 5:
            raise ValueError(f"{key} must be at least 5 characters long.")
        return value
    
    def __repr__(self):
        return f"Hotel # {self.id}: {self.name} hotel"

class Text2Text(db.Model, SerializerMixin):
    __tablename__ = 'Text2Texts'

    serialize_rules = ('-reviews',)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    reviews = db.relationship('Review', back_populates='customer')

    hotels = association_proxy('reviews', 'hotel',
        creator=lambda h: Review(hotel=h))

    __table_args__ = (
        db.CheckConstraint('(first_name != last_name)'),
    )

    @validates('first_name', 'last_name')
    def validate_first_name(self, key, value):
        if value is None:
            raise ValueError(f"{key} cannot be null.")
        elif len(value) < 4:
            raise ValueError(f"{key} must be at least 4 characters long.")
        return value
    
    def __repr__(self):
        return f"Customer # {self.id}: {self.first_name} {self.last_name}"
    
class Text2Image(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    serialize_rules = ('-reviews',)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    reviews = db.relationship('Review', back_populates='customer')

    hotels = association_proxy('reviews', 'hotel',
        creator=lambda h: Review(hotel=h))

    __table_args__ = (
        db.CheckConstraint('(first_name != last_name)'),
    )

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    serialize_rules = ('-hotel.reviews', '-customer.reviews')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    hotel = db.relationship('Hotel', back_populates='reviews')
    customer = db.relationship('Customer', back_populates='reviews')

    def __repr__(self):
        return f"Review # {self.id}: {self.customer.first_name} {self.customer.last_name} left of a review for {self.hotel.name} with a rating of {self.rating}."

"""
