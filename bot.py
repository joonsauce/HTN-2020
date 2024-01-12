from functions import *
from help import *

# graph_file command: given a file, analyzes data and graphs it
@bot.command()
async def graph_file(ctx):
    await ctx.send(f"Please upload a file with `{','.join(supported_file_types)}` file extensions")
    msg = await wait_for_message(ctx)
    if msg:
        if msg.attachments:
            file_name = msg.attachments[0].filename
            file_id = uuid.uuid4()
            file_path = 'temp/{0}.csv'.format(file_id)
            if any([file_name.endswith(i) for i in supported_file_types]):
                if not file_name.endswith('.csv'):
                    convert_to_csv(msg.attachments)
                else:
                    await msg.attachments[0].save(file_path)
                await initial_analysis(ctx, file_path, file_id)
                try:
                    os.remove(file_path)
                    os.remove('temp/{0}.png'.format(file_id))
                except:
                    print('Manual deletion required')
            else:
                await ctx.send("Invalid file type. Please attach a file with `{0}` extensions and try again.".format(','.join(supported_file_types)))
        else:
            await ctx.send("No files attached. Please try again.")

bot.run(bot_token)
