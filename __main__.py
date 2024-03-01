try:
    from ping3 import ping
    from send_gmail import SendEmail

    send_gmail = SendEmail(
        'Relatório de Ip',
        '@from.com',
        '@to.com',
        'password'
    )

    IP_TESTING_LIST = ['8.8.8.8', 'lfjlas']
    online_ip_list = IP_TESTING_LIST[:]
    ip_list_not_online = []

    while True:
        for ip in IP_TESTING_LIST:
            is_online = ping(ip)
            if is_online and ip not in online_ip_list:
                send_gmail.get_body_and_ip('online.html', ip)
                send_gmail.send()
                online_ip_list.append(ip)
                if ip in ip_list_not_online:
                    ip_list_not_online.remove(ip)
            elif not is_online and ip not in ip_list_not_online:
                send_gmail.get_body_and_ip('offline.html', ip)
                send_gmail.send()
                online_ip_list.remove(ip)
                ip_list_not_online.append(ip)
except Exception as error:
    with open('log.txt', 'w') as log:
        log.write(str(error))
