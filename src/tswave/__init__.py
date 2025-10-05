from importlib.metadata import version as _v, PackageNotFoundError
try:
    __version__ = _v("tswave")
except PackageNotFoundError:  # during local development
    __version__ = "0.0.0"
