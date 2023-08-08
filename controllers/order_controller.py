
# from app.py import app
# from app import *
# import the Blueprint class from flask framework
from flask import Blueprint
# also import the render_template (template method) from flask
from flask import render_template
# import the order from orders list
from models.orders import orders

# create an Order Blueprint instance and call it orders. __name__ parameter initialises this
orders_blueprint = Blueprint("orders", __name__)

# Assign a URL route for the "/orders" web request coming into the App 
# using @app.route decorator
@orders_blueprint.route('/orders')

# Display what you want to display against that URL assignment using the render template 
# which passes index.html, a title for the page and the orders list
def index():
    return render_template("index.html", title="Baldwin's Books", orders=orders)

# Create a new route to display details about one particular order
@orders_blueprint.route('/orders/<order_number>')
def selected_order(order_number):
    order_detail = orders[int(order_number)]
    return render_template("order.html", title="Baldwin's Books", order_number=order_number, order=order_detail)
