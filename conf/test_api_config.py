# python_13
# test_config
# shen
# 2019/1/11 20:27

# import configparser  # ConfigParser 配置类 专门来读取配置文件的
from configparser import ConfigParser
from common import contants
# 配置文件：结尾 .ini、 .conf、 .config、 .properties、.xml

# 配置文件一般是什么样的
# section
# 片段/区域 [区域名] 存储的区域名里面的值是最好是唯一的
# option 相当于字典里面的key 一个一个的配置选项
# value 相当于字典里面的value

# 怎么用呢？
# # cf = configparser.ConfigParser() #import使用
cf = ConfigParser()  # 创建对象
cf.read('case.conf', encoding='utf-8')  # open()
# #方法一 读值：
# # value = cf.get('StudentInfo','class_name')
# # value = cf.get('TeacherInfo','t2')
# #方法二 读值：
# value = cf['TeacherInfo']['t2']#一层一层的剥开定位配置文件
# #方法三 读值：int float boolean
# value = eval(cf.get('TeacherInfo', 'grade'))#上下的效果都一样
# value = cf.getfloat('TeacherInfo', 'grade')

# value = cf.getint('TeacherInfo', 'avg_ag')
# value = cf.getboolean('TeacherInfo', 'age')
# print(value)
# print('值得类型', type(value))


# 注意点：读出来的值，都是字符串 对值进行处理 可以用eval（）
# 读取值，只能分开读取多个值
# 如果想要原来的数据类型 就用eval

# 看看啊python 中 * 和 ** 的打包和解包 http://www.lemfix.com/topics/51

# 写一个类 缺点：如果是列表类型或者是字典类型 或者是字符串类型，怎么做呢？下周二再讲解
from configparser import ConfigParser

class ReadConfig:
    '这个是一个读取配置文件的类'

    def __init__(self, file):
        self.cf = ConfigParser()  # 为什么要赋值给self.cf 方便后面的方法调用
        self.cf.read(file, encoding='utf-8')

    def get_value(self, section, option):

        return self.cf.get(section, option)

    def get_int(self, section, option):

        return self.cf.getint(section, option)

    def get_float(self, section, option):

        return self.cf.getfloat(section, option)

    def get_boolean(self, section, option):

        return self.cf.getboolean(section, option)


if __name__ == '__main__':
    # res = eval(ReadConfig('test_api.conf').get_value('CASE', 'button'))
    # print(res)
    # print(type(res))
    res = ReadConfig(contants.api_conf_file)
    res2 = res.get_value('LOG', 'file_name')
    print(res2)
    res3 = res.get_value('URL', 'path_url')
    print(res3)

