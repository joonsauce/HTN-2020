from graph import *
from settings import *


def convert_to_csv(file):
    if file.filename.endswith('.xlsx'):
        file.attachments[0].save('temp/file.xlsx')
        file = pandas.read_excel('temp/file.xlsx')
        file.to_csv('temp/file.csv')
    elif file.filename.endswith('.xls'):
        file.attachments[0].save('temp/file.xls')
        file = pandas.read_excel('temp/file.xls')
        file.to_csv('temp/file.csv')


async def wait_for_message(ctx):
    try:
        msg = await bot.wait_for('message', timeout=60)
    except asyncio.TimeoutError:
        await ctx.send('Timed out. Please try again.')
        return None
    else:
        return msg


async def check_graph_type(ctx, max_val):
    msg = await wait_for_message(ctx)
    if msg:
        msg = msg.content
        if not msg.isnumeric():
            await ctx.send("Graph type must be inputted as an integer. Please try again.")
            return -1
        if not float(msg).is_integer():
            await ctx.send("Graph type must be inputted as an integer. Please try again.")
            return -1
        msg = int(msg)
        if msg <= 0 or msg > max_val:
            await ctx.send("Invalid graph type")
            return -1
        return msg
    return -1


def verify_data(data: list, row_len: int, col_len: int) -> bool:
    return all([len(data[i]) == col_len for i in range(row_len)])


async def initial_analysis(ctx, file_path, file_id):
    with open(file_path, 'r') as data:
        # check number of rows and columns
        # throw problems if number of rows/columns is too large (greater than 3)
        # return number of rows/columns and save direction
        data = list(csv.reader(data))
        row_len = len(data)
        if row_len <= 1:
            await ctx.send("Data invalid. Please run `d!help` for more information "
                           "on formatting your data for graphing")
            return
        col_len = len(data[0])
        if not verify_data(data, row_len, col_len):
            await ctx.send("Data invalid. Please run `d!help` for more information "
                           "on formatting your data for graphing")
            return
        if row_len == 2:
            await ctx.send("Please choose a graph type: Pie (1)")
            x = await check_graph_type(ctx, 1)
            if x == 1:
                basic_pie(file_path, file_id)
        else:
            if col_len == 2:
                await ctx.send("Please choose a graph type: X vs Y *line* (1), X vs Y *scatter* (2), "
                               "X vs Y *bar* (3)")
                x = await check_graph_type(ctx, 3)
                if x == 1:
                    basic_line(file_path, file_id)
                elif x == 2:
                    basic_scatter(file_path, file_id)
                elif x == 3:
                    basic_bar(file_path, file_id)
                else:
                    return
        await ctx.send(file=discord.File(open('temp/{0}.png'.format(file_id), 'rb'), '{0}.png'.format(file_id)))

