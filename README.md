# nutrifit-ml
ML repository for Nutrifit project. The ML part of Nutrifit project is detect 15 food categories.

## 15 food category:
1. beef curry
2. chicken nugget
3. french fries
4. green salad
5. grilled salmon
6. hamburger
7. hot dog
8. natto
9. omelet
10. pizza
11. rice
12. rice ball
13. spaghetti
14. steak
15. waffle

## Experiment evaluation tracking
- all model train and evaluate using FOOD15 v2 dataset (https://drive.google.com/drive/folders/1c_D7QE6YUB5ILFR1aCpREV8EOFFk1BwD?usp=sharing)
- `map 0.5` as single matrics (bigger better)
- subject to: `ukuran*` (free), `kategori` (15 food, more better), dan `waktu prediksi**` (5 sec, less better)

|           name           | ukuran (MB) | kategori | waktu prediksi (s) | map 0.5 (val) | map 0.95 (val) | epoch / iterasi | weights file***  |
|:------------------------:|:-----------:|:--------:|:------------------:|:-------------:|:--------------:|:---------------:|:-----------:|
| YOLOv5s-transformer      |        14.4 |       15 |                    | 82.7          | 54.8           |             301 |             |
| YOLOv5s-transformer-best |             |       15 |                    | 48.8          | 23.5           |                 |             |
| YOLOv5s-transformer-last |             |       15 |                    | 49.5          | 24.4           |                 |             |
| YOLOv5s6                 |       23.98 |       15 |                    | 85.7          | 61.16          |             111 |             |
| YOLOv5s6-best            |             |       15 |                    | 67.2          | 37.8           |                 |             |
| YOLOv5s6-last            |             |       15 |                    | 60.1          | 35.3           |                 |             |
| YOLOv5s-best             |        14.8 |       15 |                    | 80.3          | 49.7           |             300 |             |
| YOLOv5s-last             |             |       15 |                    | 44            | 22.8           |                 |             |
| YOLOv5m6-best            |             |       15 |                    | 62.2          | 28.8           |                 |             |
| YOLOv5m6-last            |             |       15 |                    | 62.1          | 30.5           |                 |             |
| YOLOv5m6-best-2          |             |       15 |                    | 39.8          | 24             |                 |             |
| YOLOv5m6-last-2          |             |       15 |                    | 38.8          | 23.3           |                 |             |
| YOLOv5m-best             |             |       15 |                    | 49.8          | 30.4           |                 |             |
| YOLOv5m-last             |             |       15 |                    | 53.4          | 32             |                 |             |
| YOLOv4-Tiny              |       23.09 |       15 |                    | 74.26         |                |            5452 |             |
| YOLOv4-fp16              |         122 |       10 |                    |               |                |            1000 |             |
| YOLOv4                   |         244 |       10 |                    | 67.57         |                |            1000 |             |
| YOLOv4                   |             |        5 |                    |               |                |                 |             |
| YOLOv5m                  |         162 |       15 |                    | 88.3          |                |             200 |             |

`*` this metrics not longer measured as project plan has change

`**` this metrics measure as a whole user experienced

`***` all files in this link https://drive.google.com/drive/folders/1H1M3BRpyGXHtsOhGQx3AHhNlEThmTDh_?usp=sharing 

## Results
The result of the selected model inference https://drive.google.com/drive/folders/1GJOphru8FKrkiW_ihhpe3xnv8A1S8ViS?usp=sharing

[![N|Solid](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/results.jpg?token=ALAAYUGUXFY2CQOPGJUQ32TAXU6VA)]()

## Deployment
We decide to deploy selected model on Virtual Machine and comunicate to user using ResAPI.
This API endpoint recive .jpg image sent from android app backend and return list of food detected on the image.

strat flask server `nohup python resapi.py --port 4040 &`

send request to server `curl -X POST -F image=@path/to/iamge.jpg http://flask-server.url:P.O.R.T/v1/object-detection/yolov5s/`

[![N|Solid](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/resAPI.jpg?token=ALAAYUEI3L6ZDQAO3GXSRPTAXU6J2)]()

## Credits
- Datasets (allow us to use for non-commercial research purpose) http://foodcam.mobi/dataset256.html
- Yolov5 implementation https://github.com/ultralytics/yolov5
- Yolov4 implementation https://github.com/AlexeyAB/darknet/ and https://github.com/roboflow-ai/darknet
