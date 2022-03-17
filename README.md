# Towards More Efficient EfficientDets and Low-Light Real-Time Marine Debris Detection 

![Capture](https://user-images.githubusercontent.com/62107909/158655824-5cc3caaf-6738-461d-bf6c-45a97c901783.JPG)

This repository contains the source code and the dataset related to the paper:
Federico Zocco et al., Towards More Efficient EfficientDets and Low-Light Real-Time Marine Debris Detection, 2022, https://arxiv.org/pdf/2203.07155.pdf.  

An overview of each folder is below. For details, see the .txt files inside each folder.

### 
This folder is a modification of the original TensorFlow implementation of EfficientDets, version 
of 23 October 2021: https://github.com/google/automl/tree/master/efficientdet

Files where I made changes or files that I have added (I commented with my name the changes in each file):

(1) re-wrote "tutorial.ipynb" (resulting in "Tutorial-training_PASCAL-federico_zocco.ipynb", 
"Tutorial-training_TrashICRA19-federico_zocco.ipynb", "Tutorial-inference_images-federico_zocco.ipynb" and
"Tutorial-model_eval-federico_zocco.ipynb")

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

![Capture](https://user-images.githubusercontent.com/62107909/158658670-1b94b5cb-0b18-42f0-861c-e13c8c936ab4.JPG)

![Capture](https://user-images.githubusercontent.com/62107909/158659111-9856b27f-ba26-44ca-81b2-e9d98c0fa0bf.JPG)
