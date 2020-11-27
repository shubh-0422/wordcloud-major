from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import textInput
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
import requests
import matplotlib.pyplot as plt
import numpy as npy

def generate_wordcloud(words, mask):
    word_cloud = WordCloud(width = 512, height = 512, background_color='black', stopwords=STOPWORDS, mask=mask).generate(words)
    plt.figure(figsize=(8,6),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    print('generated')

def create_word_cloud(string, Type):
	print(Type)
	print('OOKk')
	type="wc/static/"+Type+".jpg"
	maskArray = npy.array(Image.open(type))
	cloud = WordCloud(background_color = "black",margin=0, mask = maskArray, stopwords = set(STOPWORDS))
	cloud.generate(string)
	cloud.to_file(r"wc/static/pic.png")

def create(request):
    if (request.method == 'POST'):
    	print('POSTED')
    	form = textInput(request.POST)
    	if form.is_valid():
    		text = form.cleaned_data['text']
    		Type = form.cleaned_data['maskType']
    		dataset = text.lower()
    		print(text)
    		print(Type)
    		create_word_cloud(string = dataset,Type=Type)
    		
    	return render(request,'wc/image.html')
    else:
    	form = textInput()
    	args = {'form': form}
    	return render(request,'wc/ak.html', args)
def aboutus(request):
	return render_to_response('wc/aboutus.html')
def contact(request):
	return render_to_response('wc/contact.html')
def home(request):
	return render_to_response('wc/index.html')


