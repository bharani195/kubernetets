from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def load_products():
	df = pd.read_csv("products.csv")
	return df.to_dict(orient="records")


@app.route("/products",methods=["GET"])
def get_products():
	products = load_products()
	return jsonify(products)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

