 #coding=utf-8
 #!/usr/bin/env python

print '输入：'
a = input('  账户金额：')
if (isinstance(a, int) or isinstance(a, float)) and a>=0:
    b = input('  小费比例：')
    if isinstance(b, int) or isinstance(b, float):
        c = a*b/100.
        if c%0.01 >= 0.001:
            c = c-c%0.001
        print '预期结果：'
        print '  小费：$%.2f' % c
        print '  总金额: $%.2f' % (a+c)

    else:
        print '小费比例格式输入错误。'

else:
    print '账户金额格式输入错误。'
print 1.6985%0.01
#python 中的浮点数也可以进行求余操作——  一大特点or区别？