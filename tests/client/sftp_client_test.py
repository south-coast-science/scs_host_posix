#!/usr/bin/env python3

"""
Created on 21 Mar 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.client.sftp_client import SFTPClient


# --------------------------------------------------------------------------------------------------------------------

client = None

# noinspection SpellCheckingInspection
try:
    client = SFTPClient('scs-rpi-006.local')
    print(client)

    client.connect(username='pi', password='Science1706')
    print(client)

    print("-")

    print(client.cwd() + ':')
    for item in client.listdir():
        print(item)
    print("-")

    path = 'SCS/conf'

    client.chdir(path)

    print(client.cwd() + ':')
    for item in client.listdir():
        print(item)
    print("-")

    print(client)
    print("=")

    print("get...")
    client.get('afe_baseline.json')
    print("-")

    print("put...")
    client.put('afe_baseline.json', remote_path='afe_baseline.upload')
    print("-")

    # client.close()
    #
    # client = SFTPClient('scs-bbe-003')
    # print(client)
    #
    # client.connect(username='scs')
    # print(client)
    #
    # client.close()

    # client.close()
    #
    # client = SFTPClient('sftp.airnowdata.org')
    # print(client)
    #
    # client.connect(username='UNEPdatauser', password='bA&y$EW06b')
    # print(client)
    #
    # client.close()

finally:
    if client:
        client.close()
