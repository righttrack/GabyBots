"""
Module for interacting with *nix shell from python.
"""

def convert_to_posix_args(*args, **kwargs):
   """
   Flatten all kwargs (filtering out any items with falsy values) into [k1, v1, k2, v2]
   keeping only values that are not of type bool.

   This is useful for passing arguments to a *nix command that accepts posix-style arguments.

   @note: Order is not guaranteed to be preserved
   @return: A tuple of all given args and kwargs converted to posix style arguments
   """
   def get_key(arg):
       if len(arg) > 1:
           return '--' + arg
       else:
           return '-' + arg
   return tuple(
       arg for arg in args + tuple(
           k_or_v
           for k, v in kwargs.items() if bool(v) is True
           for k_or_v in ((get_key(k),) if isinstance(v, bool) else (get_key(k), str(v)))
       )
   )