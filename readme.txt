

selenium

1.元素定位  ==>js DOM  document.getElementById()
#8大元素定位:ID,name,tagname,classname,partial_link_text,link_text,xpath,css
2.等待
3.元素操作
4.鼠标操作 actionchains
5.js脚本  js操作，窗口操作
6.Select类  click,option
7.文件上传    固定用法
8.三大切换    窗口，iframe,alert
9.selenium 原理


#selenium ,Server ===>python subprocess ,chromedriver.exe ===>启动服务
#urlib3 ===>requests==>进行http请求


#find_element()==>



#第二个面试题：css,xpath  css选择器简单定位更简洁
1.css对于简单的定位，更加的简洁
2.主流的浏览器，效率更高
3.复杂的定位，xpath更简洁
4.xpath基本上都能定位到，功能更强大


测试流程：
1.分析需求
2.测试计划，方案
3.写用例
4.用例评审
5.用例执行
6.报告

1.需求分析
2.先出具体方案，优先级，紧急的先做，历史的后作，哪些是自动化优势非常明显，交互非常多的，哪些可以用手动，让其他基础
测试人员去测，核心功能反复做，边缘功能次数少，技术选型，综合成熟性和现有人力


为什么要把业务逻辑从测试逻辑抽离出来
- 业务清晰
- 更加利于维护,
- 可以复用




首页里面的逻辑封装到一个页面：HomePage  ==>ＵＲＬ
- 方法和逻辑封装到登录页面： LoginPage　　　＝＝》URL
投资 BidPage，蜂群，  UserPage

PO  ==> PageObjcet  页面对象   ==》 页面封装成一个对象  ==》 DOM  HTML文档==》对象  document.getElement
document.url
# WebElement  ==> HTML标签--> python object, 对象。 web_elent.text  web_elem.get_attibute()

# --> Python object,  PageOject 加到简历。
PageObject  --> 1 WebElement  2 元素操作，

找元素出现了问题，没有找到或者是超时：
1.没有加等待
2.等待时间不够
3.定位表达式有问题
4.显示等待的条件不对


basepage需要封装哪些方法
原则：无论是在哪个页面都可以使用的



找元素出现了问题，没有找到或者是超时

1.没有加等待
2.等待时间不够
3.定位表达式有问题
4.显示等待的条件不对

basepage封装原则
不以测试的页面而改变，无论在哪个页面都可以使用

#web分层
1.PO PageObject 页面逻辑，测试逻辑
2.元素定位层,locator 单独成类，也可以写到类属性
3.数据层 ==》数据分组
4.用例层
5.basepage

一、pytest简洁和好处
1.自动发现 testloader
2.断言方便 assert
3.灵活运行指定的测试用例，标签化  回归，正向，冒烟，登录
4.环境管理灵活，会话、模块  fixture
5.丰富的插件，测试报告  allure
5.和unittest/nose 兼容

二、pytest运行方式
1.pytest
2.pytest -m pytest
3.编辑器
4.代码

三、测试用例的原则
文件 test_*.py 或者_test.py 开头或结尾
Test开头的不能有__init__函数
test_开头的函数
脱离类也是可以写的
import pytest
@pytest.mark.demo
def test_demo():
    print("测试成功")

执行 pytest -m demo -s

自定义查找规则：pytest.ini
[pytest]
python_files=
    test_*.py
    check_*.py
    example_*.py

 python_functions=*_test

 python_classes = *Suite

指定测试模块：pytest test_mod.py
指定测试目录 pytest testing/
通过节点id来运行测试
 节点id的组成:py模块名::类名::函数名  或者 py模块名::函数名
 示例:pytest test_xxx.py::TestXXX::func_xxx
通过关键字表达式过滤执行
    pytest -k "MyClass and not method"(条件过滤）
    这条命令会匹配文件名、类名、方法名匹配表达式的用例

 通过标记表达式执行
   pytest -m smoke(用and 连接多个标签名）
   这条命令会执行被装饰器@pytest.mark.smoke 装饰的所有测试用例

 获取用例执行性能数据
   获取最慢的10个用例的执行耗时
   pytest --durations=3



 四、mark随机测试
 pytest
   注册
   标签贴到测试用例上
   运行的时候指定标签
  mark 注册:修改ini文件
  #pytest.ini
  [pytest]
  markers=
    slow
    serial

1.函数标记
冒烟用例，需要保证所有文件夹和用例命名符合规范
#放到类和函数都可以
@pytest.mark.smoke

#运行
pytest -m smoke

2.类标记的2种方式
@pytest.mark.webtest
class TestClass(object):
    pytestmark=[pytest.mark.webtest,pytest.mark.slowtest]

3.标记表达式
可以同时打多个标签，可以在类上面打标签。而且可以用表达式 -m "mark and not mark2"
  【注意】一定要使用双引号，单引号会报错

4.跳过函数
@pytest.mark.skip(reason='out-of-date api')

#skipif
@pytest.mark.skipif(sys.platform=="win32",reason="does not run on windows")

5.跳过预见错误
@pytest.mark.xfail(gen.__version__<'0.2.0',reason='not support until v0.2.0')

五、pytest用例执行顺序
上下，而不是和unittest 根据assic码

六、断言
assert 自定义结果

assert a%2==0,"value was odd,should be even"


七、参数化
pytest和unittest兼容

pytest使用以下功能不能和unittest兼容
1.parametrize
2.fixture(autouse=True)
3.Custom hooks

4.pytest.fixture(scope="session")
只运行一次

#【注意】如果想在pytest使用parametrize和fixture就不能使用unittest
#pytest标签生产allure，分析最慢的测试用例 pytest和unittest兼容
