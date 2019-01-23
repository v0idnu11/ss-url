# SSR Convertor

This script can convert ssr subscription to ss urls.

## Usage

```shell
$ python main.py --help
Usage: main.py [OPTIONS] URL

  This script request ssr subscription <URL> and then convert the response
  to ss urls.

Options:
  -D, --debug TEXT    Switch debug message on.
  -t, --token TEXT    Add http header [token] for authentication of request.
  -r, --rewrite TEXT  SS rule rewrite, support JSON format dict, for example:
                      `-r "{\"server_port\":12345}"` .
  -d, --domain TEXT   Subscription provider, currently only miaopasi is
                      supported.
  --help              Show this message and exit.

```

```shell
python main.py -r "{\"server_port\":12345,\"method\":\"aes-256-cfb\",\"password\":\"test\"}" "https://subscription.com/user/abcdefg?mu=443&filter_offline=1"
```