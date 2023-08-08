# create order app to display list of orders on a webpage. 

# Import Flask class from flask framework
from flask import Flask

# Import Order blueprint from Blueprint instance created in the controller file
from controllers.order_controller import orders_blueprint

# Import Orders list created in the order_list file
# from order_list import orders

# Create Order Flask App instance from Flask class
order_app = Flask(__name__)

# Register the order blueprint against the Order Flask App
order_app.register_blueprint(orders_blueprint)

