#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-2.0

import argparse
import base64
import hashlib
import os
import ssl
import sys
import urllib.request


def FetchAndGenerateFilterList(args):
    urls = sorted(list(set(args.urls)))
    hasher = hashlib.new('sha256')
    for url in urls:
        if not url.startswith("https://"):
            continue
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.minimum_version = ssl.TLSVersion.TLSv1_3
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(url=req, context=context, timeout=30) as res:
            while True:
                buf = res.read(4096)
                if not buf:
                    break
                args.output.write(buf)
                hasher.update(buf)
    with open('.'.join([args.output.name, 'sha256']), 'w') as f:
        f.write(hasher.hexdigest())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--urls', nargs='+',
                        help='Relative path to folders to search for duplicate includes check_in.')
    parser.add_argument('--output', required=True, type=argparse.FileType('wb'), default=sys.stdout)
    FetchAndGenerateFilterList(parser.parse_args(sys.argv[1:]))
