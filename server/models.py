from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from flask import Flask

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Audio(db.Model, SerializerMixin):
    __tablename__ = 'audios'
    id = db.Column(db.Integer, primary_key=True)
    audio_data = db.Column(db.LargeBinary)

    def to_dict(self):
        return {
            'id': self.id,
            'audio_data': self.audio_data.decode(),
            'name': self.name
        }


    
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    def __repr__(self):
        return f"Audio # {self.id}"
    

class Audio2Text(db.Model, SerializerMixin):
    __tablename__ = 'audio2texts'

    id = db.Column(db.Integer, primary_key=True)
    audio_file_path = db.Column(db.String(500), unique=False, nullable=True)
    transcript_text = db.Column(db.Text, unique=False, nullable=True)
    # keywords = db.Column(db.Text, unique=False, nullable=True)
    # sentiment = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f"Audio2Text # {self.id}: {self.audio_file_path}"


class Text2Text(db.Model, SerializerMixin):
    __tablename__ = 'text2texts'

    id = db.Column(db.Integer, primary_key=True)
    transcript_text = db.Column(db.Text, nullable=True)
    prompt = db.Column(db.Text, nullable=True)
    response = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Text2Text # {self.id}: {self.prompt}"


class Text2Image(db.Model, SerializerMixin):
    __tablename__ = 'text2images'

    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, nullable=True)
    image_path = db.Column(db.String, nullable=True)
