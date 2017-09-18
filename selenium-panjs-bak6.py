from selenium import webdriver
from urllib import request
import os
import random
import time
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys


#       查找一个页面中的元素：
#find_element_by_id
#find_element_by_name
#find_element_by_xpath
#find_element_by_link_text
#find_element_by_partial_link_text
#find_element_by_tag_name
#find_element_by_class_name
#find_element_by_css_selector
#        下面是查找多个元素（这些方法将返回一个列表）：
#find_elements_by_name
#find_elements_by_xpath
#find_elements_by_link_text
#find_elements_by_partial_link_text
#find_elements_by_tag_name
#find_elements_by_class_name
#find_elements_by_css_selector

#定位username元素的方法如下：
#http://www.cnblogs.com/qingchunjun/p/4208159.html  定位参考资料
#by xpath：
#1. 绝对定位：
#此方法最为简单，具体格式为
#          xxx.find_element_by_xpath("绝对路径")
#    具体例子：
#         xxx.find_element_by_xpath("/html/body/div[x]/form/input") x 代表第x个 div标签，注意，索引从1开始而不是0
#2.相对路径：
#相对路径，以‘//’开头，具体格式为
# xxx.find_element_by_xpath("//标签")
#具体例子：
#xxx.find_element_by_xpath("//input[x]") 定位第x个input标签,[x]可以省略，默认为第一个
#  相对路径的长度和开始位置并不受限制，也可以采取以下方法
#xxx.find_element_by_xpath("//div[x]/form[x]/input[x]"), [x]依然是可以省略的
#综合例子：
# <html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#    <input name="continue" type="button" value="Clear" />
#   </form>
# </body>
# <html>
#[python] view plain copy
#username = driver.find_element_by_xpath("//form[input/@name='username']")
#username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
#username = driver.find_element_by_xpath("//input[@name='username']")
#[1] 第一个form元素通过一个input子元素，name属性和值为username实现
#[2] 通过id=loginForm值的form元素找到第一个input子元素
#[3] 属性名为name且值为username的第一个input元素
###用Text关键字，定位代码如下：
#代码中的“退出”这个超链接，没有标准id元素，只有一个rel和href，不是很好定位。不妨我们就用xpath的几种模糊匹配模式来定位它吧，主要有三种方式，举例如下。
#用contains关键字，定位代码如下：
#1 driver.findElement(By.xpath(“//a[contains(@href, ‘logout’)]”));
#1 driver.findElement(By.xpath(“//*[text()=’退出’]));
#这个方法可谓相当霸气啊。直接查找页面当中所有的退出二字，根本就不用知道它是个a元素了。这种方法也经常用于纯文字的查找。
#另外，如果知道超链接元素的文本内容，也可以用
#1 driver.findElement(By.xpath(“//a[contains(text(), ’退出’)]));
#这种方式一般用于知道超链接上显示的部分或全部文本信息时，可以使用。

#元素操作：
#clear 清除元素的内容
#send_keys 模拟按键输入
#click 点击元素
#submit 提交表单

#操作页面的前进和后退功能：
#driver.forward()     #前进
#driver.back()        # 后退

#Python中文件读写模式：
#（1）r模式：
#该模式打开的文件必须存在，如果不存在，将会出错；并且，该模式打开的文件，只能读，不能向文件中写入。（只读）
#（2）r+模式：
#该模式打开的文件必须存在，如果不存在，将会出错；并且，该模式打开的文件，可以向文件中写入。
#（3）w模式：
#该模式打开的文件如果已经存在，则先清空，否则新建一个文件，然后只能写入数据，不能读取。
#（4）w+模式
#该模式打开的文件如果已经存在，则先清空，否则新建一个文件，然后可以写入数据，也可以读取。
#（5）a模式
#该模式打开的文件如果已经存在，不会清空，否则新建一个文件，写入的内容追加到文件尾；不能读取数据。（以追加的方式写入）
#（6）a+模式
#该模式打开的文件如果已经存在，不会清空，否则新建一个文件，写入的内容追加到文件尾；也可以读取数据

my_header = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)'
]

BASE_URL = 'https://book.km.com'
TYPE = 'shuku_0_0_0_1_0_0_%s.html'
NOVEL_DIR = 'books'

#driver = None

#获取第 n 页目录的所有小说
def getMenu(n,drv):
    print('getMenu: %s' % (n))
    title = drv.find_element_by_xpath('/html/body/div/div/div[3]/a').text
    print('test getMenu title:' + title)
    #第 n 页 的driver
    url_n = BASE_URL + '/' + TYPE % (n)  # 第 n 页
    drv.get(url_n)
    #获取本页menu的小说数量
    num = getCurrentMenuNovelNum(drv)
    for i in range(0,num):
        #getNovel(i, n,drv)
        getNovel(12,n,drv)  #test 抓取第4个小说
    time.sleep(5)


def getCurrentMenuNovelNum(drv):
    num = len(drv.find_elements_by_xpath("//div[contains(@class,'book_list')]/ul[@class='clearfix']/li"))
    print('novel num:',num)
    #return num
    return 1

#获取第 n 页中的第 m 个小说
def getNovel(m,n,drv):
    print('getNovel: 第%s页，第%s个小说' % (n,m))
    #处理drv页的第m个小说
    #title = drv.find_element_by_xpath("//ul[@class='clearfix']/li[%s]/div[@class='imgbox']/a/img/" % m).text
    title = drv.find_element_by_xpath("//ul[@class='clearfix']/li[%s]/div/a/img" % (str(m+1))).get_attribute('title')
    book_url = drv.find_element_by_xpath("//ul[@class='clearfix']/li[%s]/div/a" % (str(m+1))).get_attribute('href')
    auther = drv.find_element_by_xpath("//ul[@class='clearfix']/li[%s]/dl/dd[%s]/span/a" % (str(m+1),1)).text
    newest = drv.find_element_by_xpath("//ul[@class='clearfix']/li[%s]/dl/dd[%s]/span/a" % (str(m+1),2)).text
    desc = drv.find_element_by_xpath("//ul[@class='clearfix']/li[%s]/dl/dd[%s]" % (str(m + 1), 3)).text
    #img_url用了ajax异步加载，导致得到的url都是loading的url：http://img1.km.com/bookimg/public/pic/common/ajax-loading.gif
    #故此处采用小说具体的页面中的大图
    #img_url = drv.find_element_by_xpath("//ul[@class='clearfix']/li[%s]/div/a/img" % (str(m+1))).get_attribute('src')
    print('title:%s' % (title), 'book_url:' + book_url, 'auther:' + auther, 'newest:' + newest, 'disc:' + desc)
    dir = str(n)+'_'+str(m)+'_'+title
    os.mkdir(dir)
    f = open(os.path.join(dir,'desc.txt'), 'w')
    f.write('title:' + title + '\n')
    f.write('book_url:' + book_url + '\n')
    f.write('auther:' + auther + '\n')
    f.write('update to:' + newest + '\n')
    f.write('description:' + desc + '\n')
    f.flush()
    f.close()
    #request.urlretrieve(img_url,os.path.join(dir,'novel.jpg'))

    #通过book_url（小说详情页） 进入具体书籍，获取书籍图片(由于小说列表首页的小说图片是动态加载，所以在小说详细说明页加载图片)，
    drive_book = webdriver.PhantomJS()
    drive_book.get(book_url)
    img_url = drive_book.find_element_by_xpath("//div[@class='cover']/div/a/img").get_attribute('src')
    print('img url:%s' % img_url)
    request.urlretrieve(img_url, os.path.join(dir, 'novel.jpg'))
    #加载全部章节，并逐一下载全部章节中的每一页小说内容
    all_capter_url = drive_book.find_element_by_xpath("//div[@class='abook_contents']/p[@class='total']/a").get_attribute('href')
    print('all_capter_url: %s' % (all_capter_url))
    drive_book.get(all_capter_url)
    capter_num = getCapterNum(drive_book)  #获取章节数
    print('capter num:',capter_num)
    #循环获取每一章节的内容
    capters = drive_book.find_elements_by_xpath("//div[@class='mod_catalog']/div[@class='bd']/ul[@class='catalog_list clearfix']/li")
    #capters.txt用于保存章节列表名称
    fcapter = open(os.path.join(dir, 'capters.txt'),'w')
    capter_list = []
    index = 0
    for capter in capters:
        capter_title = capter.find_element_by_tag_name('a').text
        print('  capter_title:' + capter_title)
        capter_list.append('%s : %s \n' % (index,capter_title))
        index = index + 1
    fcapter.writelines(capter_list)
    fcapter.flush()
    fcapter.close()
    #章节列表获取完毕
    #循环获取章节实际内容。。
    #drive_book 全部章节页的drive
    #capters 所有章节的链接信息
    fnovel = open(os.path.join(dir,'novel.txt'),'a')
    novel_content_list = []
    index = 0
    for capteru in capters:
        capter_url = capteru.find_element_by_tag_name('a').get_attribute('href')
        print('  capter_url:' + capter_url)
        driv_book_capter = webdriver.PhantomJS()
        driv_book_capter.get(capter_url)
        novel_capter_title = driv_book_capter.find_element_by_xpath("//div[@class='main']/div[@class='article-title']/h1").text
        print('novel_capter_title:',novel_capter_title)
        capter_ps = driv_book_capter.find_elements_by_xpath("//div[@class='main']/div[@class='article-body']/p")
        for p in capter_ps:
            novel_content_list.append(p.text + '\n')
        driv_book_capter.close()
        #novel_capter_title = '第 %s 章：%s \n\n' % (index,novel_capter_title)  #报错
        fnovel.write('第 %s 章：' % str(index))
        fnovel.write(novel_capter_title + '\n\n')
        index = index + 1
        fnovel.writelines(novel_content_list)
        novel_content_list.clear()
        fnovel.flush()
    #退回到章节列表
    #drive_book.back()
    fnovel.close()
    print('''
         ########################################################################\n
         ########## ## ################### ######################################\n
         ###### ######### ################ ######## #############################\n
         ##### ############ ############## ###### ###############################\n
         ##### ############ ############## ### ##################################\n
         ###### ######### ################ ## ###################################\n
         ####### ####### ################# #### #################################\n
         ######### ## #################### ###### ###############################\n
         ################################# ######### ############################\n
         ########################################################################\n
    ''')
    pass
    pass
    time.sleep(1)

def getCapterNum(drive):
    num = len(drive.find_elements_by_xpath("//div[@class='mod_catalog']/div[@class='bd']/ul[@class='catalog_list clearfix']/li"))
    return num


def getWeb(m,n):
    url = BASE_URL+ '/' + TYPE % (1)  #第 1 页
    print('url: %s' % (url))
    # 调用环境变量指定的PhantomJS浏览器创建浏览器对象
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.implicitly_wait(2) #等待2秒
    #title = driver.find_element_by_xpath('//a[@class="i_website"]').text
    title = driver.find_element_by_xpath('/html/body/div/div/div[3]/a').text
    print('title:' + title)

    for i in range(m,n):
        getMenu(i,driver)
        driver = getNextMenuDriver(driver)

def getNextMenuDriver(driver):
    print('getNextMenuDriver')
    #print(driver.find_element_by_xpath('//div[@class="page"]/a[@text="下一页"]').text)
    #print(driver.find_element_by_xpath('//div[@class="page"]/a').text)
    print(driver.find_element_by_xpath('//a[contains(text(),"下一页")]').text)
    #得到下一页的driver
    pass
    return driver



if __name__ == '__main__':
    if os.path.exists(os.path.join(os.getcwd(),NOVEL_DIR)):
        print('dir exists return')
        exit(code=-1)
    else:
        os.mkdir(NOVEL_DIR)
        print('mkdir %s' % (NOVEL_DIR))
    os.chdir(NOVEL_DIR)
    print('cur path : %s' % (os.getcwd()))
    #一共爬取第 m 到第 n 页
    m = 1
    n = 2  #第二页会报错
    getWeb(m,n)
