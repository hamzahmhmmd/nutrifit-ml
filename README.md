# nutrifit-ml
ML repository for Nutrifit project. The ML part of Nutrifit project is detect 15 food categories.

## Data
Details about data for this project available in dataset above.

#### 15 food category:
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

#### Sample Augmented Training Data
*mosaic image augmentation only implemented on YOLO not on EfficientDet*

[![N|Solid](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/train_batch0.jpg)]()
[![N|Solid](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/train_batch1.jpg)]()
[![N|Solid](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/train_batch2.jpg)]()

## Experiment evaluation tracking
- all model train and evaluate using FOOD15 v2 dataset (https://drive.google.com/drive/folders/1c_D7QE6YUB5ILFR1aCpREV8EOFFk1BwD?usp=sharing)
- `map 0.5` as single matrics (bigger better)
- subject to: `ukuran*` (free), `kategori` (15 food, higher better), dan `waktu prediksi**` (5 sec, less better)

|           name           | ukuran (MB) | kategori | waktu prediksi (s) | map 0.5 (val) | map 0.95 (val) | epoch / iterasi |weights files|
|:------------------------:|:-----------:|:--------:|:------------------:|:-------------:|:--------------:|:---------------:|:-----------:|
| Efficientdet-d0          |             |       15 |                    | 79.40         | 0.462          |            8000 |  tf (saved) |
| Efficientdet-d0 food15v3 |             |       15 |                    | 65.40         | 0.386          |            4500 |  tf (saved) |
| Efficientdet-d1          |             |       15 |`**LACK OF MEMORY**`|               |                |                 |             |
| YOLOv4-Tiny              |       23.09 |       15 |                    | 74.26         |                |            5452 |  tf (saved) |
| YOLOv4-fp16              |         122 |       10 |                    |               |                |            1000 |  tf (saved) |
| YOLOv4                   |         244 |       10 |                    | 67.57         |                |            1000 |  tf (saved) |
| YOLOv5s-transformer      |        14.4 |       15 |                    | 82.7          | 54.8           |             301 |pytorch (.pt)|
| YOLOv5s-transformer-last |             |       15 |                    | 49.5          | 24.4           |                 |pytorch (.pt)|
| `YOLOv5s6`               |     `23.98` |      `15`|                    | `85.7`        | `61.16`        |            `111`|`pytorch (.pt)`|
| YOLOv5s6-last            |             |       15 |                    | 60.1          | 35.3           |                 |pytorch (.pt)|
| YOLOv5s-best             |        14.8 |       15 |                    | 80.3          | 49.7           |             300 |pytorch (.pt)|
| YOLOv5s-last             |             |       15 |                    | 44            | 22.8           |                 |pytorch (.pt)|
| YOLOv5m6-best            |             |       15 |                    | 62.2          | 28.8           |                 |pytorch (.pt)|
| YOLOv5m6-last            |             |       15 |                    | 62.1          | 30.5           |                 |pytorch (.pt)|
| YOLOv5m6-best-2          |             |       15 |                    | 39.8          | 24             |                 |pytorch (.pt)|
| YOLOv5m6-last-2          |             |       15 |                    | 38.8          | 23.3           |                 |pytorch (.pt)|
| YOLOv5m-best             |             |       15 |                    | 49.8          | 30.4           |                 |pytorch (.pt)|
| YOLOv5m-last             |             |       15 |                    | 53.4          | 32             |                 |pytorch (.pt)|

`*` this metrics no longer measured/track as project plan has change

`**` this metrics measure as a whole user experienced

### Weights Files
All weights files in this link https://drive.google.com/drive/folders/1H1M3BRpyGXHtsOhGQx3AHhNlEThmTDh_?usp=sharing 

### Model Selection
We are select `YOLOv5s6` model for our app. 
The model reaches highest map 0.5 on validation data and the model meet our criteria: capable to detect 15 food categories, 
and based on our integration testing *waktu prediksi* is less than 5 s. 

> We are aware the model not implemented in Tensorflow Framework. Base on the capstone project rules we are allowed to not use Tensorflow when it is `not available`. In our case the pre-train model of YOLOv4 and YOLOv5 `only available` and `posible` on darknet and pytorch. We are using pre train model (transfer learning) for faster training, faster experiment, sweet able for GPU limitation on google colab, and equal MAP compare to training from scratch. We are `not possible` to select `YOLOv4-Tiny` (model on Tensorflow format) because the MAP far away lower than `YOLOv5s6`.
> 
> ![capstone rules](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/capstone-rules.jpg)

## Results
The result of the selected model inference https://drive.google.com/drive/folders/1GJOphru8FKrkiW_ihhpe3xnv8A1S8ViS?usp=sharing

[![N|Solid](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/results.jpg?token=ALAAYUGUXFY2CQOPGJUQ32TAXU6VA)]()

## Deployment
We decide to deploy the selected model on Virtual Machine and communicate to users using ResAPI.
This API endpoint recive .jpg image sent from the android app backend and returns a list of food detected on the image.

strat flask server `$ nohup python resapi.py --port 4040 &`

send a request to server `$ curl -X POST -F image=@path/to/iamge.jpg http://flask-server.url:P.O.R.T/v1/object-detection/yolov5s6/`

## Reproducibility
#### Model reproducibility
just run the notebook .ipynb on goole colab env. and dont forget to add the dataset from (https://drive.google.com/file/d/1lF_9VNyNVDcD8QxQivzOzCn_4LnkZheJ/view?usp=sharing)
#### Deployment reproducibility
1. set a VM instance
2. install requirements.txt
3. download model files from (https://drive.google.com/drive/folders/1H1M3BRpyGXHtsOhGQx3AHhNlEThmTDh_?usp=sharing)
4. makesure model path in `resapi.py` pointing the model file
5. run server `$ python resapi.py`
6. send a request

[![N|Solid](https://raw.githubusercontent.com/hamzahmhmmd/nutrifit-ml/master/resAPI.jpg?token=ALAAYUEI3L6ZDQAO3GXSRPTAXU6J2)]()

## Credits
- Datasets (allow us to use for non-commercial research purpose) http://foodcam.mobi/dataset256.html
- Yolov5 implementation https://github.com/ultralytics/yolov5
- Yolov4 implementation https://github.com/AlexeyAB/darknet/ and https://github.com/roboflow-ai/darknet
- Shout out to roboflow team for giving away colaborative feature for free

[![N|Solid](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.png)]()
