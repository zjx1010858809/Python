# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# a = 10
# b = 3
# a += b # 相当于：a = a + b
# print(a)
# print('%d * = %d + 2' % (a,a))
# a *= a + 2 # 相当于：a = a * (a + 2)
# print(a) # 想想这里会输出什么
# print(15*13)
#
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
