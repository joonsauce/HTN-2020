import asyncio
from settings import *
from graph import *


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
        await ctx.send('Timed out. Pleas try again.')
        return
    else:
        return msg


async def check_graph_type(ctx, msg, rc_len):
    if not msg.isnumeric():
        await ctx.send("Graph type must be inputted as an integer. Please try again.")
        return
    else:
        if not float(msg).is_integer():
            await ctx.send("Graph type must be inputted as an integer. Please try again.")
            return
        msg = int(msg)
        return msg


def initial_analysis(ctx, file_path):
    with open(file_path, 'r') as data:
        # check number of rows and columns
        # throw problems if number of rows/columns is too large (greater than 3)
        # return number of rows/columns and save direction
        reader = csv.reader(data)
        row_len = len(list(reader))
        row_type = False
        if row_len > 3:
            reader1, reader2 = itertools.tee(data)
            col_len = len(next(reader1))
            del reader1
            if col_len == 2:
                await ctx.send("Please choose a graph type from the following: X vs Y (line, 1), X vs Y (scatter, 2), "
                               "X vs Y (bar, 3), Pie (4)")
            # 3 var graphs will be implemented later
            # elif col_len == 3:
            #     await ctx.send("Please choose a graph type from the following: X vs Y1 and Y2 (line, 1), "
            #                    "X vs Y1 and Y2 (bar,2 )")
            else:
                await ctx.send("File format is invalid. Please run `d!help` to find out more about the file format.")
                return
            row_type = False
        # 3 var graphs will be implemented later
        # elif row_len == 3:
        #     await ctx.send("Please choose a graph type from the following: X vs Y1 and Y2 (line, 1), "
        #                    "X vs Y1 and Y2 (bar,2 )")
        #     row_type = True
        elif row_len == 2:
            await ctx.send("Please choose a graph type from the following: X vs Y (line, 1), X vs Y (scatter, 2), "
                           "X vs Y (bar, 3), Pie(4)")
            row_type = True
        msg = await wait_for_message(ctx)
        if msg:
            if row_type:
                await check_graph_type(ctx, msg, row_len)
            else:
                await check_graph_type(ctx, msg, col_len)
            # should create graph here - make new function
        else:
            await ctx.send("Timed out. Please try again.")
            return

