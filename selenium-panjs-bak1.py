from selenium import webdriver
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

my_header = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)'
]

BASE_URL = 'https://book.km.com'
TYPE = 'shuku_0_0_0_1_0_0_1.html'
NOVEL_DIR = 'books'

#driver = None

#获取第 n 页目录的所有小说
def getMenu(n,drv):
    print('getMenu: %s' % (n))
    title = drv.find_element_by_xpath('/html/body/div/div/div[3]/a').text
    print('test getMenu title:' + title)
    #获取本页menu的小说数量
    num = getCurrentMenuNovelNum(drv)
    for i in range(0,num):
        getNovel(i, n,drv)
    time.sleep(5)


def getCurrentMenuNovelNum(drv):
    num = len(drv.find_elements_by_xpath("//div[contains(@class,'book_list')]/ul[@class='clearfix']/li"))
    print('novel num:',num)
    return 5

#获取第 n 页中的第 m 个小说
def getNovel(m,n,drv):
    print('getNovel: 第%s页，第%s个小说' % (n,m))
    #处理drv页的第m个小说
    pass
    pass
    time.sleep(1)


def getWeb(m,n):
    url = BASE_URL+ '/' + TYPE
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
    m = 0
    n = 2
    getWeb(m,n)



