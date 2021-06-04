
Nutrifit-10 - v3 2021-05-25 5:32pm
==============================

This dataset was exported via roboflow.ai on June 4, 2021 at 5:57 AM GMT

It includes 5027 images.
Foods are annotated in Tensorflow TFRecord (raccoon) format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
* Random rotation of between -15 and +15 degrees
* Random shear of between -15° to +15° horizontally and -15° to +15° vertically
* Random brigthness adjustment of between -20 and +20 percent
* Random exposure adjustment of between -25 and +25 percent
* Random Gaussian blur of between 0 and 1 pixels
* Salt and pepper noise was applied to 1 percent of pixels

Download
https://drive.google.com/file/d/1-AQZ2OB5qAdmWkJXol1hdanUBtwD21DV/view?usp=sharing
