# nutrifit-ml
ML repository for Nutrifit project. The ML part of Nutrifit project is detect 15 food categories.

15 food category:

1.  
2.  
3.  

## Experiment evaluation tracking
- all model train and evaluate using FOOD15 v2 dataset
- `map 0.5` as single matrics (bigger better)
- subject to: `ukuran*` (free), `kategori` (15 food, more better), dan `waktu prediksi**` (5 sec, less better)

|           name           | ukuran (MB) | kategori | waktu prediksi (s) | map 0.5 (val) | map 0.95 (val) | epoch / iterasi | link gdrive |
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

## Deployment
We decide to deploy selected model on Virtual Machine and comunicate to user using ResAPI.
This API endpoint recive .jpg image sent from android app backend and return list of food detected on the image.
