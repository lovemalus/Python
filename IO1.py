#! usr/bin/env python
# -*- coding:UTF-8 -*-

x = 1.0/81.0
print x 
print 'value: %.2f' %x
print 'value: %.5f' %x

#格式字符串插入

print 'My {pet} has {prob}'.format(pet = 'dog', prob = 'fleas')
 
#在格式字符串中，用大括号括起来的内容都将被替换，这称为命名替换（named，replacement）
#还可以按位置替换

print 'My {0} has {1}'.format('dog', 'fleas')

#指定格式设置参数

print 'num = {x:.{d}f}'.format(x=1.0/81,d=3) 

#模板包
#cheetah(cheetahtemplate.com)
#Django(diangoproject.com)