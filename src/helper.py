# -*- coding: utf-8 -*-
"""
    helper
"""

import base64
from click import echo, style
from re import compile
from urllib.parse import quote_plus

re_obfs = compile(r'obfsparam=([\w\-_]+)&protoparam=([\w\-_]+)&remarks=([\w\-_]+)&group=([\w\-_]+)')


def print_error(message):
    echo(style(message, bg='red', fg='white'), err=True)


def base64_decode(raw_data):
    """
    Base64 decode with url safe.

    :param raw_data:
    :return:
    """
    is_str = True

    # If data is not string, decode to string first.
    if type(raw_data).__name__ != 'str':
        is_str = False
        raw_data = raw_data.decode()

    if len(raw_data) % 4:
        raw_data += '=' * (4 - len(raw_data) % 4)

    decoded_data = base64.urlsafe_b64decode(raw_data.encode())

    # If input is string return string, otherwise return bytes.
    return decoded_data.decode() if is_str else decoded_data


def base64_encode(raw_data):
    """
    Base64 decode with '/' escaped.

    :param raw_data:
    :return:
    """
    is_str = True

    # If data is not string, decode to string first.
    if type(raw_data).__name__ != 'str':
        is_str = False
    else:
        raw_data = raw_data.encode()

    encoded_data = base64.b64encode(raw_data).decode()
    encoded_data = encoded_data.replace('/', '\\/')

    # If input is string return string, otherwise return bytes.
    return encoded_data if is_str else encoded_data.encode()


def ssr_parse(ssr_url):
    """
    ssr://base64(abc.xyz:12345:auth_sha1_v2:rc4-md5:tls1.2_ticket_auth:{base64(password)}/?obfsparam={base64(混淆参数(网址))}&protoparam={base64(混淆协议)}&remarks={base64(节点名称)}&group={base64(分组名)})

    :param ssr_url:
    :return:
    """
    data = ssr_url.replace('ssr://', '').encode()
    data = base64_decode(data).decode()
    [part1, part2] = data.split('/?')
    groups1 = part1.split(':')
    groups2 = re_obfs.match(part2).groups()

    remarks = base64_decode(groups2[2])
    ssr_obj = {
        'server': groups1[0],
        'server_port': int(groups1[1]),
        'method': groups1[3],
        'password': base64_decode(groups1[5]),
        'protocol': groups1[2],
        'protocolparam': base64_decode(groups2[1]),
        'obfs': groups1[4],
        'obfsparam': base64_decode(groups2[0]),
        'group': base64_decode(groups2[3]),
        'remarks': remarks,
        'remarks_base64': base64_encode(remarks)
    }

    return ssr_obj


def ss_gen(ss_obj):
    """
    ss://base64(method:password)@domain:port/?#remarks

    :param url:
    :return:
    """
    part1 = base64.urlsafe_b64encode((ss_obj['method'] + ':' + ss_obj['password']).encode()).decode()
    remarks = quote_plus(ss_obj['remarks']).replace('+', '%20')
    return 'ss://%s@%s:%s/?#%s' % (part1, ss_obj['server'], str(ss_obj['server_port']), remarks)


def ssr_to_ss(ssr_obj):
    """
    Convert ssr dict to ss dict

    :param data:
    :return:
    """
    return {
        'server': ssr_obj['server'],
        'server_port': ssr_obj['server_port'],
        'method': ssr_obj['method'],
        'password': ssr_obj['password'],
        'remarks': ssr_obj['remarks']
    }
