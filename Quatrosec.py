#!/usr/bin/env python

# Note: This script runs Quatrosec from within a cloned git repo.
# The script `bin/quatrosec` is designed to be run after installing (from /usr/sbin), not from the cwd.

from quatrosec import __main__
__main__.entry_point()
