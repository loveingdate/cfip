import re

PATH = './ip/'
    
if "__name__==__main__":#主程序开始

    with open(f'{PATH}ALLIP.txt', 'r', encoding='utf-8') as f:
        ip_all = f.read()
    ip_list = re.split(r'\n+',ip_all)

    with open(f'{PATH}node.txt', 'r', encoding='utf-8') as f:
        ip_node_all = f.read()
    ip_node_list = re.split(r'\n+',ip_node_all)
    
    alive_ip = []
    for ip in ip_list:
        if ip == '':
            continue
        if '#' in ip:
            ipaddr = ip.split("#")[0]
        else:
            ipaddr = ip
        for node in ip_node_list:
            if ipaddr in node:
                alive_ip.append(ip)
                print(ip)
                continue
    #分区域保存
    hkip = []
    jpip = []
    sgip = []
    krip = []
    usip = []
    for ip in alive_ip:
        if 'HK' in ip or 'TW' in ip:
            hkip.append(ip)
        if 'JP' in ip:
            jpip.append(ip)
        if 'SG' in ip:
            sgip.append(ip)
        if 'KR' in ip:
            krip.append(ip)
        if 'US' in ip:
            usip.append(ip)
    #保存
    if hkip and jpip and sgip and krip and usip:
        alive_ip = '\n'.join(alive_ip)
        with open(f'{PATH}/checked/ipALL.txt', 'w', encoding='utf-8') as f:
            f.write(alive_ip)
    if hkip:
        hkip = '\n'.join(hkip)
        with open(f'{PATH}/checked/ipHK.txt', 'w', encoding='utf-8') as f:
            f.write(hkip)
    if jpip:
        jpip = '\n'.join(jpip)
        with open(f'{PATH}/checked/ipJP.txt', 'w', encoding='utf-8') as f:
            f.write(jpip)
    if sgip:
        sgip = '\n'.join(sgip)
        with open(f'{PATH}/checked/ipSG.txt', 'w', encoding='utf-8') as f:
            f.write(sgip)
    if krip:
        krip = '\n'.join(krip)
        with open(f'{PATH}/checked/ipKR.txt', 'w', encoding='utf-8') as f:
            f.write(krip)
    if usip:
        usip = '\n'.join(usip)
        with open(f'{PATH}/checked/ipUS.txt', 'w', encoding='utf-8') as f:
            f.write(usip)
    

    
