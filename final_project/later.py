@bot.message_handler(content_types=['photo'])
def ai_class(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    with open("images/"+file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    result = get_class("images/"+file_name)
    bot.reply_to(message, result)


