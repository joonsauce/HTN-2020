from settings import *

@bot.command()
async def help(ctx, *, msg=''):
    embed = discord.Embed(color=None)
    embed.set_author(name="DisGraph Help")
    if not msg:
        embed.add_field(name="graph_file", value="Generates a graph based on the contents of a data file. "
                                                 "To make a pie graph, the first row must be the names of the "
                                                 "associated data, and the second row must be the numerical data. "
                                                 "To make a 2-var bar/line/scatter graph, the first row must include "
                                                 "the variable names and the data must follow below. Usage: "
                                                 "d!graph_file", inline=False)
    elif msg == 'graph_file':
        embed.add_field(name="graph_file", value="Generates a graph based on the contents of a data file. "
                                                 "To make a pie graph, the first row must be the names of the "
                                                 "associated data, and the second row must be the numerical data. "
                                                 "To make a 2-var bar/line/scatter graph, the first row must include "
                                                 "the variable names and the data must follow below. Usage: "
                                                 "d!graph_file", inline=False)
    else:
        embed.add_field(name="Command `{0}` does not exist".format(msg), value="", inline=True)

    await ctx.send(embed=embed)