 #coding=utf-8
 #!/usr/bin/env python

print '输入：'
a = input('  账户金额：')
if (isinstance(a, int) or isinstance(a, float)) and a>=0:
    b = input('  小费比例：')
    if isinstance(b, int) or isinstance(b, float):
        c = int((a*b/100.)*1000)
        if ((a*b/100)*1000)%10 > 0:
            c = c/10
            c = (c+1)/100.
        else:
            pass
        print '预期结果：'
        print '  小费：$%.2f' % c
        print '  总金额: $%.2f' % (a+c)

    else:
        print '小费比例格式输入错误。'

else:
    print '账户金额格式输入错误。'
