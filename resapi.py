import argparse
import io
import requests
import torch
from PIL import Image
from flask import Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

run_with_ngrok(app)   #starts ngrok when the app is run

DETECTION_URL = "/v1/object-detection/yolov5s6"
DETECTION_URL_2 = "/v1/object-detection/yolov5m"

# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()

@app.route("/health_check")
def home():
    return """
<h1>It's Works. Running Flask on Google Colab!</h1>
<h6>request POST to this endpoint </h6>
<p>/v1/object-detection/yolov5s6 atau /v1/object-detection/yolov5m</p>
"""

# @app.route('/shutdown', methods=['GET'])
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'

@app.route(DETECTION_URL_2, methods=["POST"])
def predict2():

    if not request.method == "POST":
        return

    if request.values.get('size'):
        img_size = request.values.get('size', type=int)
    else:
        img_size = 640  # reduce size=320 for faster inference
    if request.values.get('conf'):
        model2.conf = request.values.get('conf', type=int) / 100
    else:
        model2.conf = 0.25
    if request.values.get('iou'):
        model2.iou = request.values.get('iou', type=int) / 100
    else:
        model2.iou = 0.45

    if request.form.get("image_url"):
        results = model2(request.form.get("image_url"), size=img_size)
        return results.pandas().xyxy[0].to_json(orient="records")

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()

        img = Image.open(io.BytesIO(image_bytes))

        results = model2(img, size=img_size)
        return results.pandas().xyxy[0].to_json(orient="records")

@app.route(DETECTION_URL, methods=["POST"])
def predict():

    if not request.method == "POST":
        return

    if request.values.get('size'):
        img_size = request.values.get('size', type=int)
    else:
        img_size = 640  # reduce size=320 for faster inference
    if request.values.get('conf'):
        model.conf = request.values.get('conf', type=int) / 100
    else:
        model.conf = 0.25
    if request.values.get('iou'):
        model.iou = request.values.get('iou', type=int) / 100
    else:
        model.iou = 0.45

    if request.form.get("image_url"):
        results = model(request.form.get("image_url"), size=img_size)
        return results.pandas().xyxy[0].to_json(orient="records")

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()

        img = Image.open(io.BytesIO(image_bytes))

        results = model(img, size=img_size)
        return results.pandas().xyxy[0].to_json(orient="records")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=4040, type=int, help="port number")
    args = parser.parse_args()
    
    model = torch.hub.load("ultralytics/yolov5", 
                              "custom", 
                              path="/content/YOLOv5s6_best_striped.pt", 
                              force_reload=True)

    model2 = torch.hub.load("ultralytics/yolov5", 
                              "custom", 
                              path="/content/YOLOv5m_300epoch_best.pt", 
                              force_reload=True)

    # app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
    app.run()  # debug=True causes Restarting with stat
