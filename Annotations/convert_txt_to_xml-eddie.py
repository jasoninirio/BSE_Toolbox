from numpy.lib.type_check import imag
import pandas as pd
import os
import xml.etree.ElementTree as xml
from tqdm import tqdm
from PIL import Image
import sys
import glob

mphb_images_db = pd.read_csv("MPHB-label.txt", sep=",")

# Generate XML
def generateXML(image_obj):
    N = int((28 - image_obj.isna().sum()) / 4)
    try: 
        im = Image.open("image\\" + str(image_obj.idx).zfill(5) + ".jpg")
        width, height = im.size
        root = xml.Element("annotation")
        fn = xml.Element("filename")
        fn.text = "image\\" + str(image_obj.idx).zfill(5) + ".jpg"
        root.append(fn)

        size = xml.Element("size")
        root.append(size)

        w = xml.SubElement(size, "width")
        w.text = str(width)
        h = xml.SubElement(size, "height")
        h.text = str(height)
        d = xml.SubElement(size, "depth")
        d.text = "0"
        i = 0

        for i in range(N):
            _object = xml.Element("object")
            root.append(_object)

            class_name = xml.SubElement(_object, "name")
            class_name.text = "person"
            p = xml.SubElement(_object, "pose")
            p.text = "Unspecified"
            t = xml.SubElement(_object, "truncated")
            t.text = "0"
            d = xml.SubElement(_object, "difficult")
            d.text = "0"

            # Count how many boundboxes are not NaN = N
            # there are N/2 objects
            # xmax, ymax, xmin, ymin

            bound_box = xml.SubElement(_object, "bndbox")
            xmin = xml.SubElement(bound_box, "xmin")
            xmin.text = int(image_obj[(i * 4) + 1])
            ymin = xml.SubElement(bound_box, "ymin")
            ymin.text = int(image_obj[(i * 4) + 2])
            xmax = xml.SubElement(bound_box, "xmax")
            xmax.text = int(image_obj[(i * 4) + 3])
            ymax = xml.SubElement(bound_box, "ymax")
            ymax.text = int(image_obj[(i * 4) + 4])
        
        tree = xml.ElementTree(root)
        # tree.write("mphb_images_xml\\" + str(image_obj.idx).zfill(5) + ".xml")
        # print(tree)
        with open("xml\\" + str(image_obj.idx).zfill(5) + ".xml", "wb") as files:
            tree.write(files)
    except Exception:
        pass

if __name__ == "__main__":
    for i in tqdm(range(len(mphb_images_db.index))):
        generateXML(mphb_images_db.loc[i])
