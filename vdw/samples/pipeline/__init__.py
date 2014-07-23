from vdw.pipeline import Channel

SAMPLE_CHANNEL = Channel('samples', ['manifest_path', 'database'])


# Setup local handlers to watch the channels of interest..
from vdw.variants.pipeline import VARIANT_CHANNEL
from . import handlers
handlers.load_results.watch(VARIANT_CHANNEL)
