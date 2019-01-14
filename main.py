# -*- coding: utf-8 -*-
"""
    main
"""

from click import echo, command, option, argument, STRING
from requests import get
from requests.exceptions import RequestException, ConnectionError
from src import helper, miaopasi


@command()
@option('-D', '--debug', default=False, help='Switch debug message on.')
@option('-t', '--token', type=STRING, default='', help='Add http header [token] for authentication of request.')
@option('-d', '--domain', type=STRING, default='miaopasi', help='Subscription provider, currently only miaopasi is supported.')
@argument('url', type=STRING)
def cli(debug, token, domain, url):
    """This script request ssr subscription <URL> and then convert the response to ss urls."""
    try:
        headers = {'User-Agent': 'ss_url_convertor'}
        if token:
            headers['token'] = token
        res = get(url, headers=headers)

        # TODO Support more domain
        ss_urls = miaopasi.convert(res.content, debug)
        echo(ss_urls)

    except ConnectionError as err:
        helper.print_error(type(err).__name__ + ', plz check your url, proxy works correctly .')
    except RequestException as err:
        helper.print_error(type(err).__name__ + ', you need fix that problem first .')


if __name__ == '__main__':
    cli()
