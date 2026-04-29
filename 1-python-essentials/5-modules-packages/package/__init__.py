"""Package notes for local import examples.

`__init__.py` tells Python that this directory should behave like a package.
It can stay empty, but it is also a good place to expose the parts of the
package that we want to import more easily.
"""

from .calc import add, subtract

__all__ = ["add", "subtract"]
