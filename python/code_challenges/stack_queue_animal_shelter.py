from data_structures.queue import Queue



class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()  # Queue for dogs
        self.cat_queue = Queue()  # Queue for cats
        self.order = 0  # To keep track of the order of arrival


    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)
        else:
            raise ValueError("Animal must be an instance of Dog or Cat")

    def dequeue(self, pref):
            if pref == "dog":
                return self._dequeue_dog()
            elif pref == "cat":
                return self._dequeue_cat()
            else:
                return None

    def _dequeue_dog(self):
            if not self.dog_queue.is_empty():
                oldest_dog = self.dog_queue.dequeue()
                return oldest_dog
            else:
                return None

    def _dequeue_cat(self):
        if not self.cat_queue.is_empty():
            oldest_cat = self.cat_queue.dequeue()
            return oldest_cat  # Return the Cat object instead of the name
        else:
            return None
        
class Dog:
    def __init__(self, name):
        self.species = "dog"
        self.name = name


class Cat:
    def __init__(self, name):
        self.species = "cat"
        self.name = name

