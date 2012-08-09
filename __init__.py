"""time.monotonic() for older versions of python.

If time.monotonic() doesn't already exist, this module monkey patches it
in so that people looking for it will find it.  That function is available
starting in python 3.3; with this extension, it becomes available in
earlier versions too.

Somewhere in your program you need to 'import monotime' first.  After
that, any module looking for time.monotonic() will find it successfully.
"""

from _monotime import monotonic


import time as _time
if not hasattr(_time, 'monotonic'):
  _time.monotonic = monotonic
