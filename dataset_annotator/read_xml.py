from numpy.lib.type_check import imag
import pandas as pd
import os
import xml.etree.ElementTree as xml
from tqdm import tqdm
from PIL import Image

root = xml.parse("cars_train_xml\\00001.xml")
root = root.getroot() # annotations

for i in root[2][4]:
    print(i.text)