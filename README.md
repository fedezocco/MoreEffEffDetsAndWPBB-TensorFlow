# Towards More Efficient EfficientDets and Low-Light Real-Time Marine Debris Detection 

This repository contains the source code and the dataset related to the paper:
Federico Zocco et al., Towards More Efficient EfficientDets and Low-Light Real-Time Marine Debris Detection, 2022, https://arxiv.org/pdf/2203.07155.pdf.  

An overview of the main folders is below. For details, see the .txt files inside each folder.

### Folder: _modified-EfficientDet

The folder "_modified-EfficientDet" is a modification of the original TensorFlow implementation of EfficientDets, version 
of 23 October 2021: https://github.com/google/automl/tree/master/efficientdet. The description of the architectural modifications is in the above mentioned paper. Here there is its implementation. We found that the architecture with less BiFPN layers and deeper class/box nets is more efficient.  

![Capture](https://user-images.githubusercontent.com/62107909/158774955-c8ba86e7-dc3d-4214-bdef-c634573e8209.JPG)

Files where I made changes or files that I have added (I commented with my name the changes in each file):

(1) re-wrote "tutorial.ipynb" (resulting in "Tutorial-training_PASCAL-federico_zocco.ipynb", "Tutorial-training_TrashICRA19-federico_zocco.ipynb", "Tutorial-inference_images-federico_zocco.ipynb" and "Tutorial-model_eval-federico_zocco.ipynb")

(2) slightly modified "hparams_config.py" 

(3) slightly "modified model_inspect.py"

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

![Capture](https://user-images.githubusercontent.com/62107909/158659111-9856b27f-ba26-44ca-81b2-e9d98c0fa0bf.JPG)
