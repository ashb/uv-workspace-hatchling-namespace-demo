try:
    from ._version import __version__
except ImportError:
    __version__ = "0+unknown"

__version__ = __version__ + "+t1"
