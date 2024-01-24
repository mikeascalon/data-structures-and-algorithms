import pytest
from code_challenges.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


# @pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat("tiger")
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog("wolf")
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat("tiger")
    dog = Dog("wolf")
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


@pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat("tiger")
    dog = Dog("wolf")
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat("tiger")
    dog = Dog("wolf")
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual
