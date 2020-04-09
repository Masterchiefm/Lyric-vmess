#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#载入必要的库
import os
os.system('pip install requests')
import requests 
import json
from base64 import b64decode,b64encode
DIR=0


# In[ ]:


def de_subscrip(subscription):
    vmesses = b64decode(subscription).decode('utf-8').splitlines()
    return vmesses


# In[ ]:


def de_vmess(vmess):
    vmess_code=vmess[8:]
    #print(vmess_code)
    content=str(b64decode(vmess_code).decode('utf-8'))
    #print(content) 
    #将内容转换为json格式
    content_json=json.dumps(eval(content))
    content_json=json.loads(content_json)
    #获取一句古诗词，借用了一言的API，如果要某一类的古诗，请自行参考https://v1.jinrishici.com/更改网址
    url2='https://v1.jinrishici.com/all'
    lyric=requests.get(url2).json()['content']#此处的json并不是模块json中的，是requests模块里包含的json()。
    print("\n\t获取的古诗词为：" + lyric)
    content_json["ps"]=lyric
    
    #生成新的配置，并转换为订阅
    new_content=str(content_json).encode('utf-8')
    new_vmess=str("vmess://" + str(b64encode(new_content),"utf8"))
    print("------更新后的Vmess链接------\n\n" + new_vmess + "\n\n------更新后的Vmess链接------\n\n\n\n")
    return new_vmess


# In[ ]:


def en_subscrip(vmesses):
    new_vmesses = ''
    for vmess in vmesses:
        new_vmesses = new_vmesses + vmess + '\r\n'
    new_subscrip = str(b64encode(new_vmesses.encode('utf-8')),'utf-8')
    return new_subscrip


# In[ ]:


def write_subscrip (DIR,new_subscrip):
    if DIR :
        print (DIR)
        file=open(DIR,'w')
        file.write(new_subscrip)
        file.close
        file=open(DIR)
        print("网页文件内容：\n"+file.read())
        file.close
        print("\n订阅内容已更新")
    input("回车退出")


# In[ ]:


def main_p():
    subscrip = input ('输入订阅or什么也不输入，回车跳过：\n #')
    if subscrip:
        vmesses = de_subscrip(subscrip)
        new_vmesses = []
        for vmess in vmesses:
            new_vmess = de_vmess(vmess)
            new_vmesses.append(new_vmess)
        new_subscrip = en_subscrip(new_vmesses)

    else:
        print("读取并解码原数据,请将原始vmess填入""之间,不要包含空格。vmess如果有等号也要放上去\n #")
        print("例如：vmess://sdfsfsdfadf= \n")
        vmesses = list(input('输入你的： '))
        new_vmesses = []
        for vmess in vmesses:
            new_vmess = de_vmess(vmess)
            new_vmesses.append(new_vmess)
        new_subscrip = en_subscrip(new_vmesses)
    return new_subscrip
        


# In[ ]:


new_subscrip = main_p()
DIR = input('输入订阅保存路径or回车跳过')
write_subscrip (DIR,new_subscrip)


# In[ ]:




