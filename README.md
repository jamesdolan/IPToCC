# IPToCC-Live
DEPRECATED: Use [ip_to_country](https://github.com/jamesdolan/ip_to_country/blob/main/update.py) instead which is orders of magnitude faster!

Fork of [https://github.com/roniemartinez/IPToCC](https://github.com/roniemartinez/IPToCC) that updates the databases [regularly](https://github.com/jamesdolan/IPToCC-Live/actions/workflows/update.yml).

Get ISO country code of IPv4/IPv6 address. Address lookup is done locally.

[![CI](https://github.com/jamesdolan/IPToCC-Live/actions/workflows/ci.yml/badge.svg)](https://github.com/jamesdolan/IPToCC-Live/actions/workflows/ci.yml)
[![Update](https://github.com/jamesdolan/IPToCC-Live/actions/workflows/update.yml/badge.svg)](https://github.com/jamesdolan/IPToCC-Live/actions/workflows/update.yml)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jamesdolan/IPToCC-Live/blob/master/LICENSE)

## Features
- [x] No external API call
- [x] No paid GeoIP service
- [x] Thread-safe
- [x] Offline
- [x] Updated Nightly 

To learn about using IP addresses for geolocation, read the [Wikipedia article](https://en.wikipedia.org/wiki/Geolocation_software) to gain a basic understanding.

## Install
Install the latest version with the latest database...
```bash
pip install git+https://github.com/jamesdolan/IPToCC-Live.git@master
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
- Python 3.9+
- [pandas](https://github.com/pandas-dev/pandas)
- [zstandard](https://github.com/facebook/zstd)

## References
- [RIR Statistics Exchange Format](https://www.apnic.net/about-apnic/corporate-documents/documents/resource-guidelines/rir-statistics-exchange-format/)
- [How can I compile an IP address to country lookup database to make available for free?](https://webmasters.stackexchange.com/questions/34628/how-can-i-compile-an-ip-address-to-country-lookup-database-to-make-available-for)
- [ISO 3166 Country Codes](https://dev.maxmind.com/geoip/legacy/codes/iso3166/)

## Maintainers
- [Ronie Martinez](mailto:ronmarti18@gmail.com)
