** 请务必忽略截图中的错别字（人工捂脸**

Spyder在3.x版本之后开始支持自定义语言包。

虽然使用无障碍，还是想上一个中文包，毕竟还是好多朋友找这个汉化包。

这就是汉化包的由来啦。
![screenshot](./img/2017-04-07-13-59-16.png)
============================================
该汉化包已pull到Spyder官方，目前等待合并。合并后更新Spyder到最新版即可使用中文语言了，在此之前如果想尝试的话，可以使用一键安装脚本来安装。


### 必备条件：
>1、已安装Spyder
>
>2、Spyder版本在3.X以上。

### Spyder安装：
>1、anaconda下，conda install spyder
>
>2、Python发行版下， pip install spyder

### Spyder升级：
>1、anaconda下，conda update spyder
>
>2、Python发行版下，pip install --upgrade spyder


## 汉化包的安装：
如果python环境首选路径是anaconda的话，在main.py所在路径打开命令行或者终端，输入一下命令即可：
> python main.py


Ubuntu：

![screenshot](./img/spyder001.png)

Windows:

![screenshot](./img/spyder002.png)


安装完成后，打开或重启Spyder，在偏好设置中，选择简体中文，重启即可。



如果出现如下错误提示：

'''
/home/lzh/anaconda2/lib/python2.7/site-packages/spyder/config/base.py
Traceback (most recent call last):
  File "main.py", line 72, in <module>
    with open(configpath, 'r') as f:
IOError: [Errno 2] No such file or directory: '/home/lzh/anaconda2/lib/python2.7/site-packages/spyder/config/base.py'

'''

说明spyder版本不是3.x以上版本，需要先升级。
