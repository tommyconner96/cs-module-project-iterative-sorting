#runtime review
import time
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
# A: O(1)
def print_animal(animals):
    print(animals[0])
# B: O(1)
def print_animals_0(animals):
    for _ in range(1000):
        print(animals[0])
# C: O(n)
def print_animals_1(animals):
    for animal in animals:
        print(animal)
# D: O(n)
def print_animals_2(animals):
    for animal in animals:
        for i in range(1000):
            print(i, animal)
# E: O(n^2)
def print_animal_pairs(animals):
    for animal_1 in animals:
        for animal_2 in animals:
            print(f"{animal_1} - {animal_2}")
# F: O(n^3)
def print_animal_triples(animals):
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")
# G: O(log n)
def free_animals(animals):
    while len(animals) > 0:
        animals = animals[0: len(animals) // 2]
# H: O(n log n)
def insert_array(n):
    arr = []
    for i in range(n):    # O(n) because of loop
        arr.insert(0, i)  # O(n) because we're inserting at the front
        # arr.append(i)
def time_insert():
    for n in [1000, 10000, 100000, 1000000]:
        start = time.time()
        insert_array(n)
        end = time.time()
        print(f"{n}: \t {end-start}")
time_insert()
# I: O(n log n)
def bst_random(random_nums, target):
    bst = BSTNode(random_nums[0])
    # overall: n log n
    for num in random_nums[1:]: # O(n)
        bst.insert(num)     # O(log n)
    bst.contains(target)    # O(log n)
    # in whole: n log n + log n --> n log n
bst_random([8, 4, 16, 1, 3, 12, 6, 5, 7, 2, 15, 13, 14, 10, 9, 11], 13)
# J: O(n^2)
def bst_ordered(n, target):
    bst = BSTNode(0)
    # Overall for the next two lines: O(n^2)
    for i in range(1, n):  # n
        bst.insert(i)      # n
    bst.contains(target)  # n
    # Overall: n^2 (for the loop) + n (for the contains) --> n^2
bst_ordered(16, 13)