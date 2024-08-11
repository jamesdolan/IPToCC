# IPToCC
Fork of [https://github.com/roniemartinez/IPToCC](https://github.com/roniemartinez/IPToCC) with the aim of being updated regularly.

Get ISO country code of IPv4/IPv6 address. Address lookup is done locally.

[![CI](https://github.com/jamesdolan/IPToCC/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/jamesdolan/IPToCC/actions/workflows/ci.yml)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jamesdolan/IPToCC/blob/master/LICENSE)

## Features

- [x] No external API call
- [x] No paid GeoIP service
- [x] Thread-safe
- [x] Offline

To learn about using IP addresses for geolocation, read the [Wikipedia article](https://en.wikipedia.org/wiki/Geolocation_software) to gain a basic understanding.

## Install

```bash
pip install IPToCC
```

## Usage

```python
from iptocc import get_country_code
country_code = get_country_code('<IPv4/IPv6 address>')
```

## Databases

- ftp://ftp.afrinic.net/stats/afrinic/delegated-afrinic-extended-latest
- ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest
- ftp://ftp.apnic.net/public/apnic/stats/apnic/delegated-apnic-extended-latest
- ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest
- ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest

## Dependencies

- [pandas](https://github.com/pandas-dev/pandas)
- [ipaddress](https://github.com/phihag/ipaddress)
- [backports.functools_lru_cache import lru_cache](https://github.com/jaraco/backports.functools_lru_cache)

## References

- [RIR Statistics Exchange Format](https://www.apnic.net/about-apnic/corporate-documents/documents/resource-guidelines/rir-statistics-exchange-format/)
- [How can I compile an IP address to country lookup database to make available for free?](https://webmasters.stackexchange.com/questions/34628/how-can-i-compile-an-ip-address-to-country-lookup-database-to-make-available-for)
- [ISO 3166 Country Codes](https://dev.maxmind.com/geoip/legacy/codes/iso3166/)

## Maintainers

- [Ronie Martinez](mailto:ronmarti18@gmail.com)
