'''
    猜数字游戏：
        需求：让系统随机产生一个数字，用户从键盘输入数字，对比
        如果大了，提示：大了
        如果笑了，提示：小了
        恭喜猜中。print()
    技术选型：
        1、print() 打印
        2、随机数如何产生。
            random模块
                包含了所有随机的工具给我们使用。
            使用random.randint(起始值，结束值)得到一个随机数
        3、判断：if
        4、循环
            while 条件：
                循环体
        5、键盘输入
            input（）
            int（）将字符串变成整形数字

任务：
    1、加金币赌博功能。
    2、加猜的次数计算器功能。
'''
import random
# 让系统产生一个随机数字
data = random.randint(0,200)
coin = 5000
# 2、开始猜 ， 范围（0~200）

i = 0
while i <= 10:
    num = input("请输入您要猜的数字：")
    num = int(num)
    if num > data:
        coin = coin - 500
        print("大了！您当前在第",i+1,"次""您当前金币为",coin)
    elif num < data:
        coin = coin - 500
        print("小了！您当前在第",i+1,"次""您当前金币为",coin)
    else:
        coin = coin + 1000
        print("恭喜你，猜中数字，本次幸运数字为：",num,"您当前金币为：",coin)

        break  # continuet跳出当前循环 继续下一循环
    i = i + 1
