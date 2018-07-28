# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:07:29 2017

@author: lizenghai
"""

import os,shutil,sys
import platform

thissys = platform.system()
FLAG = r'\\' if thissys == 'Windows' else '/'
pyver = sys.version_info[0] + sys.version_info[1]/10
MODICT = {'spyder':'spyder.mo',
          'spyder_pylint':'pylint.mo',
          'spyder_profiler':'profiler.mo',
		  'spyder_breakpoints':'breakpoints.mo'}
def checkpath(path):
    '''检查路径，如果路径不存在则创建。
    param path<str>: 路径地址。
    return <str>:经过检查的路径。
    '''
    try:
        tmp = path.split(FLAG)
        if '.' in tmp[-1] and len(tmp)>1:
            path = FLAG.join(tmp[:-1])
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


def search_packages_path(pyflag='1'):
    '''查找site-packages的路径地址
    return <str>: path.
    '''
    sitepath="."
    for x in sys.path:
        if pyflag == '1' and 'anaconda' not in x.lower():
            continue
        if 'AppData' in x:
            continue
        ix1 = x.find('site-packages')
        ix2 = x.find('dist-packages')
        if( (ix1>=0 and x[ix1:]=='site-packages') or (ix2>=0 and x[ix2:]=='dist-packages') ):
          sitepath = x
          break
    
    return sitepath


def creat_language_folder(sitepath, modulename='spyder'):
    # creat zh_CN language folder
    try:
        zh_CN = sitepath + '{sep}{modulename}{sep}locale{sep}zh_CN{sep}LC_MESSAGES'.format(sep=FLAG, modulename=modulename)
        checkpath(zh_CN)
        
        return 1
    except:
        return 0
    
def shutil_file(sitepath, modulename='spyder'):
    mo_file_name = MODICT[modulename]
    zh_CN = sitepath + '{sep}{modulename}{sep}locale{sep}zh_CN{sep}LC_MESSAGES'.format(sep=FLAG, modulename=modulename)
    shutil.copyfile(mo_file_name,zh_CN + r'{0}{1}'.format(FLAG, mo_file_name))
    
def chinesize(sitepath):
    '''执行汉化'''
    # base.py add zh_CN
    configpath = sitepath + '{0}spyder{1}config{2}base.py'.format(FLAG,FLAG,FLAG)
    print(configpath)
    newpath = sitepath + '{0}base.py'.format(FLAG)
    # 根据操作系统（Win和linux）、python2个大版本分别读取配置信息
    # 2020年之后就好了
    if thissys == 'Windows':
        if pyver > 2.7:
            newf = open(newpath, 'w', encoding='utf-8')
            with open(configpath, 'r',encoding='utf-8') as f:
                lines = f.readlines()
        else:
            import io
            newf = io.open(newpath, 'w', encoding='utf-8')
            with io.open(configpath, 'r',encoding='utf-8') as f:
                lines = f.readlines()
    
        islanguage = 0
        for i in range(len(lines)):
            line = lines[i]
            newf.writelines(line)
            if "LANGUAGE_CODES = {'en': u'English'," in line:
                islanguage = 1
                mystr = "                  'zh_CN': u'简体中文',\n" if pyver >2.7 else u"                  'zh_CN': u'简体中文',\n"
                
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
    if os.path.exists(sitepath + r'{0}spyder{1}config{2}base_bak.py'.format(FLAG, FLAG, FLAG)):
        os.remove(sitepath + r'{0}spyder{1}config{2}base_bak.py'.format(FLAG, FLAG, FLAG))
    os.rename(configpath,sitepath + r'{0}spyder{1}config{2}base_bak.py'.format(FLAG, FLAG, FLAG)) 
    # remove new base.py
    shutil.move(newpath,configpath) 
    mystr = u'中文语言包安装完毕，重启后配置语言选项即可。\n\n 按ENTER键开始子模块汉化'
    pyinput(mystr)
    return

def pyinput(mystr):
    try:
        input_content = raw_input(mystr.encode('gbk'))
    except:
        input_content = input(mystr)
    return input_content

if __name__ == '__main__':
    mystr = u'请输入数字以区分汉化方式，\n1、手动填入Python模块包路径（如：D:\Anaconda3\Lib\dist-packages 或 D:\Anaconda3\Lib\site-packages）。\n2、自动寻找路径。\n请输入 1或2:  '
    install_flag = pyinput(mystr)
    if install_flag == '1':
        mystr = u'Python安装根路径（如：D:\python 或 D:\anaconda）：  '
        sitepath = pyinput(mystr)
    else:
        mystr = '''
        =======================================================
        由于不同用户的环境变量过于复杂难以完全兼顾，因此
        加入部分手动配置项。                    
        一般而言，只有Windows系统会比较麻烦。另外，如果你 
        是windows系统，请确保你的python不是安装在系统盘中 
        的用户文件夹下的AppData这一类的路径里，为了照顾到
        大多数人已经将AppData做了过滤。    
        
        
        注意！！！ 如果你在安装anaconda时修改了其文件夹名
        称（如:默认为d:\\anaconda3,被修改为d:\\test），请按
        照选2/3，不要选1             
        ======================================================='''
        
        print(mystr)
        
        #==============================================================================
        mystr = u'请选择自己你的python类别:\n     1.Anaconda \n     2.Python原版\n     3.其他\n您的选择（数字）：'
        pyflag = pyinput(mystr)
   
        sitepath = search_packages_path(pyflag)
    
    print(sitepath)
    # 创建主翻译
    creat_language_folder(sitepath, 'spyder')
    shutil_file(sitepath, 'spyder')
    chinesize(sitepath)
    
    # 创建子翻译
    for m in MODICT.keys():
        if m =='spyder':
            continue
        creat_language_folder(sitepath, m)
        shutil_file(sitepath, m)

