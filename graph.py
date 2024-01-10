from settings import *

variables = {
    'x': [],
    'y': []
}

X = []
Y = []


def basic_line(file, file_id):
    """
    Renders a basic line graph
    :param file: path to file
    :param file_id: id of file
    :return: saves image to temp/{file_id}.png
    """
    lines_num = 2
    var = {}
    for i in range(1, lines_num+1):
        var[i] = ([], [])

    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        # Skip first line (values)
        lines_num = len(next(plots)) - 1
        next(plots)
        for row in plots:
            for j in range(1, len(row)):
                var[j][0].append(int(row[0]))
                var[j][1].append(int(row[j]))

    for k in range(lines_num):
        plt.plot(var[k+1][0], var[k+1][1])

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('temp/{}.png'.format(file_id))


def basic_bar(file, file_id):
    """
    Renders a basic bar graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    with open(file, 'r') as csvfile:
        plotting = csv.reader(csvfile, delimiter=',')
        next(plotting)
        for row in plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))

    plt.bar(variables['x'], variables['y'], label='Bars1')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('temp/{}.png'.format(file_id))


def basic_scatter(file, file_id):
    """
    Renders a basic scatter graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    with open(file, 'r') as csvfile:
        plotting = csv.reader(csvfile, delimiter=',')
        next(plotting)
        for row in plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))
    plt.scatter(variables['x'], variables['y'], label='Scatter', color='b')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('temp/{}.png'.format(file_id))


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

