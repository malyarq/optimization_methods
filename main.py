def f(x):
    return (x * x) + (6 * x) + 12


def svenn(x0, t):
    x = [x0]
    k = 0
    f1 = f(x[0] - t)
    f2 = f(x[0])
    f3 = f(x[0] + t)
    if f1 >= f2 and f3 >= f2:
        a0 = x[0] - t
        b0 = x[0] + t
    elif f1 <= f2 and f3 <= f2:
        print('Выберите другое x0')
    else:
        if f1 >= f2 >= f3:
            delta = t
            a0 = x[0]
            x.append(x[0] + t)
            k = 1
        elif f1 <= f2 <= f3:
            delta = 0 - t
            b0 = x[0]
            x.append(x[0] - t)
            k = 1
        while True:
            x.append(x[k] + pow(2, k) * delta)
            if f(x[k + 1]) < f(x[k]) and delta == t:
                a0 = x[k]
                k += 1
            if f(x[k + 1]) < f(x[k]) and delta == -t:
                b0 = x[k]
                k += 1
            if f(x[k + 1]) >= f(x[k]):
                if delta == t:
                    b0 = x[k + 1]
                    break
                elif delta == -t:
                    a0 = x[k + 1]
                    break
    return a0, b0


def popolam(a0, b0, e):
    global x
    a = [a0]
    b = [b0]
    xc = []
    y = []
    z = []
    L = []
    k = 0
    while True:
        xc.append((a[k] + b[k]) / 2)
        L.append(abs(b[k] - a[k]))
        fxc = f(xc[k])
        y.append(a[k] + L[k] / 4)
        z.append(b[k] - L[k] / 4)
        fy = f(y[k])
        fz = f(z[k])
        if fy < fxc:
            b.append(xc[k])
            a.append(a[k])
            xc.append(y[k])
            L.append(abs(b[k + 1] - a[k + 1]))
        else:
            if fz < fxc:
                a.append(xc[k])
                b.append(b[k])
                xc.append(z[k])
            elif fz >= fxc:
                a.append(y[k])
                b.append(z[k])
                xc.append(xc[k])
        if L[(k + 1)] <= e:
            x = xc[(k + 1)]
            break
        elif L[(k + 1)] > e:
            k += 1


def dihotomia(a0, b0, e, m):
    global x
    a = [a0]
    b = [b0]
    y = []
    z = []
    L = []
    k = 0
    L.append(abs(b[k] - a[k]))
    while True:
        y.append((a[k] + b[k] - m) / 2)
        fy = f(y[k])
        z.append((a[k] + b[k] + m) / 2)
        fz = f(z[k])
        if fy <= fz:
            a.append(a[k])
            b.append(z[k])
            L.append(abs(b[k + 1] - a[k + 1]))
        else:
            a.append(y[k])
            b.append(b[k])
            L.append(abs(b[k + 1] - a[k + 1]))
        if L[k + 1] <= e:
            x = (a[k + 1] + b[k + 1]) / 2
            break
        else:
            k += 1


def gold(a0, b0, e):
    global x
    a = [a0]
    b = [b0]
    y = []
    z = []
    k = 0
    y.append(a[k] + 0.38196 * (b[k] - a[k]))
    z.append(a[k] + b[k] - y[k])
    while True:
        fy = f(y[k])
        fz = f(z[k])
        if fy <= fz:
            a.append(a[k])
            b.append(z[k])
            y.append(a[k + 1] + b[k + 1] - y[k])
            z.append(y[k])
        else:
            a.append(y[k])
            b.append(b[k])
            y.append(z[k])
            z.append(a[k + 1] + b[k + 1] - z[k])
        delta = abs(a[k + 1] - b[k + 1])
        if delta <= e:
            x = (a[k + 1] + b[k + 1]) / 2
            break
        else:
            k += 1


global x
a0, b0 = svenn(1, 2)
e = 0.1
m = 0.05
print(f'Начальный интервал неопределенности: [{a0}, {b0}] (метод Свенна)')
popolam(a0, b0, e)
print(f'Минимум функции составляет {f(x)} и достигается в точке х = {x} (метод деления интервала пополам)')
dihotomia(a0, b0, e, m)
print(f'Минимум функции составляет {f(x)} и достигается в точке х = {x} (метод дихотомии)')
gold(a0, b0, e)
print(f'Минимум функции составляет {f(x)} и достигается в точке х = {x} (метод золотого сечения)')
