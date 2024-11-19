from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import re
import os

# Flask 앱 초기화
app = Flask(__name__, static_folder="static", template_folder="templates")

# 모델 로드
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# URL 전처리 함수
def extract_features(url):
    url_length = len(url)
    special_char_count = len(re.findall(r'[!#@%\-_]', url))
    specific_words = ['login', 'admin', 'confirm', '.exe', '000webhost', 'secure', 'account', 'update', 'verify']
    contains_specific_word = any(word in url for word in specific_words)
    num_digits = sum(c.isdigit() for c in url)
    digit_ratio = num_digits / len(url) if len(url) > 0 else 0
    contains_at_symbol_domain = int('@' in url and re.search(r'@[\\w.-]+', url) is not None)
    path_length = len(re.findall(r'/[\\w.-]+', url))
    query_length = len(re.findall(r'\\?.+', url))
    ngrams = re.findall(r'..', url)
    ngram_count = len(ngrams)

    return [
        url_length, special_char_count, int(contains_specific_word), digit_ratio,
        contains_at_symbol_domain, path_length, query_length, ngram_count
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
            'contains_at_symbol_domain', 'path_length', 'query_length', 'ngram_count'
        ]
        processed_input_df = pd.DataFrame([processed_input], columns=feature_names)

        # 모델 예측
        prediction = model.predict(processed_input_df)
        result = "Malicious" if prediction[0] == "malicious" else "Safe"

        return jsonify({"prediction": result})
    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({"error": "Prediction failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
