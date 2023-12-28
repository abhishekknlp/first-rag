import chainlit as cl


@cl.on_chat_start
async def start():
    # Send the first message without the elements
    content = "Here is image1, a nice image of a cat! As well as text1 and text2!"

    await cl.Message(
        content=content,
    ).send()