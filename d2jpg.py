import pydicom
import matplotlib.pyplot as plt
import scipy.misc
import pandas as pd
import numpy as np
import imageio
import os
def dcm2jpg (file_path):
  #Get all picture names
  c=[]
  names=os.listdir (file_path) #path
  #Separate the file name in the folder from the .dcm behind
  for name in names:
    index=name.rfind (".")
    name=name [:index]
    c.append (name)
  for files in c:
    picture_path="C:\\Users\\prith\\Downloads\\Sample dicom\\"+files+".dicom"
    out_path="C:\\Users\\prith\\Downloads\\Sample dicom\\"+files+".jpg"
    ds=pydicom.read_file (picture_path)
    img=ds.pixel_array #extract image information
    imageio.imwrite(out_path, img)
  print ("all is changed")
dcm2jpg ("C:\\Users\\prith\\Downloads\\Sample dicom\\")
