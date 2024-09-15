# среднее арифметическое
def ar_mean(numbers):
    averageNumbers = sum(numbers) / len(numbers)
    return averageNumbers


# медиана
def median(numbers):
    n = len(numbers)
    index = n // 2
    if n % 2 != 0:
        return numbers[index]
    else:
        return (numbers[index] + numbers[index - 1]) / 2


def scope(numbers):
    biggest = numbers[len(numbers) - 1]
    smaller = numbers[0]
    scp = biggest - smaller
    scopes = [biggest, smaller, scp]
    return scopes


# def moda(numbers):