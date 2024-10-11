
>----------------------------------------------------------------------
>Copyright (c) 2014-2024, SRI International
>
>Permission is hereby granted, free of charge, to any person obtaining
>a copy of this software and associated documentation files (the
>"Software"), to deal in the Software without restriction, including
>without limitation the rights to use, copy, modify, merge, publish,
>distribute, sublicense, and/or sell copies of the Software, and to
>permit persons to whom the Software is furnished to do so, subject to
>the following conditions:
>
>The above copyright notice and this permission notice shall be
>included in all copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
>EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
>MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
>NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
>LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
>OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
>WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
>----------------------------------------------------------------------



# PythonCyc Tutorial

 PythonCyc is a Python interface package to [Pathway Tools](http://brg.ai.sri.com/ptools/), version 18.5
 or above. PythonCyc has been tested with Python 3.5 and 3.7 on Linux and MacOXS.
 Since PythonCyc is based on the programming
 language Python, you must use a Python interpreter to use
 PythonCyc. In the following we assume that you have installed Python
 (we recommend version 3.7 or above, but it will most likely work with any 3.x version).

 For the complete API documentation of PythonCyc, please consult [PythonCyc API](http://pythoncyc.readthedocs.org).

 For the latest news about PythonCyc, please consult the [PythonCyc web page](http://brg.ai.sri.com/ptools/pythoncyc.html).

## Installation

We assume that you have downloaded PythonCyc from
[PythonCyc at GitHub](https://github.com/ecocyc/PythonCyc).
This may be done by using git cloning or by downloading the zip
file of PythonCyc from GitHub.  If downloading the zip file, you
will need to unpack it using the `unzip` command in some
directory of your choice.

The next step is to make PythonCyc accessible from your running Python
interpreter. To do so, install PythonCyc according to one of the
following platforms.

### Mac OS X and Linux

Open a terminal window and change your directory to the location where
you unpacked the PythonCyc package. You must have the file setup.py, and the subdirectory pythoncyc, 
in that directory.  We recommend you create and activate a python virtual environment for
your pythoncyc installation (see the [python venv webpage](https://docs.python.org/3/library/venv.html).
Otherwise, you will need to run the following command with 'sudo' because pythoncyc installation will write
files to your python system area.
Assuming that 'shell>'
is the prompt of your current Unix shell, execute the following
command:


	shell> pip install .


alternatively, you can install using setup tools, by executing:



	shell> python setup.py install


but installing with pip is recommended.

The installation command copies several files from the pythoncyc subdirectory
either the virtual environment or the system python libraries, byte-compiles these files
and may do other operations depending on the Python installation you
have. No error messages should be reported. In case of errors, make
sure you have installed Python and that it is working.

To test your
PythonCyc installation, please consult the Section [Getting Started](#gettingStarted) in this document.

### Microsoft Windows

On a Microsoft Windows platform, starts a command prompt window using
the start/Accessories menu, then change the directory to the location
where you unpacked or cloned the PythonCyc package. You must have the file
`setup.py`, and the subdirectory `pythoncyc`, in that directory.
Then, at the command prompt, execute the following command:


      python setup.py install


This command copies several files from the pythoncyc subdirectory
to other locations on your computer where Python is installed,
byte-compiles these files and may do other operations depending on the
Python installation you have. No error messages should be reported. In case
of errors, make sure you have installed Python and that it is working. To
test your PythonCyc installation, please consult the
Section [Getting Started](#gettingStarted) in this
document.

## Getting Started


 Pathway Tools (version 18.5 and up) must be running on some
computer.  You can start pathway tools from either the command line or
a short cut.  If you use the command line, you need to start pathway tools
with at least the command line option '-python' or
'-python-local-only', which starts the Python server in Pathway
Tools. If '-python' is specified, connections made to Pathway Tools
could come from a remote computer, whereas for '-python-local-only',
no remote computer can connect to the Python server. The option
'-python-local-only' is for added cybersecurity because with that
option no remote computer can access your locally running Pathway Tools
via the Python server. PythonCyc communicates to this running Pathway
Tools server via a socket on port 5008 (default setup).  It is also
recommended to start Pathway Tools with the command line option
'-lisp', so that the connection can be monitored and debugged, if need
be. In summary, we recommend to start Pathway Tools using the following options


    ./pathway-tools -lisp -python


or to run locally for added security with the options


    ./pathway-tools -lisp -python-local-only


To run PythonCyc remotely from Pathway Tools, please
read the Section [Remotely Accessing Pathway Tools](#remotely-accessing-pathway-tools)
to setup PythonCyc to remotely access Pathway Tools.  In the
following, we assume that Pathway Tools is running on the same computer
as Python and that it has the EcoCyc database.

Start a Python interpreter on the same computer as Pathway Tools.
You should get a prompt such as &gt;&gt;&gt;, then enter the following


    >>> import pythoncyc


This command imports the PythonCyc module to access its classes,
functions and methods. If any error messages is given when this command
make sure PythonCyc has been installed according to the Installation instructions.
Then enter the command


     >>> eco = pythoncyc.select_organism('eco')


This command sends a request to Pathway Tools to create a
**PGDB** object associated with the database EcoCyc, which is
specified using the 'eco' organism identifier (i.e., orgid). That PGDB
object is assigned to the variable `eco`. (If you get
an error message, it could be that Pathway Tools was not started 
as given above.)

Print out the Python `eco` variable


      >>> print(eco)
      &lt;PGDB eco, currently has 0 PFrames&gt;


<p>
This means that `eco` is bound to a PGDB object, its orgid is eco and
it has currently no PFrames attached to it. Indeed, currently we only created
a PGDB object that has no _data frames_ in it. The following sections will show
how to retrieve data frames from Pathway Tools to PythonCyc via this variable `eco`.

If you want to have a list of all PGDBs, and their orgids, accessible from your
running Pathway Tools, evaluate `pythoncyc.all_orgids()`.

<p>Please, consult the source file `__init__.py` for other 
fundamental methods available from the pythoncyc module.

<p>Also, more
advanced technical documentation is provided for each method and
functions by consulting the PythonCyc modules config.py, PGDB.py,
PToolsFrame.py and PTools.py. As usual, the Python `help`
command can provide documentation about the modules, classes and
methods: for example, `help(pythoncyc)` prints the
documentation for the module `pythoncyc`; or the
command `help(eco)`, once the variable `eco` is bound to a
PGDB object, prints all the methods available, and their documentation,
for a PGDB object.

## Retrieving Frames From Pathway Tools using Frame Ids

 Using that variable `eco`, it is now possible to request data from the
EcoCyc database.  For example, the following statement retrieves compound
TRP (i.e., L-tryptophan). 'TRP' is the **frame id** of compound L-tryptophan, which we
can also specify in lower case letters: 


    >>> eco.trp


Evaluating `eco.trp`, if done for the first time, triggers
a call to Pathway Tools to retrieve the _frame data_ (or simply
frame) of compound TRP: the slots (also called attributes) and their
data of the Pathway Tools frame representing compound TRP are
sent to PythonCyc to create a **PFrame** object to represent
the compound TRP. PythonCyc also prints that frame content which is
represented as a Python dictionary: the slots of the frame are
the keys of the dictionary and the value of the slots are the
values of the dictionary.

 Note: in Pathway Tools, the _slots_ are used to access the
data of a frame (i.e., object).  In Python, an object has
_attributes_. The meaning of these two terms, that is, slots and
attributes, are very similar. A slot of a frame in Pathway Tools
becomes an attribute of a PFrame object in PythonCyc. We will use the term
slots when referring to a frame in Pathway Tools and attributes when referring
to the same slots in PythonCyc.  

Printing out eco now shows that we have one PFrame attached to 
eco:


	>>> print(eco)
	&lt;PGDB eco, currently has 1 PFrames&gt;

Indeed, this PFrame for TRP was also bound to the PGDB meta such that it
became an attribute of meta. That is, executing `eco.trp` again would
not retrieve the data from Pathway Tools, but directly use the PFrame
already created for it and now stored as an attribute for eco. All
created PFrames based on a PGDB object are attached to that object and
no two PFrames can have the same frame id for that PGDB object. 


In Pathway Tools, the frame id is in upper case, that is,
'TRP'. The conversion from lower case to upper case is handled
automatically by PythonCyc.  PFrame, in PythonCyc, is the class of
objects to represent frame objects from Pathway Tools. More details
about PFrames is given below and in the Section [PFrame Objects](#pframes). In particular, note that PFrames
are read only, that is, their attributes cannot be modified.  

From a PGDB object, a PFrame can be accessed using the frame id
either by using the attribute or indexing syntax of Python. For example, the
following would retrieve reaction with frame id RXN-14361 


	  >>> rxn14361 = eco['RXN-14361']


or by using the attribute syntax


   >>> rxn14361 = eco.rxn_14361


Both forms access the same attribute. Note that the frame id
'RXN-14361' has a dash in its name but an attribute in Python cannot
have a dash. To provide access to such frame ids, using the attribute
syntax of Python, dashes are converted to underscores. Mixed cases
(i.e., upper or lower case letters) can be used for both syntax
(attributes and indexing) because an automatic conversion is done by
PythonCyc. There are cases where only the second form, the indexing
syntax, can be used. For example, for a slot name starting with a
digit, or a character that is not a letter or an underscore, the
indexing syntax with a string must be used. This is due to the syntax
of attribute names in Python which can only have letters, digits and
underscores, and cannot start with a digit. For example, the slot
name 'N+1-NAME' can only be accessed using the index syntax because
it has the character '+' which cannot be used in a Python identifier.

In PythonCyc, frame ids are stored as strings prefixed and suffixed
by '|'. In general, these vertical bars identify symbols in
PythonCyc which exists as Lisp symbols in Pathway Tools. When
symbols are return from Pathway Tools, the vertical bars are inserted.
For example, we can see the frame id of eco.trp by printing it: 


    >>> print(eco.trp.frameid)
    |TRP|


The syntax '|...|' is used to indicate that this string represents a symbol and can be
interpreted by Pathway Tools as a frame id. In Lisp, the programming language used
to implement Pathway Tools, the double vertical bars signifies that this is a symbol that
must be read exactly as given without any transformation (e.g., no case
conversion on letters).

Advanced technical note: all PFrames created using a PGDB object are
included in a Python dictionary bound to an attribute, of that PGDB
object, called "frames". The keys of that dictionary are the frame ids
of the PFrames converted to valid Python identifiers. The __getattr__
and __getitem__ methods of the PGDB class were written in such a way
that such an expression as 'eco.trp' searches in the dictionary for a
PFrame with frame id 'TRP'.  

Once you have access to a frame, the frame ids stored in that
frame can be used to create more PFrames. For example, the
`trp` object has an attribute called `appears_in_right_side_of`
which has a list of reaction frame ids as a value. The reaction
frame ids refer to all reactions that has TRP on its right-hand side.
The reactions can be retrieved in the following way:



	>>> rxns_trp_right = [eco[fid] for fid in eco.trp.appears_in_right_side_of]


The variable `rxns_trp_right` is bound to a list of PFrames 
representing the reactions. Each PFrame becomes also attributes to
`eco` based on the frame ids.


The basic mechanism of attribute access and indexing on a PGDB
object just shown is enough to retrieve all frames from a PGDB
assuming that frame ids are known and PFrames are implicitly
(i.e., automatically) created. The next section shows
how to retrieve large number of frames based on classes of objects,
which indirectly provides the frame ids of large number of frames.

## Retrieving Classes of Frames from Pathway Tools

Another implicit operation done by PythonCyc is the retrieval of
classes of objects from Pathway Tools. There are many classes of
objects, such as Reactions, Proteins, Compounds, Genes, Pathways, and
more. For example, retrieving the class of all reactions of PGDB eco,
from Pathway Tools, can be done by 


     >>> reactions = eco.reactions


 which assign to variable `reactions` a PFrame representing the class
of reactions from PGDB eco. Printing out this variable gives 


   >>> reactions
   &lt;PFrame class |Reactions| currently with 3237 instances (eco)&gt;



As can be seen, `reactions` is a PFrame and it is a class which
has the name |Reactions| in Pathway Tools and it has 3,237 instances,
that is, 3,237 reactions, all from the PGDB eco (i.e., EcoCyc).
The number of instances may differ for you because EcoCyc is
periodically modified. Remember that the vertical bars in a name means
that it is a symbol, and here it is more specifically a frame id.

This PFrame `reactions` has an attribute `instances`
assigned with the list of all reactions of the EcoCyc PGDB. Each such
reaction is also a PFrame, although these PFrames have currently **no
other data than the frame id of each reaction**. It is a _lazy
transfer_ of the frames where only the frame ids were requested
from Pathway Tools. This approach is useful because in some cases not
all data from all reactions are needed. We can access each reaction
via the attribute `instances`, for example


    >>> reactions.instances[0]


but we can also use indexing directly on the class reactions such as


    >>> reactions[0]
    {'_gotframe': False, '_isclass': False, 'pgdb': <PGDB eco, currently has 3240 PFrames>, 'frameid': '|3.1.22.4-RXN|'}


but the frameid value is likely different (EcoCyc is periodically
modified). As mentioned, each object in a PGDB has a unique identifier
called the frame id, which in PythonCyc is stored in the field frameid
of a PFrame. When the reactions were retrieved from Pathway Tools,
the frame id values also became attributes of the Python PGDB object eco,
that is, we can also indexed object `eco` with the frame
ids. For example,


     >>> eco['|3.1.22.4-RXN|']
     {'_gotframe': False, '_isclass': False, 'pgdb': <PGDB eco, currently has 3240 PFrames>, 'frameid': '|3.1.22.4-RXN|'}


This Python dictionary is a very short representation of the frame
with almost no data. The attributes shown are only created by
PythonCyc to maintain that frame in Python. If you access one
slot of that reaction frame, which is not listed in that
output, the value of that slot is retrieved from Pathway Tools. For
example,


	>>> reactions[0].left
	[ '|WATER|', '|CPD0-889|']


retrieves the data for slot `left` **and that value is kept in the PFrame**. 
Therefore, accessing several times the same slot of a frame, only triggers one communication
to Pathway Tools because after it was accessed once, it is no longer accessed again
from Pathway tools. (Note: the methods `get_slot_values` and `get_slot_value`
presented later in this document always trigger a transfer from Pathway Tools.)
We can verify that the the PFrame has the left attribute in the PFrame itself:

   >>> reactions[0]
   {'left': ['|CPD0-889|', '|WATER|'], '_gotframe': False, 
   '_isclass': False, 'pgdb': <PGDB eco, currently has 3240 PFrames, 'frameid': '|RXN0-5040|'}

### Explicit Transfer of Frames

Another very different approach to retrieve all the data
of a list of frames is by using the Python method
`get_frame_objects` defined for a PGDB object.
That method takes a list of frame ids as input and send a request to
Pathway Tools to transfer all the slots and their data for all the
frames identified by these frame ids. The function creates a PFrame,
for each frames retrieved, for the PGDB, if none exist. 

For example, assuming that we have the variable `reactions`
bound to the class of reactions as in the previous section,
to retrieve all the frame data for the first 10 reactions,
the following can be used: (We retrieve only the first 10 reactions 
to reduce execution time)


   >>> r = eco.get_frame_objects([f.frameid for f in reactions.instances[0:10]])


The list comprehension gathers the frame ids in one list and a call to
the `get_frame_objects` method is done, using the PGDB object eco, to
retrieve from Pathay Tools all the slots and their data for all the
frame ids. This approach always transfer the frames from Pathway Tools
even if we already transferred them already. This can be needed if the
frames were modified and there is a need to transfer them again.

## Explicit Access to Slot Data Without PFrames

Another very different way to access the frame data is to use
methods `get_slot_value` and `get_slot_values`.  These
methods are among the more than 150 methods of the PGDB class which is the
subject of the next section.  The
first method retrieves a scalar value on a slot that can only have one
value whereas the second method retrieves a list of values from a slot
that can have multiple values. In both cases, only the data from one
slot is retrieved, not the whole frame. That is, there are **no
creation of PFrames** when using these functions.  

For example, the following retrieves the Gibbs free
energy of reaction RXN-14361 from EcoCyc


       >>> eco.get_slot_value('RXN-14361', 'GIBBS-0')
       3.1530151


We did not specify the vertical bars for the frame id 'RXN-14361'
and the name of the slot 'GIBBS-0' although both are symbols in
Pathway Tools.  The translation to symbols is handled automatically by
the function `get_slot_value`, and many other functions that
require symbols as arguments.

The following retrieves the chemical formula of compound TRP


    >>> eco.get_slot_values('TRP', 'CHEMICAL-FORMULA')
    {'|N|': [2], '|C|': [11], '|H|': [12], '|O|': [2]}


The method `get_slot_values` is needed (instead of
`get_slot_value`, the singular version) because the slot
'CHEMICAL-FORMULA' keeps the chemical formula as a list of pairs
(atom-species coefficient) where atom-species is the species of the
atom (e.g., 'C' for carbon) and coefficient is an integer. In that
particular case, that is, a list of pairs, the result will be returned
as a Python dictionary where the keys are the atom species and the
values are the coefficients.  In the next section there is more
explanation on data conversion between Lisp and Python.  

## Calling Pathway Tools Functions Using a PGDB Object

Using a variable bound to a PGDB object, which is the case for
variable `eco` from the previous sections, any of the more than 150
methods from the PGDB class can be called, each corresponding to a
specific function in Pathway Tools. The list of these methods (or
functions), and their documentation, can be obtained by consulting the
source code of file `PGDB.py` or by using the standard help mechanism
of Python (or IPython). For example,


   >>> help(pythoncyc.PGDB)


will list the source documentation of the class PGDB with the list of
all methods. For a particular function, you can request its documentation
by naming the function. For example,


   >>> help(pythoncyc.PGDB.get_slot_value)


Almost all these methods do not create PFrame objects but return a
basic Python object, that is, boolean, numbers, strings, lists,
dictionaries, and so on. When a Pathway Tools object (e.g., gene,
pathway, reaction) needs to be returned, the frame id (as a string) is
returned. For example, the following call retrieves all the pathways
from eco by returning a list of frame ids (as strings): 


     >>> pwys = eco.all_pathways()


As presented in the previous section, to create PFrames, and the
data about pathways, using frame ids, you can use the method
`get_frame_objects`. 

Many other Lisp functions, defined in Pathway Tools, can be called using
Python's syntax. These functions often need a frame as one of the parameters.
A frame can be specified as a frame id (a string) or as a PFrame object. For example,


	>>> eco.reactions_of_compound('TRP')


where 'TRP' is the frame id of compound L-tryptophan. The
`reactions_of_compound` method (which is a function in Pathway Tools)
retrieves all reaction frame ids that
use TRP as a substrate. Note that, if the given frame id was not
existing in the PGDB, it would raise a PToolsError in PythonCyc because
Pathway Tools itself will report a 'non coercible frame'. 

A PFrame can also be used instead of the frame id. For example, 
`eco.trp` refers to a PFrame for compound TRP and
can be used to do the same operation we just did, that is,

    >>> eco.reactions_of_compound(eco.trp)

Some methods modify the PGDB in Pathway Tools, such as


     >>> eco.put_slot_value('RXN-14361','GIBBS-0',2.7)


which modifies the slot 'GIBBS-0' for frame 'RXN-14361' to the value
2.7 for the PGDB associated with object eco, which in our case is EcoCyc.

Some functions have keywords arguments, which are always optional. But notice
that the default value is often the Python value `None`.
The value `None` is not translated to `False`, but
indicates to use the default value of the Lisp function called. These defaults
are given in the documentation of each PythonCyc method.

The transfer of all data from Pathway Tools to PythonCyc is done
using the JSON (JavaScript Object Notation) syntax. On the other hand,
PythonCyc **does not use** JSON for the transfer of data from
Python to Pathway Tools because Pathway Tools uses Lisp and it is
simpler to use a Lisp syntax for that transfer.  Some conversion rules
are applied on data types when transferring data to and from Pathway
Tools and we discuss these in the following. Note that all the special
rules of conversion from Lisp to Python is based on what the JSON Lisp
package does whereas the special rules of conversion from Python to
Lisp is what the method `convertArgToLisp`, of class PGDB,
does.

During conversion, the numbers are kept relatively unchanged:
integers and floating-point numbers are translated using the same
types but floating-point numbers are not guaranteed to have the same
precision. In Lisp and Python, infinite precision of integers are
implemented. The rational numbers of Lisp are translated to
floating-point numbers in Python.  

The Python value `True` is translated into `t` in Lisp whereas
`False` and `None` are translated into `nil` in Lisp.
The value `t` in Lisp is translated into `True` in Python.
On the other hand, the value `nil` in Lisp is translated into
`False`, `None` or the empty list `[]` in Python depending
on the context. It is translated to `False` when a PythonCyc method
is called that expects a boolean value as a result: for example, the
PythonCyc method `pathway_hole_p` does return `False` when
the result of the corresponding function in Lisp is `nil`. It is translated
to the empty list `[]` when a PythonCyc
method is called that expects a list as a result: for example, the 
PythonCyc method `get_slot_values` does return `[]`
when the slot value is `nil`. Finally, the `nil`
values is translated to `None` when the result is not
known to be a boolean or a list value: for example, the
PythonCyc method `get_slot_value` would return `None`
if the slot value is `nil`.

Any Lisp string is translated into a Python string. A Python string
that starts and ends with a '|', and contains no space, is assumed to
represent a symbol and is translated successfully into one if indeed
the Python string follows the correct syntax of a Lisp symbol. For example,
the Python string `"|RXN-14361|"` is translated into the Lisp
symbol `RXN-14361`.

Lisp lists are translated to Python lists, but with one important
exception: a Lisp list where all elements are non empty sublists, and
every first element of each sublist is a symbol or string, are
translated into a Python dictionary. For example, the
slot `chemical-formula` has such lists: the chemical formula H2O is
represented as the list of sublists `((H 2) (O 1))`, where H and O
are symbols, in that slot. Each sublist is translated, in JSON, to a
key/value pair in a dictionary, where the key is the first element of
the sublist and the value is the rest of the list. Therefore, the Lisp
value `((H 2) (O 1))` is translated into the Python dictionary
`{'|H|' : [2], '|O|' : [1]}`. Notice that H and O are translated into Python strings
with the vertical bars to indicate that they are symbols
and the coefficients 2 and 1 are translated into lists of one element
because the rest of each sublist is a list.  

A dictionary in Python is translated into a list of dotted pairs or
list of lists when transferred to Pathway Tools. For example,
`{'|H|' : [2], '|O|' : [1]}` is translated into `((H 2) (O
1))`, which is the desired Lisp representation in Pathway Tools
for the a chemical-formula slot value. On the other hand the Python
dictionary `{'|H|' : 2, '|O|' : 1}` would be translated into
`((H . 2) (O . 1))`, that is, a list of dotted pairs, which is
not the desired Lisp representation for that slot but could be used
correctly in some other context although Pathway Tools rarely uses
dotted pairs.  

A vector from Pathway Tools is translated into a Python list.
Note: there is no basic vector type in Python.

Finally, a Python tuple is translated into an improper Lisp list.
For example, the Python tuple `(1, 2, 3)` is translated
into the improper Lisp list `(1 2 . 3)`. The last element
of the list is preceded by a dot, which makes it an improper list.
Note that the particular case of a tuple with only one element is translated
into an improper list of `nil` followed by the element. For example,
the Python tuple `(2,)` is translated into `(nil . 2)`. 
Improper lists are uncommon in Pathway Tools such that you may never need
to worry about them. 
<p>

<p>If you modify the slots of data frames in Pathway Tools, via the
PythonCyc interface, care must be taken to store the appropriate data
structures and use the appropriate corresponding Python data
structures.  As we just saw, this should not be a problem for numbers,
strings, booleans and list of these basic types as the translation is
one to one. For example, the value of the slot `synonyms` of compound
frames is a list of strings, the synonyms of the compounds:


       >>> eco.get_slot_values('atp', 'synonyms')
       ['adenylpyrophosphate', 'adenosine-triphosphate', "adenosine-5'-triphosphate"]

You could modify that list, say to only include the first two synonyms, in the following
way:


	>>> eco.put_slot_values('atp', 'synonyms', ['adenylpyrophosphate', 'adenosine-triphosphate'])

 Note: Typically, modifying a slot should be done on your own
created PGDB, not on EcoCyc.  In any case, you will not be able to
save EcoCyc and any slots modified in EcoCyc will be restored to its
original value after you restart the Pathway Tools application.  

As for a slot such as `chemical-formula`, you can represent the
value to store in the slot as a list of sublists, such as:


      >>> eco.put_slot_values('water', 'chemical-formula', [['|H|',2],['|O|',1]])
      {'|H|': [2], '|O|': [1]}

The returned value is a dictionary that contains frames ids (i.e., the vertical bars
surrounding H and O indicate that they are symbols). Or you can use a dictionary
as in


   >>> eco.put_slot_values('water', 'chemical-formula', {'|H|': [2], '|O|': [1]})


In all cases, care must be taken to have the right representation when
modifying a frame slot of a PGDB in Pathway Tools because, at the moment of
modifiying the slot, there is no verification of the validity of
the data being stored.

 When a slot is supposed to contain frames, storing the frame ids
in the slot automatically convert these frame ids into frame
references.  For example, the slot `structure-atoms` is a list
of atom species frames. To modify it would simply require to list the
atom species frame ids. For example, for compound water: 


     >>> eco.put_slot_values('water', 'structure-atoms', ['|O|', '|H|', '|H|'])


Notice that we passed the frame ids O and H using the vertical bars.
This is needed because otherwise these would be taken as strings not symbols that
refer to frame object in Pathway Tools.

As already mentioned, there are many more methods that can be
called to access functions in Pathway Tools and some of them can run
complex analysis. For example, there is a method to run flux balance
analysis (FBA) called `run_fba`. Please, consult the file `PGDB.py` for the
complete list of available methods and their documentation.  

## More on PFrame Objects


PFrame is a Python class to represent Pathway Tools' frames in
PythonCyc. A PFrame can represent a Pathway Tools class frame (e.g.,
Reactions) as well as an instance frame (e.g., RXN-9000). PFrames are
useful to retrieve many frames and all their data from Pathway to
PythonCyc and then operate on that data locally in Python. On the
other hand, if the data needs to be modified in the PGDB of Pathway
Tools, PFrames are not useful because they are read only.

As discussed in the previous sections, PFrames are automatically
created when retrieving classes, or instances using the attribute or
indexing syntax applied to a PGDB object. You could also directly create PFrames.
To do so, you need to import the class PFrame:


   >>> from pythoncyc.PToolsFrame import PFrame


The required parameters to create a PFrame are the frame id (a string) and a PGDB
object. For example, assuming that variable `meta` is bound to a PGDB object, the following
create a PFrame to represent the reaction RXN-14361,


       >>> PFrame('RXN-14361', eco)
       {'_gotframe': False, '_isclass': False, 'pgdb': <PGDB eco, currently has 1 PFrames>, 
       'frameid': '|RXN-14361|'}


By default, an instance PFrame (not a class PFrame) is created and
the data of the frame is not requested from the server, that is,
a PFrame object is created containing only the frame id, the PGDB and a fews other
attributes to maintain the PFrame. This is what the print out of that frame shows
above. That PFrame is also attached, as an attribute, to the PGDB eco. That
can be seen by evaluating 


    >>> eco._frames.keys()
    ['rxn_14361']


By specifying the keyword argument `getFrameData=True`, all slots and data of the frame are retrieved 
from Pathway Tools. For example, the following
create a PFrame for reaction RXN-14361 and retrieve all its slots and data,


       >>> PFrame('RXN-14361', meta, getFrameData=True)
       {'frameid': '|RXN-14361|', '_isclass': False, '_gotframe': True, 'pgdb': <PGDB eco, currently has 1 PFrames>,
       'ec_number': ['|EC-2.4.1.17|'], 'schema_p': True, 'reaction_direction': '|PHYSIOL-LEFT-TO-RIGHT|',
       'credits': ['|O0-13|', '|amackie|'], 'reaction_balance_status': '|BALANCED|', 'gibbs_0': 3.1530151,
       'synonym_slots': ['|ABBREV-NAME|', '|SYNONYMS|'], 'creator': '|amackie|',
       'substrates': ['|CPD0-934|', '|UDP-GLUCURONATE|', '|CPD-15237|', '|UDP|', '|PROTON|'], 'key_slots': '|COMMON-NAME|',
       'enzymatic_reaction': ['|ENZRXN0-7685|'], 'creation_date': 3572053675, 'left': ['|UDP-GLUCURONATE|', '|CPD0-934|'],
       'instance_name_template': 'RXN-*', 'physiologically_relevant_p': [True], 'right': ['|CPD-15237|', '|UDP|', '|PROTON|']}

For creating a class, the `isClass` keyword parameter must say so,

    >>> PFrame('Reactions', eco, isClass=True)


When creating a class, if `getFrameData=True` is specified, the class slots and its
data are fetched and all the instances of the class are also created
as, mostly empty, PFrames. They are mostly empty in the sense that the
slots and data of the instances are not transferred, but only the
frame id of each frame initialized each PFrame.

The attribute values of the PFrames cannot be modified, that is, attributes are read only.
If you try to modify a PFrame attribute, a PythonCycError is raised.
On the other hand, slots of Pathway Tools' objects can be modified using methods
`put_slot_value` and `put_slot_values`. In that case, the PGDB
itself in Pathway Tools is modified. See class PGDB for these methods.

## Remotely Accessing Pathway Tools


It is possible to use PythonCyc to access a Pathway Tools
application running on a remote computer. First, Pathway Tools must be
started with the command line option '-python' (not
'-python-local-only'). That is,


	./pathway-tools -python


or with also the option -lisp to get a Lisp console to monitor the Python server


	./pathway-tools -lisp -python


<p>
Note: If you were using the option '-python-local-only' instead of '-python' 
the Python server runs with increased security by not accepting connections
from remote computers.

Second, you need to
use the config module of PythonCyc to set the appropriate host name
of that remote computer. For example, assuming that the remote computer
is at address 'ptools.mydomain.com' (this is a fictive address for
this example). The following would configure
PythonCyc to communicate with it:


	>>> import pythoncyc.config as config
	>>> config.set_host_name('ptools.mydomain.com')


If for some reason the Pathway Tools Python server is not using the default port
(i.e., 5008),  but some other port such as 5000,
it can also be configured on the PythonCyc side by using method `set_host_port`


	>>> config.set_host_port(5000)


The preceding Python configuration can be done at any time and it affects 
all future operations of PythonCyc. It could be done several times to 
access different Pathway Tools running on different ports or host names.

## Complete Examples

### Function to Gather the Gibbs Free Energies of Substrates of Reactions

 This example is a function that gathers the Gibbs free energy of
the compounds involved in each reaction of a PGDB with a given
orgid. The result is a Python dictionary with keys as the frame ids of
the reactions and the values as lists of the substrates' Gibbs free
energy of each reaction.  

This function does not create any PFrame but uses the basic `get_slot_value`
and `get_slot_values` to retrieve data from Pathway Tools. The function
`all_rxns` retrieves the frame ids of all reactions from the PGDB,
then the substrates slot is accessed to get the compound
frame ids involved in each reaction. Finally, for each compound frame id, the slot
'GIBBS-0' is accessed to create pairs of compound frame id and Gibbs free energies values
transformed into a dictionary using the Python `dict` function.


	def gather_gibbs_substrates_of_reactions(orgid):
	     """
	     Return a dictionary of all reactions of PGDB orgid with the Gibbs free energies of formation 
	     of their substrates. The keys are the frame ids of the reactions and the values are dictionaries
	     of compound frame ids to Gibbs free energies of formation.
	     """
	     pgdb = pythoncyc.select_organism(orgid)
	     rxn_frameids = pgdb.all_rxns(type='all')
	     gibbs_dict = {}
	     for rxn_fid in rxn_frameids:
	         cpds_fids = pgdb.get_slot_values(rxn_fid,'SUBSTRATES')
	         gibbs_dict[rxn_fid] = dict([(cpd_fid, pgdb.get_slot_value(cpd_fid, 'GIBBS-0')) for cpd_fid in cpds_fids])
	     return gibbs_dict


This function could be called in the following way assuming that
the PGDB with orgid 'eco' is available from the Python server of Pathway Tools.


	>>> gibbs_dict = gather_gibbs_substrates_of_reactions('eco')


This function may take more than 30 seconds to execute because it is retrieving
a large amount of data from Pathway Tools. 

### Function to Create a PGDB with all its Compounds and Reactions

The following is a simple function to create a PGDB object based on
the organism name (i.e., orgid) and retrieve all its basic PFrames for
compounds and reactions. Note that these PFrames has no other data 
than their frame ids.


     def create_pgdb_with_compounds_and_reactions(orgid):
	    """
	    Create a PythonCyc PGDB object with all its compounds and reactions
	    PFrames created. Return the PGDB object.
	    ""
	    pgdb = pythoncyc.select_organism(orgid)
	    pgdb.compounds
	    pgdb.reactions
	    return pgdb


 Assuming that the PGDB ecoli is available on your running Pathway
Tools server, the following call would bound variable `pgdb` to a PGDB
object containing the PFrames for the compounds and reactions of
ecoli: 


	pgdb = create_pgdb_with_compounds_and_reactions('eco')

## Support

For comments, questions and bug reports about PythonCyc,
send an email to ptools-support@ai.sri.com

## Acknowledgments

Eli Bogart inspired some implementation details of PythonCyc from
its PyCyc package, Tomer Altman wrote the original Pathway Tools Lisp
API documentation at http://brg.ai.sri.com/ptools/api/ and Daniel
Weaver suggested to implement some specific functions to access the
functionality of FBA in Pathway Tools.  

* * *

</body>
</html>
