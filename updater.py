#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2017-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import hashlib
import os
import threading

try:
    from urllib.request import urlopen, urlretrieve
except ImportError:
    # noinspection PyUnresolvedReferences
    from urllib import urlopen, urlretrieve


def update_rir_database(rir_database_url):
    rir_database_path = os.path.join("iptocc", rir_database_url.split("/")[-1])
    try:
        print("Downloading RIR database {}".format(rir_database_path))
        urlretrieve(rir_database_url, filename=rir_database_path)
        print("RIR database downloaded: {}".format(rir_database_url))
    except IOError:
        pass


def calculate_hash(hash_md5, path):
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)


def update_rir_databases():
    threads = []
    for rir_database_url in (
        "ftp://ftp.afrinic.net/stats/afrinic/delegated-afrinic-extended-latest",
        "ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest",
        "ftp://ftp.apnic.net/public/apnic/stats/apnic/delegated-apnic-extended-latest",
        "ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest",
        "ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest",
    ):
        thread = threading.Thread(target=update_rir_database, args=(rir_database_url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("RIR database update finished")


if __name__ == "__main__":
    update_rir_databases()
