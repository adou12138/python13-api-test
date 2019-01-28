# coding: utf-8
# python13-api-test 
# study_reflect 
# shen 
# 2019/1/28 22:41 
"""
反射

静态---运行前，如果要调用类的属性或者而方法，我需要实例化它的对象
动态---运行时，我就获取类的属性或者方法，甚至更改它的属性或者方法
"""

class Girls:
    '这个是个女孩类'

    single = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def singe(self):
        print(self.name + "会唱歌")

if __name__ == '__main__':
    # g = Girls('mongo', 18)
    # print(g.name)
    # g.singe()

    # setattr(g, 'hub', 'swimming')  # 给类或者实例对象，动态的去添加属性或者方法
    # 如果是用实例添加的，作用域仅仅限于当前实例的作用域，下面的g2就会报错：AttributeError: 'Girls' object has no attribute 'hub'
    setattr(Girls, 'hub', 'swimming')  # 传类名进去
    # print(g.hub)  # 编辑器是静态的时候才会去检查语法错误

    # g2 = Girls('lucy', 20)
    # print(g2.hub)

    # 不想实例化对象，直接根据某个属性名来获取属性值
    # print(getattr(Girls, 'hub'))  # 根据属性名获取类的属性
    # print(getattr(Girls, 'male'))  # 当属性不存在的时候，报：AttributeError: type object 'Girls' has no attribute 'male'
    print(hasattr(Girls, 'male'))  # 判断当前这个类有没有这个属性，有就返回True，没有就返回False
    print(hasattr(Girls, 'name'))
    print(hasattr(Girls, 'single'))  # 判断类是否有这个类属性

    g = Girls('mongo', 18)
    print(g.name)
    g.singe()
    print(hasattr(g, 'name'))  # 判断对象是否有这个实例属性

    # delattr(g, 'name')  # 删除对象属性
    # print(g.name)

    delattr(Girls, 'single')  # 删除类属性
    print(getattr(Girls, 'single'))  # AttributeError: type object 'Girls' has no attribute 'single'