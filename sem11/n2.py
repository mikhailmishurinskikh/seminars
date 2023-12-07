from statistics import mean
def l_s(xdata, ydata):
    try:
        if len(xdata) != len(ydata):
            raise TypeError('number of x values should be equal number of y values')
        a = (sum([x * y for x, y in zip(xdata, ydata)]) - mean(ydata) * sum(xdata)) / (sum([x**2 for x in xdata]) - mean(xdata) * sum(xdata))
        b = mean(ydata) - a * mean(xdata)
    except TypeError:
        return 'invalid values'
    except ZeroDivisionError:
        return 'invalid values'
    return (round(a,2), round(b,2))
