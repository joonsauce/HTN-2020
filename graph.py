from settings import *


def set_plot_info(x_label, y_label, title, file_id):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig('temp/{}.png'.format(file_id))
    plt.clf()


def get_two_var_data(file):
    with open(file, 'r') as csvfile:
        data = list(csv.reader(csvfile))
        row_len = len(data)
        x = [data[i][0] for i in range(row_len)]
        y = [data[i][1] for i in range(row_len)]
    return [x, y]


def two_var_line(file, file_id):
    """
    Renders a basic line graph
    :param file: path to file
    :param file_id: id of file
    :return: saves image to temp/{file_id}.png
    """
    data = get_two_var_data(file)
    plt.plot(data[0][1:], data[1][1:])
    set_plot_info(data[0][0], data[1][0], "{0} vs. {1}".format(data[0][0], data[1][0]), file_id)


def two_var_bar(file, file_id):
    """
    Renders a basic bar graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    data = get_two_var_data(file)
    plt.bar(data[0][1:], data[1][1:])
    set_plot_info(data[0][0], data[1][0], "{0} vs. {1}".format(data[0][0], data[1][0]), file_id)


def two_var_scatter(file, file_id):
    """
    Renders a basic scatter graph
    :param file: path to file
    :return: saves image to temp/{file_id}.png
    """
    data = get_two_var_data(file)
    plt.scatter(data[0][1:], data[1][1:])
    set_plot_info(data[0][0], data[1][0], "{0} vs. {1}".format(data[0][0], data[1][0]), file_id)


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

