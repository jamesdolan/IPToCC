#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2017-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import os
import threading
from urllib.request import urlretrieve
from ipaddress import IPv4Address, IPv6Network
from typing import Union, Tuple

import pandas

from iptocc import IPTOCC_DIR


def update_rir_database(rir_database_url):
    rir_database_path = os.path.join("iptocc", rir_database_url.split("/")[-1])
    try:
        print("Downloading RIR database {}".format(rir_database_path))
        urlretrieve(rir_database_url, filename=rir_database_path)
        print("RIR database downloaded: {}".format(rir_database_url))
    except IOError:
        pass


def read_rir_databases():
    headers = [
        "Registry",
        "Country Code",
        "Type",
        "Start",
        "Value",
        "Date",
        "Status",
        "Extensions",
    ]
    for rir_filename in os.listdir(IPTOCC_DIR):
        if rir_filename.startswith("delegated-") and rir_filename.endswith(
            "-extended-latest"
        ):
            rir_database_path = os.path.join(IPTOCC_DIR, rir_filename)
            yield pandas.read_csv(
                rir_database_path,
                delimiter="|",
                comment="#",
                names=headers,
                dtype=str,
                keep_default_na=False,
                na_values=[""],
                encoding="utf-8",
            )[4:]


def convert_to_ip_object(
    row: dict,
) -> Union[Tuple[IPv4Address, IPv4Address], Tuple[IPv6Network, str], Tuple[str, str]]:
    if row["Type"] == "ipv4":
        start = IPv4Address(row["Start"])
        return start, start + int(row["Value"])
    elif row["Type"] == "ipv6":
        return IPv6Network(row["Start"] + "/" + row["Value"]), ""
    return row["Start"], ""


def make_rir_database() -> pandas.DataFrame:
    print("Loading RIR databases")
    rir_db = pandas.concat(read_rir_databases())
    rir_db = rir_db[
        (
            (rir_db["Type"] == "ipv4")
            | (rir_db["Type"] == "ipv6")
        )
        & (rir_db["Type"] != "*")
    ]
    rir_db[["Start", "End"]] = rir_db.apply(
        convert_to_ip_object, axis=1, result_type="expand"
    )
    print("RIR databases loaded")
    return rir_db


def update_rir_databases():
    threads = []
    print("Downloading source databases")
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
    print("Converting to Pandas databases")
    make_rir_database().to_pickle(
        path=os.path.join(IPTOCC_DIR, "rir_database.db"),
        compression="zstd",
    )
    print("Done!")


if __name__ == "__main__":
    update_rir_databases()
