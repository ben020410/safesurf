from flask import Flask, request, jsonify, render_template
import pickle

# Flask 앱 초기화
app = Flask(__name__)

# 학습된 모델 로드 (모델이 pickle 형식으로 저장되었다고 가정)
with open("./project/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# 홈페이지 라우트
@app.route("/")
def home():
    return render_template("index.html")

# 예측 API 라우트
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # 프론트엔드에서 받은 JSON 데이터
    link = data.get("link")

    # 모델 예측 (여기서는 간단하게 가정한 예측)
    # 악성 코드 여부를 예측하는 함수
    prediction = model.predict([link])  # 모델에 링크 입력
    result = "Malicious" if prediction[0] == 1 else "Safe"

    # 결과 반환
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
