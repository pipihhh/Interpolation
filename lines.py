from flask import request
import numpy as np
from hermite import get_Hermite_interpolation
import matplotlib.pyplot as plt
from newton import get_quotient, function2


class Newton(object):
    def __init__(self):
        self._fxi = list(map(lambda x: float(x), request.form.get("fxi").split(",")))
        self._xi = list(map(lambda x: float(x), request.form.get("xi").split(",")))

    def generate(self):
        # parameters = five_order_difference_quotient(self._xi, self._fxi)
        ret = get_quotient(self._xi, self._fxi)
        x_list = np.arange(min(self._xi), max(self._xi)+0.1, 0.01)
        y_list = [function2(i, ret, self._xi, self._fxi) for i in x_list]
        plt.scatter(self._xi, self._fxi, label="Newton Point", color="red")
        plt.plot(x_list, y_list, label="Newton", color="black")
        # plt.scatter(prediction, function2(prediction, ret, x, y), label="Newton PP", color="blue")
        plt.legend(loc="upper left")
        # yuanzu = calculate_data(self._xi, parameters)

    def validate(self):
        if len(self._fxi) != len(self._xi):
            raise ValueError("数据长度不一致!")

    def __str__(self):
        s = "Newton:"
        for a in self._fxi:
            s += str(a)
        for b in self._xi:
            s += str(b)
        return s


class Lagrange(object):
    def __init__(self):
        self._fxi = list(map(lambda x: float(x), request.form.get("fxi").split(",")))
        self._xi = list(map(lambda x: float(x), request.form.get("xi").split(",")))

    def validate(self):
        if len(self._fxi) != len(self._xi):
            raise ValueError("数据长度不一致!")

    def generate(self):
        from scipy.interpolate import lagrange
        a = lagrange(self._xi, self._fxi)
        tmp_x = np.arange(min(self._xi), max(self._xi)+0.1, 0.01)
        tmp_y = [a(x) for x in tmp_x]
        plt.scatter(self._xi, self._fxi, label="Lagrange Point", color="yellow")
        plt.plot(tmp_x, tmp_y, label="Lagrange", color="purple")
        plt.legend(loc="upper left")

    def __str__(self):
        s = "Lagrange:"
        for a in self._fxi:
            s += str(a)
        for b in self._xi:
            s += str(b)
        return s


class Hermite(object):
    def __init__(self):
        self._fxi = list(map(lambda x: float(x), request.form.get("fxi").split(",")))
        self._xi = list(map(lambda x: float(x), request.form.get("xi").split(",")))
        self._ffx = list(map(lambda x: float(x), request.form.get("ffx").split(",")))

    def validate(self):
        if len(self._fxi) != len(self._xi) or len(self._ffx) != len(self._xi):
            raise ValueError("数据长度不一致!")

    def generate(self):
        func = get_Hermite_interpolation(self._xi, self._fxi, self._ffx)
        plt.scatter(self._xi, self._fxi, label="Hermit Point", color="green")
        tmp_x = np.arange(min(self._xi), max(self._xi)+0.1, 0.01)
        tmp_y = [func(i) for i in tmp_x]
        plt.plot(tmp_x, tmp_y, label="Hermite", color="blue")
        plt.legend(loc="upper left")

    def __str__(self):
        s = "Hermite:"
        for a in self._fxi:
            s += str(a)
        for b in self._xi:
            s += str(b)
        return s
