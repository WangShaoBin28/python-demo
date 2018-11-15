def demo2():
    # print(100 + 200)
    # print('100 + 200 = ', 100 + 200)
    # name = input('请输入')
    # print('您输入的是', name)
    # print('1024 * 768 = ', 1024 * 768)
    # print('计算器开始**********************************')
    # oneNum = input('请输入您的第一个数:')
    # towNum = input('请输入您的第二个数:')
    # print(oneNum + '+' + towNum + '=', (float(oneNum) + float(towNum)))
    strr = ['aa', 'bb', 'cc']
    print(strr)
    print(len(strr))
    print(strr[-2])
    strr.append('dd')
    strr.insert(0, 'AA')
    print(strr)
    for str in strr:
        print(str)

    print('分割线————————————————')
    n = 0
    while n < len(strr):
        print(strr[n])
        n = n + 1


def demo1():
    print('holle')


def fact(n):
    if n == 1:
        return 1
    return fact(n - 1)


if __name__ == '__main__':
    print()
