from flask import Flask, request, jsonify, render_template, url_for
from googletrans import Translator
import requests

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate_and_search')
def translate_and_search_api():
    recipe_name_ko = request.args.get('recipe_name_ko')
    if recipe_name_ko:
        recipe_name_en = translator.translate(recipe_name_ko, src='ko', dest='en').text
        return jsonify(get_top_5_recipes(recipe_name_en))
    return jsonify({'recipes': []})

def get_top_5_recipes(recipe_name):
    api_url = "https://api.edamam.com/search"
    app_id = "3fb51f64"
    app_key = "95d50643632f0c49d6d2ab3d5a2068d2"

    params = {
        "q": recipe_name,
        "app_id": app_id,
        "app_key": app_key,
        "from": 0,
        "to": 5,
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    recipes = []
    if "hits" in data and data["hits"]:
        for hit in data["hits"]:
            recipe = hit["recipe"]
            recipes.append({
                "label": recipe["label"],
                "url": recipe["url"],
                "image": recipe["image"]
            })
    return {"recipes": recipes}

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)