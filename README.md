# SSR Convertor

This script can convert ssr subscription to ss urls.

## Usage

```shell
$ python main.py --help
Usage: main.py [OPTIONS] URL

  This script request ssr subscription <URL> and then convert the response
  to ss urls.

Options:
  -D, --debug TEXT   Switch debug message on.
  -t, --token TEXT   Add http header [token] for authentication of request.
  -d, --domain TEXT  Subscription provider, currently only miaopasi is
                     supported.
  --help             Show this message and exit.
```