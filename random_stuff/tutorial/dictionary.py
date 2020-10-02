birds = {"pigeon": 12,
         "sparrow": 5,
         "red crossbill": 1}

prices = {"espresso": 5.0,
          "americano": 8.0,
          "latte": 10,
          "pastry": "various prices"}

empty_dict = {}
empty_dict_2 = dict()

prices_with_constr = dict({"espresso": 5.0,},
                          americano=8.0,
                          latte=10,
                          pastry="Various")

my_pets = {"dog": {"name": "dolly", "breed": "collie"},
           "cat": {"name": "fluffy", "breed": "maine coon"}}

digits = {1: {'Word': 'one', 'Roman': 'I'},
          2: {'Word': 'two', 'Roman': 'II'},
          3: {'Word': 'three', 'Roman': 'III'},
          4: {'Word': 'four', 'Roman': 'IV'},
          5: {'Word': 'five', 'Roman': 'V'}}

my_pet = {}

my_pet["name"] = "Dolly"
my_pet["animal"] = "dog"
my_pet["breed"] = "collie"

trilogy = {'IV': 'Star Wars', 'V': 'The Empire Strikes Back', 'VI': 'Return of the Jedi'}
trilogy["IV"] = "A new hope"

# Operations with dictionaries

testable = {"key1": "value1", "key2": "value2"}
testable["key"] = "Value"

catalog = {"green table": 5000,
           "brown chair": 1500,
           "blue sofa": 15000,
           "wardrobe": 10000}

for key, value in catalog.items():
    print(f"The {key} costs {value}.")
