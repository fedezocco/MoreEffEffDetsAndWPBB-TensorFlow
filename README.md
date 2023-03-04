# Towards More Efficient EfficientDets and Low-Light Real-Time Marine Debris Detection 

This repository contains the source code and the dataset related to the paper: F. Zocco, T. -C. Lin, C. -I. Huang, H. -C. Wang, M. O. Khyam and M. Van, "Towards More Efficient EfficientDets and Real-Time Marine Debris Detection," in IEEE Robotics and Automation Letters, vol. 8, no. 4, pp. 2134-2141, April 2023, doi: 10.1109/LRA.2023.3245405.

An overview of the main folders is below. For details, see the .txt files inside each folder.

### Folder: _modified-EfficientDet

The folder "_modified-EfficientDet" is a modification of the original TensorFlow implementation of EfficientDets, version 
of 23 October 2021: https://github.com/google/automl/tree/master/efficientdet. The description of the architectural modifications is in the paper mentioned above. Here there is its implementation. We found that the architecture with less BiFPN layers and deeper class/box nets is more efficient.  

![Capture](https://user-images.githubusercontent.com/62107909/158774955-c8ba86e7-dc3d-4214-bdef-c634573e8209.JPG)

Files where I made changes or files that I have added (I commented with my name the changes in each file):

(1) re-wrote "tutorial.ipynb" (resulting in "Tutorial-training_PASCAL-federico_zocco.ipynb", "Tutorial-training_TrashICRA19-federico_zocco.ipynb", "Tutorial-inference_images-federico_zocco.ipynb" and "Tutorial-model_eval-federico_zocco.ipynb")

(2) slightly modified "hparams_config.py" 

(3) slightly modified "model_inspect.py"

(4) created "dataset/prepare_xml-federico_zocco.py"

(5) added "dataset/generate_tfrecord.py"

(6) created "dataset/generate_tfrecords_Colab-federico_zocco.ipynb"

(7) slightly modified "dataloader.py"

(8) slightly modified "tf2/label_util.py" to add the Trash-ICRA19 and WPBB labels map 

(9) slightly modified "inference.py" to make either the WPBB or the Trash-ICRA19 labels map the default one

(10) added the folder "inference_images".

See each file for details. 

### Folder: WPBB_dataset

The folder "WPBB_dataset" contains the in-water plastic bags and bottles (WPBB) dataset, which currently has 900 fully annotated images for object detection. Annotations are in PASCAL VOC 2012 format.

![Capture](https://user-images.githubusercontent.com/62107909/158658670-1b94b5cb-0b18-42f0-861c-e13c8c936ab4.JPG)

### Folder: Low-light_detection_Results

The folder "Low-light_detection_Results" shows how the detection results in Table IX of the related paper were achieved. We found that, for real-time robotic applications, the simple low-light image enhancement method based on adding a constant value to all the pixels remains a competitive approach. 

![Capture](https://user-images.githubusercontent.com/62107909/158779957-984cc5c0-bcde-46cf-a3ef-5a25d1771aea.JPG)

