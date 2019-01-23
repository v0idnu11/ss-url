# -*- coding: utf-8 -*-
"""
    main
"""

import json

from click import echo, command, option, argument, STRING
from requests import get
from requests.exceptions import RequestException, ConnectionError
from src import helper, miaopasi


@command()
@option('-D', '--debug', default=False, help=r'Switch debug message on.')
@option('-t', '--token', type=STRING, default='', help=r'Add http header [token] for authentication of request.')
@option('-r', '--rewrite', type=STRING, default='', help=r'SS rule rewrite, support JSON format dict, for example: `-r "{\"server_port\":12345}"` .')
@option('-d', '--domain', type=STRING, default='miaopasi', help=r'Subscription provider, currently only miaopasi is supported.')
@argument('url', type=STRING)
def cli(debug, token, domain, rewrite, url):
    """This script request ssr subscription <URL> and then convert the response to ss urls."""
    echo('loading ...')

    try:
        headers = {'User-Agent': 'ss_url_convertor'}
        if token:
            headers['token'] = token
        res = get(url, headers=headers)

        if rewrite:
            rewrite = json.loads(rewrite)

        # TODO Support more domain
        if not res.content:
            helper.print_error('ResponseError, server response empty content .')
            return False

        ss_urls = miaopasi.convert(res.content, rewrite, debug)
        echo(ss_urls)

    except ConnectionError as err:
        helper.print_error(type(err).__name__ + ', plz check your url, proxy works correctly .')
    except RequestException as err:
        helper.print_error(type(err).__name__ + ', you need fix that problem first .')


if __name__ == '__main__':
    cli()
