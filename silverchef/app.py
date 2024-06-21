#silver chef 백엔드
from flask import Flask, request, jsonify, render_template, url_for
from googletrans import Translator
import requests

# flask 어플리케이션 생성
app = Flask(__name__)
translator = Translator()

# '/' 경로로 접근시 호출되는 함수, html 템플릿을 렌더링함
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate_and_search')
def translate_and_search_api():
    recipe_name_ko = request.args.get('recipe_name_ko')
    if recipe_name_ko:
        # 한국어로 입력받은 레시피 이름을 영어로 번역함
        recipe_name_en = translator.translate(recipe_name_ko, src='ko', dest='en').text
        return jsonify(get_top_5_recipes(recipe_name_en))
    return jsonify({'recipes': []})

# 주어진 레시피 이름으로 상위 5개의 레시피를 검색하는 함수
def get_top_5_recipes(recipe_name):
    api_url = "https://api.edamam.com/search"
    app_id = "enter your app id"
    app_key = "enter your app key"

    # api 요청에 필요한 변수 설정
    params = {
        "q": recipe_name,
        "app_id": app_id,
        "app_key": app_key,
        "from": 0,
        "to": 5,
    }

    # api에 get 요청
    response = requests.get(api_url, params=params)
    data = response.json()

    # 검색 결과에서 레시피 정보 추출
    recipes = []
    if "hits" in data and data["hits"]:
        for hit in data["hits"]:
            recipe = hit["recipe"]
            # 레시피 이름 한국어로 번역
            recipe_label_ko = translator.translate(recipe["label"], src='en', dest='ko').text
            recipes.append({
                "label": recipe_label_ko,
                "url": recipe["url"],
                "image": recipe["image"]
            })
    return {"recipes": recipes}

# 어플리케이션 시작
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
