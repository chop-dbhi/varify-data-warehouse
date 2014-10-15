from django.db import models
from avocado.lexicon.models import Lexicon


class Chromosome(Lexicon):
    label = models.CharField(max_length=2)
    value = models.CharField(max_length=2, db_index=True)

    class Meta(Lexicon.Meta):
        db_table = 'chromosome'


class Genotype(Lexicon):
    label = models.CharField(max_length=20)
    value = models.CharField(max_length=3)

    class Meta(object):
        db_table = 'genotype'
