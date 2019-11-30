async def ex(args, message, client, invoke):
    echo_msg = ""
    if len(args) > 0:
        for arg in args:
            echo_msg = echo_msg + " {}".format(arg)
    await message.channel.send(":loudspeaker: "+echo_msg)