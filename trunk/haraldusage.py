#!/usr/bin/env python
# -*- coding: utf-8 -*-
# haraldusage.py
# July 2009
# Terence Stenvold <tstenvold@gmail.com>
#
#Help info for the running of harald scan

#This file is part of Haraldscan.
#
#Haraldscan is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License Version 3 as
#published by the Free Software Foundation.
#
#Haraldscan is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License Version 3 for more details.
#
#You should have received a copy of the GNU General Public License
#Version 3 along with Haraldscan.  If not, see <http://www.gnu.org/licenses/>.

import sys

def usage():

    print "usage: haraldscan.py [options]"
    print "Options:"
    print "\t-b --build\t: Builds MAC Addr database. Ignores all other options"
    print "\t-h --help\t: Shows this help menu"
    print "\t-u \t: Updates the MACLIST if there are updates and rebuilds the database (requires and Internet connection). "
    print "\t-s --service\t: Does a service scan of all devices found and saves"
    print "\t\t\t  a file like a 'Unknown' vendor device would."
    print "\t-w --write file\t: Outputs discovered device info to (file) specified."
    print "\t\t\t  Overwrites any existing file\n"
    sys.exit(1)

def os_error():

    print "Error:\n\tYour Operating System is not supported or undetectable\n"
    sys.exit(1)

def bluetooth_error():

    print "Error:\n\tNo Bluetooth Adapter Found. Please run 'hciconfig hci0 up' If Adapter is present but not working\n"
    sys.exit(1)

def no_db():

    print "Error:\n\tDatabase not found or Corrupt. Please run 'haraldscan.py -b'\n"
    sys.exit(1)
