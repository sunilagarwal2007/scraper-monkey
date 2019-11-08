from flask import Flask, render_template,  jsonify

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
# conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)

rds_connection_string = "postgres:Infy123+@localhost:5432/Product_PriceDB"
engine = create_engine(f'postgresql://{rds_connection_string}')
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
# Product_Price = Base.classes.product_price

session = Session(engine)


# Connect to a database. Will create one if not already available.
# db = client.team_db

# Drops collection if available to remove duplicates
# db.team.drop()

# Creates a collection in the database and inserts two documents
# db.team.insert_many(
#     [
#         {
#             'player': 'Jessica',
#             'position': 'Point Guard'
#         },
#         {
#             'player': 'Mark',
#             'position': 'Center'
#         }
#     ]
# )



# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    
    # pd.read_sql_query('select * from product_price', con=engine).head()

    
    # products = session.query(Product_Price.product_name, Product_Price.product_price).all()

    # products = session.query(Product_Price.product_name, Product_Price.product_price).all()

    products = engine.execute('SELECT product_name,best_buy,Amazon,product_model,product_price, product_image,product_url FROM product_price LIMIT 13').fetchall()

    		

    # Convert list of tuples into normal list
    all_names = list(np.ravel(products))

    # return jsonify(all_names)

    # teams = list(db.team.find())
    # print(engine.table_names())

    # Return the template with the teams list passed in
    return render_template('index.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)
