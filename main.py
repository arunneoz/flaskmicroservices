import flask
from flask import request, jsonify
import json
import logging


app = flask.Flask(__name__)


cartresult = [

{
    'status': 'success',
    'message': 'successfully added items to cart'

}
]


products = [
    {'id': 0,
     'name': '3/4" FNPT BRONZE DUAL CHECK VALVE',
     'slug': 'DETAILS: Length: 4-1/16" Item: Dual Check w Atmospheric Vent Standards: ASSE 1012, CSA B64.3 Certified',
     'price': '44.99',
     'quantity': '10',
     'imageurl': 'https://ecomm-frontend-dot-inbound-rune-devops-gke.appspot.com/media/products/2018/08/16/brassvalve.JPG'},
    {'id': 0,
     'name': 'CLIPBOARD, LETTER, LIGHT BROWN, PK2',
     'slug': 'DETAILS: Height: 12-1/2" Green Certification or Other Recognition: Carbon Free Certified Sheet Size: 8-1/2 x 11"',
     'price': '3.47',
     'quantity': '10',
     'imageurl': 'https://ecomm-frontend-dot-inbound-rune-devops-gke.appspot.com/media/products/2018/08/16/clipboard.JPG'}

]

def add2cart(item , qty):

  logging.info("Received Cart Items name %s  quantity %s",item,qty);

  cartresult[0]['message'] = "successfully added "+ item + " to cart"

  return jsonify(cartresult)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>MicroServices Engine is Up</h1>
<p>A prototype API for showcasing Microservices using Flask.</p>'''


@app.route('git init', methods=['GET'])
def api_product_all():
    return jsonify(products)


@app.route('/api/v2/resources/shop/addtocart', methods=['POST'])
def api_add2cart():
   content = request.get_json()
   return add2cart(content['name'],content['quantity'])



if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)