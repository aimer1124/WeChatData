# coding:utf-8
import itchat
import re
itchat.login()
friends = itchat.get_friends(update=True)[0:]
tList = []
text = ""
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)
    text = "".join(tList)


import jieba
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)


import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
d = os.path.dirname(__file__)
my_wordcloud = WordCloud(font_path='/Users/yjshi/Library/Fonts/arialuni.ttf').generate(wl_space_split)
plt.imshow(my_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()