import search
import json
# def main():
#     for i in range(1):
#         # search.random_evolution()
#         search.evolve()

def main():
    fitness_values = {}

    for i in range(10):
        fitness_values = search.a8_evolve()
        fitness_values[i] = fitness_values

    with open('fitness_values_1.json','w') as f:
        json.dump(fitness_values,f)

if __name__ == "__main__":
    main()