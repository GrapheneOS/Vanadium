#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-2.0

import argparse
import ssl
import sys
import urllib.request


def filter_list_download(args) -> int:
    urls = sorted(list(set(args.urls)))
    for url in urls:
        if not url.startswith("https://"):
            continue
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.minimum_version = ssl.TLSVersion.TLSv1_3
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(url=req, context=context, timeout=30) as res:
            if res.status != 200:
                return -1
            while True:
                buf = res.read(4096)
                if not buf:
                    break
                args.output.write(buf)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--urls', nargs='+',
                        help='Relative path to folders to search for duplicate includes check_in.')
    parser.add_argument('--output', required=True, type=argparse.FileType('wb'), default=sys.stdout)
    sys.exit(filter_list_download(parser.parse_args(sys.argv[1:])))
