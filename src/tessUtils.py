import pytesseract as tess
from pytesseract import Output
from PIL import Image
import csv,sys

def imageToCsv(file_name):
    img = Image.open(file_name)
    data = tess.image_to_data(img,output_type=Output.DATAFRAME)
    new_name = '/output/' + file_name + '.csv'
    data.to_csv(new_name,index=False)

def imageToTxt(file_name):
    img = Image.open(file_name)
    data = tess.image_to_string(img)
    file_name = file_name.lower()
    new_name = file_name.replace('.png','.txt')
    # data.to_csv(new_name,index=False)
    with open(new_name,'w') as f:
        f.write(data)
        f.close()