# Implemented by Federico Zocco, version 16 March 2022

# This script modifies the PASCAL VOC 2012 annotations, which are in an .xml file. Specifically, it removes the "path" field and renames the "folder" field. 

# REFERENCES
#[1] F. Zocco et al., Towards More Efficient EfficientDets and Low-Light Real-Time Marine Debris Detection, https://arxiv.org/pdf/2203.07155.pdf
#[2] https://github.com/google/automl/blob/master/efficientdet/tutorial.ipynb
#[3] https://openaccess.thecvf.com/content_CVPR_2020/papers/Tan_EfficientDet_Scalable_and_Efficient_Object_Detection_CVPR_2020_paper.pdf



import xml.etree.ElementTree as ET
import os

############USER SETTINGS:
dataset_type = "bottle" #either train or val or bottle or bag  
###############################################################################


for file in os.listdir(dataset_type + '/'):
    if file.endswith(".xml"):

        # Read a single .xml file from the folder
        tree = ET.parse(dataset_type + '/' + file)
        root = tree.getroot()

        # Delete "path" field in an .xml file 
        for path in root.findall('path'):
            root.remove(path)

        # Rename "folder" field in an .xml file
        for folder in root.iter('folder'):    
            folder.text = dataset_type 
            
        # Overwrite the old .xml file
        tree.write(dataset_type + '/' + file)

