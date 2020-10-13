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
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)
    plt.figure(figsize=(8,6),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    print('generated')

def create_word_cloud(string, Type):
	print(Type)
	print('OOKk')
	if Type == 1:
		maskArray = npy.array(Image.open(r"wc/static/square.png"))
	elif Type == 2:
		maskArray = npy.array(Image.open(r"wc/static/heart.jpg"))
	elif Type == 3:
		maskArray = npy.array(Image.open(r"wc/static/diamond.jpg"))
	cloud = WordCloud(background_color = "white",max_words = 200,margin=0, mask = maskArray, stopwords = set(STOPWORDS))
	cloud.generate(string)
	cloud.to_file(r"wc/static/pic.png")

def index(request):
    if (request.method == 'POST'):
    	print('POSTED')
    	form = textInput(request.POST)
    	if form.is_valid():
    		text = form.cleaned_data['text']
    		Type = form.cleaned_data['maskType']
    		dataset = text.lower()
    		print(text)
    		print(Type)
    		if Type == 'Type1':
    			create_word_cloud(string = dataset, Type = 1)
    		elif Type == 'Type2':
    			create_word_cloud(string = dataset, Type = 2)
    		elif Type == 'Type3':
    			create_word_cloud(string = dataset, Type = 3)
    		
    	return render(request,'wc/image.html')
    else:
    	form = textInput()
    	args = {'form': form}
    	return render(request,'wc/ak.html', args)
def aboutus(request):
	return render_to_response('wc/aboutus.html')
def contact(request):
	return render_to_response('wc/contact.html')

