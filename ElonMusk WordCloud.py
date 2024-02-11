import numpy as np  
from PIL import Image 
import matplotlib.pyplot as plt  
from wordcloud import WordCloud, STOPWORDS  

with open('elonmuskspeech.txt',encoding='utf-8',errors='ignore') as infile:
    text = infile.read()
    
mask = np.array(Image.open('rocket.png'))

stopwords = STOPWORDS 
stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
                  'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
                  'put', 'seem', 'asked', 'made', 'half', 'much',
                  'certainly', 'might', 'came','things'])

wc = WordCloud(max_words=500,
               relative_scaling=0.5,
               mask=mask,
               background_color='white',
               stopwords=stopwords,
               margin=2,
               random_state=7,
               contour_width=2,
               contour_color = 'brown',
               colormap='copper').generate(text)
colors = wc.to_array()

plt.figure()
plt.title("Elon Musk Speech:\n",
          fontsize=15, color='brown')
plt.text(-10,0,'Work Super Hard',fontsize=20, fontweight='bold',color='brown')
plt.suptitle("At The University",x=0.52,y=0.095,fontsize=15,color='brown')
plt.imshow(colors, interpolation="bilinear")
plt.axis('off')
plt.show()