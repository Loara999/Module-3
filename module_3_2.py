def send_email(message, recipient, *, sender='university.help@gmail.com'):
    email_ending = ('.com', '.ru', '.net')
    check_email = True
    if '@' not in recipient or '@' not in sender:
        check_email = False
    elif recipient[recipient.find('.', len(recipient) - 4, len(recipient)):] not in email_ending or \
            sender[sender.find('.', len(sender) - 4, len(sender)):] not in email_ending:
        check_email = False
    if check_email == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        print(f'Содержание письма: "{message}"')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        print(f'Содержание письма: "{message}"')


mail_test = "berry@gmail.com"
mail2_test = "cherry@mail.ru"
send_email('Привет, ягодка!', mail_test)
