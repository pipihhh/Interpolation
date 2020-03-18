import matplotlib.pyplot as plt
from pylab import mpl


"""
牛顿插值法
插值的函数表为
xi      0.4，       0.55，     0.65，      0.80，       0.90，   1.05
f(xi)   0.41075,    0.57815,   0.69675,    0.88811,    1.02652,  1.25382
"""

x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]

"""计算五次差商的值"""


def five_order_difference_quotient(x, y):
    # i记录计算差商的次数，这里循环5次，计算5次差商。
    i = 0
    quotient = [0, 0, 0, 0, 0, 0]
    while i < 5:
        j = 5
        while j > i:
            if i == 0:
                quotient[j] = ((y[j] - y[j - 1]) / (x[j] - x[j - 1]))
            else:
                quotient[j] = (quotient[j] - quotient[j - 1]) / (x[j] - x[j - 1 - i])
            j -= 1
        i += 1
    return quotient


def get_quotient(xi, fi):
    # xi = [Decimal(str(x)) for x in xi]
    # fi = [Decimal(str(y)) for y in fi]
    # ret_arr = [[None for _ in range(len(xi))] for _ in range(len(xi))]
    # for col in range(len(ret_arr[0])):
    #     if col + 1 >= len(ret_arr[0]):
    #         break
    #     ret_arr[col][0] = (fi[col+1] - fi[col]) / (xi[col+1] - xi[col])
    # for col in range(1, len(ret_arr)):
    #     for row in range(len(ret_arr[col])):
    #         if col + row + 1 >= len(ret_arr[col]):
    #             break
    #         ret_arr[row][col] = (ret_arr[row+1][col-1] - ret_arr[row][col-1]) / (xi[row+col+1] - xi[row])
    parameter_arr = [None for _ in range(len(xi) - 1)]
    for index in range(len(parameter_arr)):
        # print((fi[1] - fi[0]) / (xi[1] - xi[0]))
        parameter_arr[index] = (fi[index + 1] - fi[index]) / (xi[index + 1] - xi[index])
    # print(parameter_arr)
    temp = None
    for difference in range(1, len(parameter_arr)):
        for index in range(difference, len(parameter_arr)):
            last = parameter_arr[index]

            parameter_arr[index] = (parameter_arr[index] - parameter_arr[index - 1]) / (
                        xi[index + 1] - xi[index - difference]) if temp is None else (parameter_arr[index] - temp) / (
                        xi[index + 1] - xi[index - difference])
            temp = last
        temp = None
    print(parameter_arr)
    return parameter_arr


def function(data):
    return x[0] + parameters[1] * (data - 0.4) + parameters[2] * (data - 0.4) * (data - 0.55) + \
           parameters[3] * (data - 0.4) * (data - 0.55) * (data - 0.65) \
           + parameters[4] * (data - 0.4) * (data - 0.55) * (data - 0.80)


def function2(data, param, xi, fi, j=None):
    j = j or len(param) - 1
    count = fi[0]
    while j >= 0:
        tmp = param[j]
        index = j
        while index >= 0:
            # count *= data - Decimal(str(xi[index]))
            tmp *= data - xi[index]
            index -= 1
        count += tmp
        j -= 1
    # count += Decimal(str(fi[0]))
    return count



"""计算插值多项式的值和相应的误差"""


def calculate_data(x, parameters):
    returnData = []
    for data in x:
        returnData.append(function(data))
    print(returnData)
    return returnData


def calculate_data2(param, xi, fi, j=None):
    return_data = []
    for data in xi:
        # return_data.append(function2(Decimal(str(data)), param, xi, fi))
        return_data.append(function2(data, param, xi, fi, j))
    print(return_data)
    return return_data


"""画函数的图像
newData为曲线拟合后的曲线
"""


def draw(newData):
    plt.scatter(x, y, label="离散数据", color="red")
    plt.plot(x, newData, label="牛顿插值拟合曲线", color="black")
    plt.scatter(0.596, function(0.596), label="预测函数点", color="blue")
    plt.title("牛顿插值法")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc="upper left")
    # plt.savefig(f"C:\\Users\\qq312\\Desktop\\{random.randint(1, 10)}.png")
    # plt.imshow((10, 10, 4))
    plt.show()


parameters = five_order_difference_quotient(x, y)
print(parameters)
ret = get_quotient(x, y)
yz = calculate_data2(ret, x, y)
yuanzu = calculate_data(x, parameters)
draw(yz)
