Copyright (c) 2014-2020, SRI International

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


PythonCyc 1.1, April 2020
============================

Overview
--------

The PythonCyc module provides a Python 3.5+ interface to a Pathway Tools
application running either locally or remotely. This module has been
designed to work on the three platforms supported by Pathway Tools:
Linux, Mac OS X, and Windows. Pathway Tools version 18.5 or
above is needed to use this module.

This release has been tested under Python 3.5 and 3.7 under Linux and
Mac OSX.  It has not been tested under Windows, or with IPython
or Jupyter.

The original PythonCyc 1.0 for Python 2.6-2.7
[is still available](https://github.com/latendre/PythonCyc)


Installation
------------

Please, consult the HTML file tutorial.html under the doc directory of this
package for the installation instruction of PythonCyc and how to start
Pathway Tools to be able to use PythonCyc.

Documentation
-------------

1) For a tutorial on how to use PythonCyc, please consult the HTML file
tutorial.html under the doc directory of this package, or [go directly
to the tutorial](https://github.com/ecocyc/PythonCyc/blob/master/doc/tutorial.md)

2) API documentation for PythonCyc is available [here](http://pythoncyc.readthedocs.org).
Note that there have not been any changes to the API documentation in this release.

3) The latest news about PythonCyc is available [here](http://bioinformatics.ai.sri.com/ptools/pythoncyc.html).

Author
------ 

PythonCyc 1.0 was developed by Mario Latendresse, latendre@AI.SRI.COM
The Python 3 update (aka PythonCyc 1.1) was developed by Peter Midford, midford@ai.sri.com

License
-------

See file LICENSE.

Support
-------

For comments and/or bug reports, send an email to ptools-support@ai.sri.com.

Acknowledgments
---------------

Thanks to Eli Bogart to have inspired some implementation details of
PythonCyc via PyCyc, Tomer Altman for the Pathway Tools API
documentation, and Daniel Weaver for suggesting to implement some
specific functions and his design, with Kai Chen, of the beautiful PythonCyc logo.
