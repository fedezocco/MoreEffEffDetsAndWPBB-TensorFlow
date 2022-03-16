# MoreEffEffDetsAndWPBB-TensorFlow

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
