def handle_response(user_message):
    p_message = user_message.strip().lower()

    if p_message == 'nguoimy':
        return 'https://cdn.discordapp.com/attachments/611535900111011842/1125473240974901369/357486595_837268411252769_1623317376413614827_n.mov'

    # Default response if no specific condition is met
    return 'Default response'
