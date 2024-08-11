#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2017-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import pytest

from iptocc import CountryNotFound, get_country

PARAMS = [
    ("United States - IPv4", "5.35.192.0", "United States"),
    ("Sweden - IPv4", "5.35.184.0", "Sweden"),
    (
        "United States - IPv6",
        "2607:f8b0:4004:c1f::71",
        "United States",
    ),
]


@pytest.mark.parametrize(
    "name, ip, expected", ids=[x[0] for x in PARAMS], argvalues=PARAMS
)
def test_get_country(name: str, ip: str, expected: str):
    assert get_country(ip) == expected, name


def test_ipv4_private():
    with pytest.raises(CountryNotFound):
        get_country("10.0.0.0")


def test_invalid_ip():
    with pytest.raises(ValueError):
        get_country("123456")
