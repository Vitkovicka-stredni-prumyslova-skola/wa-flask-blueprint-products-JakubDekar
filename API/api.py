from flask import Blueprint, render_template
import requests

import json


api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static')
URL_API = "https://fakestoreapi.com"


def GetAllProducts():   
    
    request = requests.get(f"{URL_API}/products")
    
    return json.loads(request.text)


def GetSingleProducts(id):   
    
    request = requests.get(f"{URL_API}/products/" + str(id))
    
    return json.loads(request.text)
 
def GetRelatedProducts(category):
        request = requests.get(f"{URL_API}/products/category/{category}")
        products = json.loads(request.text)
        return products[:4]

