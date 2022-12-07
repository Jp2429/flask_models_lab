from flask import render_template
from app import app
from models.order_list import games

@app.route('/orders')
def index():
    return render_template('index.html', title="Game Shop", games=games)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', title="Order", index = index, games=games)
