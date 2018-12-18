#!/usr/bin/env python3

import os
import sys
import json
import argparse
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deploy an Awingu environment')
    parser.add_argument('--dns', type=str, required=True)
    parser.add_argument('--domain', type=str, required=True)
    parser.add_argument('--netbios', type=str, required=True)
    parser.add_argument('--admin-pass', type=str, required=True)
    parser.add_argument('--domain-admin', type=str, required=True)
    parser.add_argument('--domain-pass', type=str, required=True)
    parser.add_argument('--app-server-count', type=int, required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    process = subprocess.Popen(['unzip', 'setup_awingu.zip'])
    process.wait()

    json_data = open('/etc/awingu/appliance_version.json').read()
    data = json.loads(json_data)
    awingu_version = data['fields']['number']
    package_version = ''.join(awingu_version.split('.')[:2])
    cwd = os.getcwd()
    sys.path.append('{}/awingu{}'.format(cwd, package_version))

    from setup_awingu import setup

    args.ad_server_name = 'awingu-ad'
    args.app_server_prefix = 'awingu-app'

    setup(args)
