# -* coding: utf-8 *-
# System imports
# Third-party imports
from pbr.version import VersionInfo

# Local imports
__all__ = (
    '__version__',
    'version_info'
)

_v = VersionInfo('papyr').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()