if __name__ == '__main__':
    # 生成了一个名为a的函数
    # 通过a() 进行调用
    a = lambda x: x + x
    print(a)
    print(a(2))
    # 输出如下
    # < function <lambda > at 0x0000020E868A6288 >
    # 4
