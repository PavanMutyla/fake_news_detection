from django.shortcuts import render, redirect
import pickle
model = pickle.load(open('model2.pkl', 'rb'))
tfidfvect = pickle.load(open('tfidfvect2.pkl', 'rb'))
import re
import pandas as pd
import string
import numpy as np
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text
def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt) 
    new_x_test = new_def_test["text"]
    new_xv_test = tfidfvect.transform(new_x_test).toarray()
    prediction = model.predict(new_xv_test)
    print(model.predict(new_xv_test))
    return prediction
    


from store.forms import (
    HeadlineForm
)
from store.models import (
    HeadLines
)

def file_uploader(request):   
    if request.method == 'POST':
        form = HeadlineForm(request.POST, request.FILES)
       
        if form.is_valid():
            # Ye kaiku....
            if(form.cleaned_data['headline'] and form.cleaned_data['image']):                
                return redirect('file-uploader')
            
            # The following block of code is for the ext
            elif form.cleaned_data['headline']:
                message = form.cleaned_data['headline']
                #cleaned_data = wordopt(message)
                #pred = manual_testing(message) #  .predict(message)
                pred = manual_testing(message)
                print(pred)
                print(message)
                
                if pred == 1:
                    instance = form.save(commit=False)
                    instance.is_real = True
                    instance.save()
                    
                    headline_instance = HeadLines.objects.get(id = instance.id)                    
                    print(headline_instance)
                    context = {
                        'headline': headline_instance
                    }
                    return render(request, 'result.html', context)              
                else:
                    instance = form.save(commit=False)
                    instance.is_real = False
                    instance.save()
                    
                    headline_instance = HeadLines.objects.get(id = instance.id)                     
                    context = {
                        'headline': headline_instance
                    }
                    return render(request, 'result.html', context)    

            # The following block of code is for the files
            else: 
                file = form.cleaned_data['image']
                pred = 1
                if pred == 1:
                    instance = form.save(commit=False)
                    instance.is_real = True
                    instance.save()     
                else:
                    form.save() 

            return render(request, 'result.html')
        else:
            print(form.errors)               
    else:
        form = HeadlineForm()
    
    context = {
        'form': form
    }
    return render(request, 'fileUploader.html', context)

def result(request):
    return render(request, 'result.html')
