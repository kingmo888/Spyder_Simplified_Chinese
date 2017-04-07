# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:07:29 2017

@author: lizenghai
"""

import os,shutil,sys
import platform



thissys = platform.system()
flag = r'\\' if thissys == 'Windows' else '/'


def checkpath(path):
    try:
        tmp = path.split(flag)
        if '.' in tmp[-1] and len(tmp)>1:
            path = flag.join(tmp[:-1])
    except:
        pass
    if os.path.exists(path):
        if os.path.isfile(path)==False:
            return path
        else:
            raise ValueError('文件夹创建失败，存在同名文件。')
    else:
        os.makedirs(path)
        return path
    
    
# search site-packages folder
sitepath="."
for x in sys.path:
    ix=x.find('site-packages')
    if( ix>=0 and x[ix:]=='site-packages'):
      sitepath=x
      break
  
# creat zh_CN language folder
zh_CN = sitepath + '{0}spyder{1}locale{2}zh_CN{3}LC_MESSAGES'.format(flag,flag,flag,flag)
checkpath(zh_CN)
shutil.copyfile("spyder.mo",zh_CN + r'{0}spyder.mo'.format(flag))

# base.py add zh_CN
configpath = sitepath + '{0}spyder{1}config{2}base.py'.format(flag,flag,flag)

print(configpath)

    
newpath = sitepath + '{0}base.py'.format(flag)
if thissys == 'Windows':
    newf = open(newpath, 'w', encoding='utf-8')
    with open(configpath, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        islanguage = 0
        for i in range(len(lines)):
            line = lines[i]
            newf.writelines(line)
            if "LANGUAGE_CODES = {'en': u'English'," in line:
                #print(line)
                islanguage = 1
                mystr = "                  'zh_CN': u'简体中文',\n"
                newf.writelines(mystr)



else:
    newf = open(newpath, 'w')
    with open(configpath, 'r') as f:
        lines = f.readlines()
        islanguage = 0
        for i in range(len(lines)):
            line = lines[i]
            newf.writelines(line)
            if "LANGUAGE_CODES = {'en': u'English'," in line:
                #print(line)
                islanguage = 1
                mystr = "                  'zh_CN': u'简体中文',\n"
                newf.writelines(mystr)
    
    
    
newf.close()

# rename old base.py
if os.path.exists(sitepath + r'{0}spyder{1}config{2}base_bak.py'.format(flag, flag, flag)):
    os.remove(sitepath + r'{0}spyder{1}config{2}base_bak.py'.format(flag, flag, flag))
os.rename(configpath,sitepath + r'{0}spyder{1}config{2}base_bak.py'.format(flag, flag, flag)) 
# remove new base.py
shutil.move(newpath,configpath) 

try:
    raw_input('中文语言包安装完毕，请重启后配置语言选项即可。\n请尽情享用~\n\n 按ENTER键退出。')
except:
    input('中文语言包安装完毕，请重启后配置语言选项即可。\n请尽情享用~\n\n 按ENTER键退出。')
