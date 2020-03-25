#!/usr/bin/env python
# coding: utf-8

# In[2]:


#载入必要的库
os.system('pip install requests')
import requests 
import json
from base64 import b64decode,b64encode
import os
DIR=0


# In[7]:


#===============================================================================
#-----------------------------------自定义区域-----------------------------------

print("读取并解码原数据,请将原始vmess填入""之间,不要包含空格。vmess如果有等号也要放上去\n")
print("例如：vmess://sdfsfsdfadf= \n")
URL=input("请粘贴你的:")

print("\n最终写入的订阅文件路径，没有/不懂就直接按回车跳过\n")
#例如，我在我网页服务器放了一个地方用来更新订阅
#例：DIR="/www/example.com/subscribe/index.html"
DIR=input("请输入:")

#-----------------------------------自定义区域-----------------------------------
#===============================================================================


# In[8]:


#读取原vmess内容
vmess_code=URL[8:]
#print(vmess_code)
content=str(b64decode(vmess_code).decode('utf-8'))
#print(content)


# In[9]:


#将内容转换为json格式
content_json=json.dumps(eval(content))
content_json=json.loads(content_json)


# In[14]:


#获取一句古诗词，借用了一言的API，如果要某一类的古诗，请自行参考https://v1.jinrishici.com/更改网址
url2='https://v1.jinrishici.com/all'
lyric=requests.get(url2).json()['content']#此处的json并不是模块json中的，是requests模块里包含的json()。
print("\n\t获取的古诗词为：" + lyric)


# In[11]:


#将获取的诗词替换原有的诗词
content_json["ps"]=lyric


# In[12]:


#生成新的配置，并转换为订阅
new_content=str(content_json).encode('utf-8')
new_vmess=str("vmess://" + str(b64encode(new_content),"utf8"))
new_subscribe=str(b64encode(new_vmess.encode('utf-8')),'utf-8')
print("------更新后的订阅文件内容------\n\n" + new_subscribe + "\n\n------更新后的订阅文件内容------\n" )
print("------更新后的Vmess链接------\n\n" + new_vmess + "\n\n------更新后的Vmess链接------\n\n\n\n")


# In[13]:


#将订阅文件内容写入到订阅文件中
if DIR :
    print (DIR)
    file=open(DIR,'w')
    file.write(new_subscribe)
    file.close
    file=open(DIR)
    print("网页文件内容：\n"+file.read())
    file.close
    print("\n订阅内容已更新")

