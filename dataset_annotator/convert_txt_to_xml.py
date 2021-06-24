from numpy.lib.type_check import imag
import pandas as pd
import os
import xml.etree.ElementTree as xml
from tqdm import tqdm
from PIL import Image

class_names_db = pd.read_csv("cars_meta.txt", sep=",")
cars_train_annos = pd.read_csv("cars_train_annos.txt", sep=",")

# Generate XML
def generateXML(image_obj, class_type):
    # print("On Image: " + image_obj.fname)
    im = Image.open("cars_train\\" + image_obj.fname)
    width, height = im.size
    root = xml.Element("annotation")
    fn = xml.Element("filename")
    fn.text = image_obj.fname
    root.append(fn)

    size = xml.Element("size")
    root.append(size)

    w = xml.SubElement(size, "width")
    w.text = str(width)
    h = xml.SubElement(size, "height")
    h.text = str(height)
    d = xml.SubElement(size, "depth")
    d.text = "0"

    _object = xml.Element("object")
    root.append(_object)

    class_name = xml.SubElement(_object, "name")
    class_name.text = str(class_type.loc[0][image_obj._class - 1])
    p = xml.SubElement(_object, "pose")
    p.text = "Unspecified"
    t = xml.SubElement(_object, "truncated")
    t.text = "0"
    d = xml.SubElement(_object, "difficult")
    d.text = "0"
    bound_box = xml.SubElement(_object, "bndbox")
    xmin = xml.SubElement(bound_box, "xmin")
    xmin.text = str(image_obj.bbox_x1)
    ymin = xml.SubElement(bound_box, "ymin")
    ymin.text = str(image_obj.bbox_y1)
    xmax = xml.SubElement(bound_box, "xmax")
    xmax.text = str(image_obj.bbox_x2)
    ymax = xml.SubElement(bound_box, "ymax")
    ymax.text = str(image_obj.bbox_y2)

    tree = xml.ElementTree(root)
    with open("cars_train_xml\\" + image_obj.fname[:-4] + ".xml", "wb") as files:
        tree.write(files)

if __name__ == "__main__":
    for i in tqdm(range(len(cars_train_annos.index))):
        generateXML(cars_train_annos.loc[i], class_names_db)
