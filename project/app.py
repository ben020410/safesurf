from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import re
import os
from urllib.parse import urlparse

# Flask 앱 초기화
app = Flask(__name__, static_folder="static", template_folder="templates")

# 모델 로드
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# URL 전처리 함수
def extract_features(url):
    # Feature 1: URL 길이
    url_length = len(url)
    # Feature 2: 특정 특수문자 개수 (!, #, @, %, - 등)
    special_char_count = len(re.findall(r'[!@#$%^&*()_+\-=[\]{};\':",.<>/?~\|]', url))
    # Feature 3: 특정 단어 포함 여부 (login, admin, confirm, .exe, 000webhost 등)
    specific_words = ['login', 'admin', 'confirm', '.exe', '000webhost', 'secure', 'account', 'update', 'verify']
    contains_specific_word = any(word in url for word in specific_words)
    # Feature 4: 숫자 구성 비율
    num_digits = sum(c.isdigit() for c in url)
    digit_ratio = num_digits / len(url) if len(url) > 0 else 0
    # Feature 5: @ 기호 이후 도메인 여부
    contains_at_symbol_domain = int('@' in url and re.search(r'@[\\w.-]+', url) is not None)
    # Feature 6: Path 및 Query String 길이
    path_length = len(re.findall(r'/[\\w.-]+', url))
    query_length = len(re.findall(r'\\?.+', url))
    # Feature 7: N-gram 특질 (bigram)
    ngrams = re.findall(r'..', url)
    ngram_count = len(ngrams)
    # Feature 8: www 포함여부
    parsed_url = urlparse(url)
    contains_www = 'www' in parsed_url.netloc
     # Feature 9: https 여부
    parsed_url = urlparse(url)
    if parsed_url.scheme == 'http':
        ssl= 1  # HTTP는 피싱 사이트로 간주
    elif parsed_url.scheme == 'https':
        ssl= 0  # HTTPS는 정상 사이트로 간주
    else:
        ssl= -1  # 비정상적인 경우

    return [
        url_length, special_char_count, int(contains_specific_word), digit_ratio,
        contains_at_symbol_domain, path_length, query_length, ngram_count, contains_www, ssl
    ]

# 홈페이지 라우트
@app.route("/")
def home():
    return render_template("index.html")

# 예측 API 라우트
@app.route("/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    link = data.get("link")

    if not link:
        return jsonify({"error": "No link provided"}), 400

    try:
        # URL 전처리
        processed_input = extract_features(link)
        
        # 피처 이름을 포함한 DataFrame으로 변환
        feature_names = [
            'url_length', 'special_char_count', 'contains_specific_word', 'digit_ratio',
            'contains_at_symbol_domain', 'path_length', 'query_length', 'ngram_count', 'has_www', 'ssl'
        ]
        processed_input_df = pd.DataFrame([processed_input], columns=feature_names)

        # 모델 예측
        prediction = model.predict(processed_input_df)
        result = "Safe" if prediction[0] == "benign" else "Malicious"

        return jsonify({"prediction": result})
    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({"error": "Prediction failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
