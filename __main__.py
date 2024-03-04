try:
    from ping3 import ping
    from send_email import SendEmail

    send_email = SendEmail(
        'Relatório de Ip',
        '@from.com',
        '@to.com',
        'password',
        'smtp.gmail.com',
        '587'
    )

    IP_TESTING_LIST = ['8.8.8.8', 'lfjlas']
    online_ip_list = IP_TESTING_LIST[:]
    ip_list_not_online = []

    while True:
        for ip in IP_TESTING_LIST:
            for counter in range(600):
                is_online = ping(ip)
                if is_online:
                    break
            if is_online and ip not in online_ip_list:
                send_email.get_body('online.html', {'ip': ip})
                send_email.send()
                online_ip_list.append(ip)
                ip_list_not_online.remove(ip)
            elif not is_online and ip not in ip_list_not_online:
                send_email.get_body_and_ip('offline.html', ip)
                send_email.send()
                online_ip_list.remove(ip)
                ip_list_not_online.append(ip)
except Exception as error:
    with open('error.txt', 'w') as log:
        log.write(str(error))
