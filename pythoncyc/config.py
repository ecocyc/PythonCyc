# Copyright (c) 2014-2020, SRI International
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ----------------------------------------------------------------------

"""
This module can be used to set various parameters for PythonCyc,
in particular to set debug on or off, the host name and port number
of the running Pathway Tools' Python server. By default, the Pathway Tools
Python server is running locally on port 5008.
"""

_debug = False
_hostname = "localhost"
_hostport = 5008

def set_debug_on():
    """
     Turn on debug mode for PythonCyc.
     Turning on debugging should turn on output tracings of the communications between PythonCyc and Pathway Tools.
    """
    global _debug
    _debug = True
    print('Debug on.')
    
def set_debug_off():
    """
     Turn off debug mode for PythonCyc.
     Turning off debugging should turn off all output tracings of the communications between PythonCyc and Pathway Tools.

    """
    global _debug
    _debug = False
    print('Debug off.')

def set_host_name(hostname):
    global _hostname
    _hostname = hostname
    print('PythonCyc will communicate with Pathway Tools running on host name ',_hostname)

def set_host_port(hostport):
    global _hostport
    _hostport = hostport
    print('PythonCyc will communicate with Pathway Tools running on host port ',_hostport)
