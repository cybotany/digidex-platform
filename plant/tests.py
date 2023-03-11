# Create your tests here.
import pytest

# Arrange data for tests
class Plant:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_plant():
    return Plant('Jade')

@pytest.fixture
def plant_collection(my_plant):
    return [Plant('Ficus'), my_plant]

def test_my_plant_in_collection(my_plant, plant_collection):
    assert my_plant in plant_collection
