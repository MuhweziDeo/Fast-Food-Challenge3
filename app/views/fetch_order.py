from flask import request
from flask_restful import Resource
from app.models.validate import VerifyOrders, VerifyToken
from app.models.orders import Orders
from app.models.db_actions import OrderDbQueries

class FetchSpecificOrder(Resource):
    def get(self, order_id):
        auth_token = request.headers["Authentication"]
        user_info = VerifyToken.validate(auth_token)
        if user_info:
            if user_info["user_role"] == "admin":
                response = OrderDbQueries().fetch_order_byId(int(order_id))
                return {"response":response}
            return {"response":" only admins access this resource"}
        return {"response":"not authenticated"}
     