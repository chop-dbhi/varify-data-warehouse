from global_settings import *   # noqa

try:
    from local_settings import *    # noqa
except ImportError:
    import warnings
    warnings.warn(
        'Local settings have not been found (vdw.conf.local_settings)')
