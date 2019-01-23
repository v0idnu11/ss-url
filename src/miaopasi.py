# -*- coding: utf-8 -*-
"""
    mps
"""


from .helper import base64_decode, ssr_parse, ss_gen, ssr_to_ss


def convert(data, rewrite=None, debug=False):
    """
    Convert subscribe feed to ss urls.

    :param data:
    :param rewrite:
    :param debug:
    :return:
    """
    records = base64_decode(data).decode().split('\n')

    ss_urls = []
    error_count = 0
    for ssr_url in records:
        if ssr_url:
            try:
                ssr_obj = ssr_parse(ssr_url)
                ss_obj = ssr_to_ss(ssr_obj, rewrite)
                ss_url = ss_gen(ss_obj)
                ss_urls.append(ss_url)

            except Exception as err:
                if debug:
                    print(err)
                    error_count += 1

    if debug:
        print('Error count: %d' % error_count)
        print('Correct count: %d' % len(ss_urls))

    return '\n'.join(ss_urls)
