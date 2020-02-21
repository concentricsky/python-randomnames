
from .nouns import NOUNS, ANIMALS
from .adjectives import ADJECTIVES, POLITE_ADJECTIVES
import random

def random_noun():
    return random.choice(NOUNS).title()

def random_animal():
    return random.choice(ANIMALS).title()

def random_adjective():
    return random.choice(ADJECTIVES).title()

def random_polite_adjective():
    return random.choice(POLITE_ADJECTIVES).title()

def random_namepair():
    return "{} {}".format(random_adjective(), random_noun())

def random_polite_animalpair():
    return "{} {}".format(random_polite_adjective(), random_animal())
