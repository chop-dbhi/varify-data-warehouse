from vdw.conf import settings
from django.core.exceptions import ImproperlyConfigured

__version_info__ = {
    'major': 0,
    'minor': 4,
    'micro': 2,
    'releaselevel': 'beta',
    'serial': 1
}


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i.%(micro)i" % __version_info__, ]
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0],
                    __version_info__['serial']))
    return ''.join(vers)

__version__ = get_version()

if getattr(settings, 'VDW_GENOME_VERSION', None) is None:
    raise ImproperlyConfigured(
        'VDW_GENOME_VERSION must be defined in settings.')
