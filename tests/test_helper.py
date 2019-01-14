# -*- coding: utf-8 -*-
"""
    test_helper
"""

import unittest
from src.helper import ssr_parse, ss_gen


class TestHelper(unittest.TestCase):
    def test_ssr_parse(self):
        # us-7.mitsuha-node.com:443:auth_aes128_md5:aes-256-ctr:tls1.2_ticket_auth:dGVzdA/?obfsparam=dGVzdA&protoparam=dGVzdA&remarks=cml4Q2xvdWRfVVNfZm9yX01QUyAtIDQ0MyDnq6_lj6M&group=5Za15biV5pav572R57uc5Yqg6YCfLeWNleerr-WPo-WkmueUqOaItw
        url = 'ssr://dXMtNy5taXRzdWhhLW5vZGUuY29tOjQ0MzphdXRoX2FlczEyOF9tZDU6YWVzLTI1Ni1jdHI6dGxzMS4yX3RpY2tldF9hdXRoOmRHVnpkQS8/b2Jmc3BhcmFtPWRHVnpkQSZwcm90b3BhcmFtPWRHVnpkQSZyZW1hcmtzPWNtbDRRMnh2ZFdSZlZWTmZabTl5WDAxUVV5QXRJRFEwTXlEbnE2X2xqNk0mZ3JvdXA9NVphMTViaVY1cGF2NTcyUjU3dWM1WXFnNllDZkxlV05sZWVyci1XUG8tV2ttdWVVcU9hSXR3'
        target = {
                     "server": "us-7.mitsuha-node.com",
                     "server_port": 443,
                     "method": "aes-256-ctr",
                     "password": "test",
                     "protocol": "auth_aes128_md5",
                     "protocolparam": "test",
                     "obfs": "tls1.2_ticket_auth",
                     "obfsparam": "test",
                     "group": "喵帕斯网络加速-单端口多用户",
                     "remarks": "rixCloud_US_for_MPS - 443 端口",
                     "remarks_base64": "cml4Q2xvdWRfVVNfZm9yX01QUyAtIDQ0MyDnq6\/lj6M=",
                 }

        ret = ssr_parse(url)

        self.assertDictEqual(ret, target)

    def test_ss_gen(self):
        obj = {
            'server': 'hk-14.mitsuha-node.com',
            'server_port': 8379,
            'method': 'aes-256-ctr',
            'password': 'test',
            'remarks': 'test'
        }
        target = 'ss://YWVzLTI1Ni1jdHI6dGVzdA==@hk-14.mitsuha-node.com:8379/?#test'

        ret = ss_gen(obj)

        self.assertEqual(ret, target)


if __name__ == '__main__':
    unittest.main()
