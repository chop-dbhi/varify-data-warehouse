from django.dispatch import Signal

pre_delete_sample = Signal(providing_args=['pk_set', 'cursor'])
pre_delete_project = Signal(providing_args=['pk', 'cursor'])
