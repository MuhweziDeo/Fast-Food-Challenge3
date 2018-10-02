from flask import request
from flask_restful import Resource
from app.models.validate import VerifyMenu, VerifyToken
from app.models.menu import Menu
from app.models.db_actions import MenuDbQueries

class GetMenu(Resource):
    def get(self):
        auth_token = request.headers["Authentication"]
        user_info = VerifyToken.validate(auth_token)
        if user_info:
            response = MenuDbQueries().fetch_all_menu()
            if response:
                return{"response": response}
            return {"response":"no menu"}
        return{"response":"Not Authenticated"}
    