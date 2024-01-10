from settings import *


def two_var_line(file, file_id):
    """
    Renders a basic line graph
    :param file: path to file
    :param file_id: id of file
    :return: saves image to temp/{file_id}.png
    """
    with open(file, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        row_len = len(data)
        x = [data[i][0] for i in range(1, row_len)]
        y = [data[i][1] for i in range(1, row_len)]
        plt.plot(x, y)
    plt.xlabel(data[0][0])
    plt.ylabel(data[0][1])
    plt.title("{0} vs. {1}".format(data[0][0], data[0][1]))
    plt.savefig('temp/{}.png'.format(file_id))
    plt.clf()


def two_var_bar(file, file_id):
    """
    Renders a basic bar graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    with open(file, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        row_len = len(data)
        x = [data[i][0] for i in range(1, row_len)]
        y = [data[i][1] for i in range(1, row_len)]
    plt.bar(x, y)
    plt.xlabel(data[0][0])
    plt.ylabel(data[0][1])
    plt.title("{0} vs. {1}".format(data[0][0], data[0][1]))
    plt.savefig('temp/{}.png'.format(file_id))
    plt.clf()


def two_var_scatter(file, file_id):
    """
    Renders a basic scatter graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    with open(file, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        row_len = len(data)
        x = [data[i][0] for i in range(1, row_len)]
        y = [data[i][1] for i in range(1, row_len)]
    plt.scatter(x, y)
    plt.xlabel(data[0][0])
    plt.ylabel(data[0][1])
    plt.title("{0} vs. {1}".format(data[0][0], data[0][1]))
    plt.savefig('temp/{}.png'.format(file_id))
    plt.clf()


def basic_pie(file, file_id):
    """
    Renders a basic pie graph
    :param file: path to file
    :param file_id: id of file
    :return: saves image to temp/{file_id}.png
    """
    names = []
    values = []
    with open(file, 'r') as csvfile:
        plotting = csv.reader(csvfile, delimiter=',')
        next(plotting)
        for row in plotting:
            names.append(row[0])
            values.append(row[1])
    colors = ['m', 'b', 'k', 'c', 'r']

    plt.pie(values, labels=names, colors=colors, startangle=90)
    plt.title('Pie Chart')
    plt.savefig('temp/{}.png'.format(file_id))

