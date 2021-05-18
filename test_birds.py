from pytest import approx, fixture
import random

import collection_birds as coll

RANDOM_SEED = 0

def random_bird():
    """Randomly select a bird from a list."""
    birds = ["penguin", "ostrich", "falcon", "robin"]
    return random.choice(birds)

def test_random_bird():
    random.seed(RANDOM_SEED)
    choices = [random_bird() for i in range(4)]
    assert choices == ["penguin", "penguin", "falcon", "robin"]


@fixture
def pseudorandom_sequence(self):
    random.seed(RANDOM_SEED)
    random.randint(1,4)
    sequence = []
    while random.count(0) > 1 or random.count(1) > 2:
        birds = ["penguin", "ostrich", "falcon", "robin"]
        item = birds.index()
        sequence.append(birds)
        assert coll.populate()
    return None

@fixture
def test_populate():
    return None

@fixture
def bird_populating(self, coordinates, pseudorandom_sequence):
    assert coll.populate()
    item = pseudorandom_sequence
