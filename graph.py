from settings import *


def two_var_set_plot_info(x_label, y_label, title, file_id):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig('temp/{}.png'.format(file_id))
    plt.clf()


def three_var_set_plot_info(title, file_id):
    plt.title(title)
    plt.savefig('temp/{}.png'.format(file_id))
    plt.clf()


def get_two_var_data(file):
    with open(file, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        row_len = len(data)
        x = [data[0][0]] + [float(data[i][0]) for i in range(1, row_len)]
        y = [data[0][1]] + [float(data[i][1]) for i in range(1, row_len)]
    return [x, y]


def get_three_var_data(file):
    with open(file, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        row_len = len(data)
        x = [data[0][0]] + [float(data[i][0]) for i in range(1, row_len)]
        y1 = [data[0][1]] + [float(data[i][1]) for i in range(1, row_len)]
        y2 = [data[0][2]] + [float(data[i][2]) for i in range(1, row_len)]
    return [x, y1, y2]


def two_var_line(file, file_id):
    """
    Renders a two-variable line graph
    :param file: path to file
    :param file_id: id of file
    :return: saves image to temp/{file_id}.png
    """
    data = get_two_var_data(file)
    plt.plot(data[0][1:], data[1][1:])
    two_var_set_plot_info(data[0][0], data[1][0], "{0} vs. {1}".format(data[0][0], data[1][0]), file_id)


def three_var_line(file, file_id):
    data = get_three_var_data(file)
    plt.plot(data[0][1:], data[1][1:], data[2][1:])
    plt.xlabel(data[0][0])
    plt.ylabel(data[1][0])
    plt.twinx().set_ylabel(data[2][0])
    three_var_set_plot_info(f"{data[0][0]} vs. {data[1][0]} vs. {data[2][0]}", file_id)


def two_var_bar(file, file_id):
    """
    Renders a two-variable bar graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    data = get_two_var_data(file)
    plt.bar(data[0][1:], data[1][1:])
    two_var_set_plot_info(data[0][0], data[1][0], "{0} vs. {1}".format(data[0][0], data[1][0]), file_id)


def two_var_scatter(file, file_id):
    """
    Renders a two-variable scatter graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    data = get_two_var_data(file)
    plt.scatter(data[0][1:], data[1][1:])
    two_var_set_plot_info(data[0][0], data[1][0], "{0} vs. {1}".format(data[0][0], data[1][0]), file_id)


def three_var_scatter(file, file_id):
    data = get_three_var_data(file)
    print(data)
    fig, ax1 = plt.subplots()
    ax1.scatter(data[0][1:], data[1][1:], color='b')
    ax2 = ax1.twinx()
    ax2.scatter(data[0][1:], data[2][1:], color='r')
    ax1.set_xlabel(data[0][0])
    ax1.set_ylabel(data[1][0])
    ax2.set_ylabel(data[2][0])
    three_var_set_plot_info(f"{data[0][0]} vs. {data[1][0]} vs. {data[2][0]}", file_id)


def basic_pie(file, file_id):
    """
    Renders a basic pie graph
    :param file: path to file
    :param file_id: id of file
    :return: saves image to temp/{file_id}.png
    """
    with open(file, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        names = data[0]
        values = data[1]
    plt.pie(values, labels=names)
    plt.title('DisGraph Pie Chart')
    plt.savefig('temp/{}.png'.format(file_id))
    plt.clf()

