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
This module is part of PythonCyc, a Python interface module to Pathway Tools.
This code has been tested with Python 3.7.

Pathway Tools (version 18.5 and up) must be running on some machine
with at least the option '-python'. It is also recommended
to start Pathway Tools with the option -lisp, so that the
connection can be monitored:

./pathway-tools -lisp -python

The global functions defined in this init file can be called before any
PGDB (an organism database in Pathway Tools) has been selected.
In fact, two of these functions, select_organism and
its synonym so, are needed to "select" a PGDB by creating a PGDB object.
See class PGDB in PGDB.py for information about how to use a PGDB object.

Please consult the tutorial.html file, under directory doc, for more information
about how to use PythonCyc.
"""

from . PGDB import PGDB
from . PTools import sendQueryToPTools

def select_organism(orgid):
    """
    Select an organism PGDB based on its unique organism id.
       orgid: string, the unique organism id in Pathway Tools (e.g., ecoli, meta).
    """
    return PGDB(orgid)

def so(orgid):
    """ A synonym of method select_organism. """
    return select_organism(orgid)

def all_orgids():
    """ 
    Returns all organism unique ids (orgids) available 
    from the current running Pathway Tools. 
    """
    orgids = sendQueryToPTools('(all-orgids)')
    return orgids

def biovelo(query):
    """
    Execute a BioVelo query and return the result.
    
    Parameters
      query: a string, which is a BioVelo query.
    Returns 
       Whatever the BioVelo query computes.
    
    Example
       bv('[(p, reactions-of-pathway(p)): p<-ecoli^^pathways]')
    """
    return sendQueryToPTools('(biovelo "'+query+'")')

def bv(query):
    """
    A synonym of method biovelo.
    """
    return biovelo(query)

def run_fba(fileName):
    """
    The function run_fba does not need to have an organism selected before
    being used because the FBA input file provided as input can specify
    the organism.

    For the documentation of this function, see method run_fba
    in file PGDB.py.
    """
    return sendQueryToPTools('(python-run-fba "'+fileName+'")')

