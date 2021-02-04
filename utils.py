#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import math

plt.rcParams['figure.dpi'] = 150

def show_imgs(data,real_labels=None,pred_labels=None,classes_rev=[]):
    plt.figure(figsize=(10,10))
    rows=int(math.sqrt(len(data)))
    cols=len(data)//rows
    if(len(data)%rows!=0):
        cols+=1
    print("rows={},cols={}".format(rows,cols))
    w=rows
    h=cols
    fig, axs = plt.subplots(w,h)
    if(w==1):
        axs=[axs]
    if(h==1):
        axs=[axs]
    

    for i in range(w):        
        for j in range(h):
            label_text = "--"
            if(i*h+j<len(data)):#within bound
                img=data[i*h+j]
                axs[i][j].imshow(img)
                if(real_labels is not None):    #if label not given, just load the img
                    
                    label_num=real_labels[i*h+j]
                    label_text = classes_rev[label_num]
                else:
                    img=data[i*h+j]
                    axs[i][j].imshow(img)
                    
                if(pred_labels is not None):    #if pred label given, append pred label
                    pred_label_num=pred_labels[i*h+j]
                    pred_label_text = classes_rev[pred_label_num]
                    label_text+="\n{}".format(pred_label_text)
            axs[i][j].set_title(label_text,fontsize=5)
            axs[i][j].set_axis_off()
    if(pred_labels is not None):
        plt.subplots_adjust(wspace=0,hspace=0.7)
    else:
        plt.subplots_adjust(wspace=0,hspace=0.4)

    plt.show()


#display multiple labels for an image
#dispMax is how many labels to display, avoid flow out of box
def show_imgs_multi_label(data,real_labels=None,pred_labels=None,classes_rev=[],dispMax=3):
    plt.figure(figsize=(10,10))
    rows=int(math.sqrt(len(data)))
    cols=len(data)//rows
    if(len(data)%rows!=0):
        cols+=1
    print("rows={},cols={}".format(rows,cols))
    w=rows
    h=cols
    fig, axs = plt.subplots(w,h)
    if(w==1):
        axs=[axs]
    if(h==1):
        axs=[axs]
    

    for i in range(w):        
        for j in range(h):
            label_text = "--"
            if(i*h+j<len(data)):#within bound
                img=data[i*h+j]
                axs[i][j].imshow(img)
                if(real_labels is not None):    #if label not given, just load the img
                    
                    label_num_list=real_labels[i*h+j]
                    counter=0
                    for i,t in label_num_list:
                        if(t==1):
                            label_text += ("/"+classes_rev[label_num])
                            counter+=1
                            if(counter>3):
                                break
                else:
                    img=data[i*h+j]
                    axs[i][j].imshow(img)
                    
                if(pred_labels is not None):    #if pred label given, append pred label
                    pred_label_num=pred_labels[i*h+j]
                    pred_label_text = classes_rev[pred_label_num]
                    label_text+="\n{}".format(pred_label_text)
            axs[i][j].set_title(label_text,fontsize=5)
            axs[i][j].set_axis_off()
    if(pred_labels is not None):
        plt.subplots_adjust(wspace=0,hspace=0.7)
    else:
        plt.subplots_adjust(wspace=0,hspace=0.4)

    plt.show()




