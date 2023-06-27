#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Audio2Text, Text2Text, Text2Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app) 

# Routes for Audio2Text model
@app.route('/audio2texts', methods=['GET'])
def get_audio2texts():
    audio2texts = Audio2Text.query.all()
    return jsonify([audio2text.to_dict() for audio2text in audio2texts])


@app.route('/audio2texts', methods=['POST'])
def create_audio2text():
    data = request.get_json()
    audio2text = Audio2Text(**data)
    db.session.add(audio2text)
    db.session.commit()
    return jsonify(audio2text.to_dict()), 201


@app.route('/audio2texts/<int:audio2text_id>', methods=['GET'])
def get_audio2text(audio2text_id):
    audio2text = Audio2Text.query.get(audio2text_id)
    if audio2text:
        return jsonify(audio2text.to_dict())
    return jsonify({'message': 'Audio2Text not found'}), 404


@app.route('/audio2texts/<int:audio2text_id>', methods=['PATCH'])
def update_audio2text(audio2text_id):
    audio2text = Audio2Text.query.get(audio2text_id)
    if not audio2text:
        return jsonify({'message': 'Audio2Text not found'}), 404

    data = request.get_json()
    audio2text.audio_file_path = data.get('audio_file_path', audio2text.audio_file_path)
    audio2text.transcript_text = data.get('transcript_text', audio2text.transcript_text)
    db.session.commit()
    return jsonify(audio2text.to_dict())


@app.route('/audio2texts/<int:audio2text_id>', methods=['DELETE'])
def delete_audio2text(audio2text_id):
    audio2text = Audio2Text.query.get(audio2text_id)
    if audio2text:
        db.session.delete(audio2text)
        db.session.commit()
        return jsonify({'message': 'Audio2Text deleted'})
    return jsonify({'message': 'Audio2Text not found'}), 404


# Routes for Text2Text model
@app.route('/text2texts', methods=['GET'])
def get_text2texts():
    text2texts = Text2Text.query.all()
    return jsonify([text2text.to_dict() for text2text in text2texts])


# Add routes for POST, GET by ID, PATCH, and DELETE for Text2Text model similar to Audio2Text model

# Routes for Text2Image model
@app.route('/text2images', methods=['GET'])
def get_text2images():
    text2images = Text2Image.query.all()
    return jsonify([text2image.to_dict() for text2image in text2images])


# Add routes for POST, GET by ID, PATCH, and DELETE for Text2Image model similar to Audio2Text model


if __name__ == '__main__':
    app.run()
# CORS(app)

""" 
api = Api(app)

class Hotels(Resource):

    def get(self):
        hotels = Hotel.query.all()

        response_body = []

        for hotel in hotels:
            response_body.append(hotel.to_dict())

        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            new_hotel = Hotel(name=request.get_json().get('name'), image=request.get_json().get('image'))
            db.session.add(new_hotel)
            db.session.commit()

            response_body = new_hotel.to_dict()
            
            return make_response(jsonify(response_body), 201)
        except ValueError as error:
            response_body = {
                "error": error.args
            }
            return make_response(jsonify(response_body), 422)


api.add_resource(Hotels, '/hotels')

class HotelById(Resource):

    def get(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()

        if not hotel:
            response_body = {
                "error": "Hotel not found"
            }
            status = 404

        else:
            response_body = hotel.to_dict()
            customer_list = []
            for customer in list(set(hotel.customers)):
                customer_list.append({
                    "id": customer.id,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name
                })
            response_body.update({"customers": customer_list})
            status = 200

        return make_response(jsonify(response_body), status)
    
    def patch(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()

        if not hotel:
            response_body = {
                "error": "Hotel not found"
            }
            return make_response(jsonify(response_body), 404)

        else:
            try:
                json_data = request.get_json()
                for key in json_data:
                    setattr(hotel, key, json_data.get(key))
                db.session.commit()

                response_body = hotel.to_dict()
                return make_response(jsonify(response_body), 200)
            
            except ValueError as error:
                
                response_body = {
                    "error": error.args
                }
                
                return make_response(jsonify(response_body), 422)
    
    def delete(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()

        if not hotel:
            response_body = {
                "error": "Hotel not found"
            }
            status = 404

        else:
            db.session.delete(hotel)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)


api.add_resource(HotelById, '/hotels/<int:id>')

class Customers(Resource):

    def get(self):
        customers = Customer.query.all()

        response_body = []
        for customer in customers:
            response_body.append(customer.to_dict())
        
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        try:
            new_customer = Customer(first_name=request.get_json().get('first_name'), last_name=request.get_json().get('last_name'))

            db.session.add(new_customer)
            db.session.commit()
            
            return make_response(jsonify(new_customer.to_dict()), 201)
        except ValueError as error:
            response_body = {
                "error": error.args
            }
            return make_response(jsonify(response_body), 422)

api.add_resource(Customers, '/customers')

class CustomerById(Resource):

    def get(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if not customer:
            response_body = {
                "error": "Customer not found"
            }
            status = 404
        else:
            response_body = customer.to_dict()
            status = 200

        return make_response(jsonify(response_body), status)
    
    def patch(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if not customer:
            response_body = {
                "error": "Customer not found"
            }
            return make_response(jsonify(response_body), 404)
        else:
            try:
                json_data = request.get_json()
                
                for key in json_data:
                    setattr(customer, key, json_data.get(key))

                db.session.commit()

                response_body = customer.to_dict()

                return make_response(jsonify(response_body), 200)
            except ValueError as error:
                response_body = {
                    "error": error.args
                }
                return make_response(jsonify(response_body), 422)
    
    def delete(self, id):
        customer = Customer.query.filter(Customer.id == id).first()
        
        if not customer:

            response_body = {
                "error": "Customer not found"
            }
            status = 404
        
        else:
            
            db.session.delete(customer)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)

api.add_resource(CustomerById, '/customers/<int:id>')

class Reviews(Resource):

    def get(self):
        reviews = Review.query.all()

        response_body = []

        for review in reviews:
            response_body.append(review.to_dict())

        return make_response(jsonify(response_body), 200)
    
    def post(self):
        json_data = request.get_json()
        new_review = Review(hotel_id=json_data.get('hotel_id'), customer_id=json_data.get('customer_id'), rating=json_data.get('rating'))
        db.session.add(new_review)
        db.session.commit()

        response_body = new_review.to_dict()
        
        return make_response(jsonify(response_body), 201)
    
api.add_resource(Reviews, '/reviews')

class ReviewById(Resource):

    def get(self, id):
        review = Review.query.filter(Review.id == id).first()

        if not review:
            response_body = {
                "error": "Review not found"
            }
            status = 404
        else:
            response_body = review.to_dict()
            status = 200

        return make_response(jsonify(response_body), status)
    
    def patch(self, id):
        review = Review.query.filter(Review.id == id).first()

        if not review:
            response_body = {
                "error": "Review not found"
            }
            status = 404
        else:
            json_data = request.get_json()

            for key in json_data:
                setattr(review, key, json_data.get(key))

            db.session.commit()

            response_body = review.to_dict()
            status = 200

        return make_response(jsonify(response_body), status)
    
    def delete(self, id):
        review = Review.query.filter(Review.id == id).first()
        
        if not review:

            response_body = {
                "error": "Review not found"
            }
            status = 404
        
        else:
            
            db.session.delete(review)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)

api.add_resource(ReviewById, '/reviews/<int:id>')

if __name__ == '__main__':
    app.run(port=7000, debug=True)
    """