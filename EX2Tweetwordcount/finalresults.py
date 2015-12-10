#!/usr/bin/env python
from __future__ import absolute_import, print_function, unicode_literals
import sys
import psycopg2


if sys.argv[1] is None:
	#Case
	print ("you forgot to enter an argument")
else:
	print("The first arg is " + str(sys.argv[1]))
