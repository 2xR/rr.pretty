=========
rr.pretty
=========

This module exposes a few functions and a class decorator to make the task of writing ``__repr__()`` and ``__str__()`` for custom classes much easier. It will display a list of nicely formatted ``(attr, val)`` pairs with customizable separator and formatting for each pair.

Let's look at an example:

.. code-block:: python

    from rr import pretty


    class Foo:

        __str__ = pretty.str
        __repr__ = pretty.repr
        __info__ = pretty.info("x y z")

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    f = Foo(1, 2, 3)
    print(repr(f))  # see for yourself :)
    print(str(f))

Now, let's do the same, only this time we'll use the ``klass()`` class decorator:

.. code-block:: python

    from rr import pretty


    @pretty.klass
    class Foo:

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    f = foo(1, 2, 3)
    print(repr(f))
    print(str(f))

We even left out the attribute list, and ``pretty.info()`` (which is what ``pretty.klass()`` uses behind the scenes) builds it for us. That's it! You get nice ``__repr__()`` and ``__str__()`` methods for free.

Finally, a similar result can be also obtained using ``PrettyMixin`` as a base class instead of the class decorator.


Compatibility
=============

Developed and tested in Python 3.6+. The code may or may not work under earlier versions of Python 3 (perhaps back to 3.3).


Installation
============

From the github repo:

.. code-block:: bash

    pip install git+https://github.com/2xR/rr.pretty.git


License
=======

This library is released as open source under the MIT License.

Copyright (c) 2016-2017 Rui Rei
