# Lyric-vmess
## 作用
初学python，不知道要搞什么。正好，vmess配置文件有个“别名”，这个别名是为了方便管理，就是个备注的意思。因为它可以随便改而不影响连接，所以我们就改了他吧！这个别名通常是美国啊，脚本作者什么的，很难看，不如用py换成古诗。
## 用法
### 1）
直接运行以下命令，按照提示输入即可
```
#Ubuntu:
python3 <(curl -s -L  https://raw.githubusercontent.com/Masterchiefm/Lyric-vmess/master/lyric-vmess.py)
#

#Windows:
curl  https://raw.githubusercontent.com/Masterchiefm/Lyric-vmess/master/lyric-vmess.py -O lyric-vmess.py ; python lyric-vmess.py
```
### 2）

下载py文件，自行修改，有注释。然后用python3运行。按照提示输入即可
```
#
wget --no-check-certificate  https://github.com/Masterchiefm/Lyric-vmess/blob/master/lyric-vmess.py

python3 lyric-vmess.py
#
```
## 使用的API
使用了大佬的免费API：[古诗词·一言](https://gushi.ci/)


[大佬的github](https://github.com/xenv/gushici)
