import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
from keras_preprocessing import image
import numpy as np
import easygui
from keras.models import load_model
import os
import serial
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
my_w = tk.Tk()
my_w.geometry("500x300")  # Size of the window 
my_w.title('www.car damage prediction.com')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload Files & display',width=30,font=my_font1)  
l1.grid(row=1,column=1,columnspan=4)
b1 = tk.Button(my_w, text='Upload Files', 
   width=20,command = lambda:looping())
b1.grid(row=2,column=1,columnspan=4)
print(tf.__version__)



model1 = load_model('model/Class1/model_Class1.h5')
model2 = load_model('model/Class2/model_Class2.h5')
model3 = load_model('model/Class3/model_Class3.h5')
model4 = load_model('model/Class4/model_Class4.h5')
model5 = load_model('model/Class5/model_Class5.h5')
model6 = load_model('model/Class6/model_Class6.h5')
def objectside():
    
   filename =upload_file()
   test_image2 = image.load_img(filename, target_size = (64, 64))
   test_image2 = image.img_to_array(test_image2)
   test_image2 = np.expand_dims(test_image2, axis = 0)   
   # cnn prediction on the test image
   result2 = model1.predict(test_image2)
   print(result2)
   result3 = model2.predict(test_image2)
   print(result3)
   result4 = model3.predict(test_image2)
   print(result4)

   if result2[0][0] == 0:
      if result3[0][0] == 1:
         if  result4[0][0] == 1:
            prediction2='Rear Damage'
         else:
            prediction2='Side Damage'
      else:
         prediction2='Front Damage'
   else:
      prediction2 = 'Whole Car'
   print(prediction2)
   prediction=prediction2
   l2 = tk.Label(my_w,text="Location :  "+prediction,width=30,font=my_font1)  
   l2.grid(row=5,column=0,columnspan=4)
   return filename 
def percentage():
   image11 =objectside()
   test_image2 = image.load_img(image11, target_size = (64, 64))
   test_image2 = image.img_to_array(test_image2)
   test_image2 = np.expand_dims(test_image2, axis = 0)   
   # cnn prediction on the test image
   result2 = model1.predict(test_image2)
   print(result2)
   result5 = model4.predict(test_image2)
   print(result5)
   result6 = model5.predict(test_image2)
   print(result6)
   result7 = model6.predict(test_image2)
   print(result7)

   if result2[0][0] == 0:
      if result5[0][0] == 1:
         if result6[0][0] == 1:
            if  result7[0][0] == 1:
               prediction2='75% Damage'
            else:
               prediction2='50% Damage'
         else:
            prediction2='25% Damage'
      else:
         prediction2 = 'Below 25% Damage'
   else:
      prediction2 ='No Damage'
      
   print(prediction2)
   prediction=prediction2
   l3 = tk.Label(my_w,text="Percentage :  "+prediction,width=30,font=my_font1)  
   l3.grid(row=6,column=0,columnspan=4)
   return prediction2

def looping():
  
   below="2000 to 5000"
   c25="8000 to 15,000"
   d50="20,000 to 45,000"
   e75="85,000 to 1,50,000"
   per=percentage()
   if per =='Below 25% Damage':
      cost=below
      print("Estimated collision repair costs ="+ cost)
   elif per =='25% Damage':
      cost=c25
      print("Estimated collision repair costs ="+ cost)
   elif per =='50% Damage':
      cost=d50
      print("Estimated collision repair costs ="+ cost)
   elif per =='75% Damage':
      cost=e75
      print("Estimated collision repair costs ="+ cost)
   elif per =='No Damage':
      cost="GOOD"
      print("Estimated collision repair costs ="+ cost)
   else:
      print("No need everthing is clear")
   
   per=cost
   l3 = tk.Label(my_w,text="Estimated repair costs :  "+per,width=30,font=my_font1)  
   l3.grid(row=7,column=0,columnspan=4)
       
def upload_file():
    f_types = [('JPEG Files', '*.JPEG'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=False,filetypes=f_types)
     
    img=Image.open(filename) # read the image file
    img=img.resize((100,100)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(my_w)
    e1.grid(row=3,column=2)
    e1.image = img
    e1['image']=img
    return filename

my_w.mainloop()




