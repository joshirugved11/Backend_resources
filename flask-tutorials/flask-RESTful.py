from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = {}

class User(Resource):
    def get(self, name):
        return users.get(name, {"message": "User not found"})
    
    def post(self, name):
        users[name] = request.json
        return {"message": f"User {name} added"}

api.add_resource(User, "/user/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)
