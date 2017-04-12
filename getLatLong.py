#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from geopy.geocoders import Nominatim


def main():
    geolocator = Nominatim()
    location = geolocator.geocode("{}".format(sys.argv[1:]))
    print "{} {}".format(location.latitude, location.longitude)


if __name__ == '__main__':
    main()
