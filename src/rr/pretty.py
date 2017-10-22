"""Utility functions to help in the creation of nicer repr() and str() representations for
objects. The main idea is to greatly reduce the amoun of code necessary to obtain helpful string
representations. This code is also often repetitive, and this library aims to address that by
providing sensible defaults with just a couple of lines of code.
"""
import builtins
import functools

__version__ = "0.2.0"
__author__ = "Rui Rei"
__copyright__ = "Copyright 2016-2017 {author}".format(author=__author__)
__license__ = "MIT"

DEFAULT_FMT = "{!s}={!r}"
DEFAULT_SEP = ", "


def str(obj):
    """This function can be used as a default `__str__()` in user-defined classes.

    Classes using this should provide an `__info__()` method, otherwise the `default_info()`
    function defined in this module is used.
    """
    info_func = getattr(type(obj), "__info__", default_info)
    return "{}({})".format(type(obj).__name__, info_func(obj))


def repr(obj):
    """Default implementation of `__repr__()` for user-defined classes.

    Simply uses the object's `str()` representation and adds the object's memory address at the
    end (which is often times useful to check if two references point to the same object).
    """
    return "<{!s} @{:x}>".format(obj, id(obj))


def info(*attrs, fmt=DEFAULT_FMT, sep=DEFAULT_SEP):
    """This function is intended to be used as a `__info__()` method factory, as in

        class Foo:

            __str__ = pretty.str
            __repr__ = pretty.repr
            __info__ = pretty.info("x y z")
            # __info__ = pretty.info("x", "y", "z")  # equivalent to the line above
            # __info__ = pretty.info(["x", "y", "z"])  # also equivalent

    The returned function builds a string representation of a list of `(attr, value)` pairs.
    Separator and format strings may be specified to customize how the pairs are joined,
    and how each pair is formatted, respectively. If no `attrs` list is given, it is dynamically
    built based on the object's `__dict__`.

    See also the pretty.klass() class decorator.
    """
    if len(attrs) == 1:
        attrs = attrs[0]  # special case when a single positional argument is given
    if isinstance(attrs, builtins.str):
        attrs = attrs.split()

    def __info__(obj):
        final_attrs = (
            attrs or
            getattr(type(obj), "__info_attrs__", None) or
            sorted(obj.__dict__.keys())
        )
        if isinstance(final_attrs, builtins.str):
            final_attrs = final_attrs.split()
        return sep.join(fmt.format(attr, getattr(obj, attr)) for attr in final_attrs)

    return __info__


# Create a default info function by calling the `info()` function factory with default arguments.
default_info = info()


def klass(cls=None, attrs=(), fmt=DEFAULT_FMT, sep=DEFAULT_SEP):
    """Sets the defaults for __str__, __repr__ and __info__ on the argument class. This function
    can be used as a class decorator or called as a normal function.

    Both __str__ and __repr__ are set to this module's str() and repr() functions only if the
    corresponding methods are not defined directly in the decorated class. If 'attrs' is not
    supplied, it is assumed that __info__() will be implemented by the class. If 'attrs' is
    given, the __info__ method is defined as pretty.info() using the given attribute list,
    format string, and separator. """
    if cls is None:
        return functools.partial(klass, attrs=attrs, fmt=fmt, sep=sep)

    if "__str__" not in cls.__dict__:
        cls.__str__ = str
    if "__repr__" not in cls.__dict__:
        cls.__repr__ = repr
    if attrs or "__info__" not in cls.__dict__:
        cls.__info__ = info(*attrs, fmt=fmt, sep=sep)
    return cls


class PrettyMixin:
    """A mixin that can be added to a class' bases to enable prettier `repr()` and `str()`. The
    contents of the representations can be customized through the `__info_attrs__` class
    attribute.
    """

    __str__ = str
    __repr__ = repr
    __info__ = default_info
    __info_attrs__ = ()
