# -*- coding: utf-8 -*-
"""CIGENETIC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SgsHtRoOajevKxJ450k7GlCF0IcKCGCv
"""

import random

def generate_random_population(pop_size, genotype_length):
    population = []
    for _ in range(pop_size):
        genotype = [random.randint(0, 1) for _ in range(genotype_length)]  # Binary encoding
        population.append(genotype)
    return population
pop_size = 10  # Population size
genotype_length = 8  # Length of each genotype (chromosome)

population = generate_random_population(pop_size, genotype_length)
print("Random Population:")
for individual in population:
    print(individual)

def generate_heuristic_population(pop_size, genotype_length, heuristic):
    population = []
    for i in range(pop_size // 2):
        heuristic_genotype = heuristic(genotype_length)
        population.append(heuristic_genotype)

    population.extend(generate_random_population(pop_size // 2, genotype_length))
    return population
def sample_heuristic(genotype_length):
    return [1 if i < genotype_length // 2 else 0 for i in range(genotype_length)]
population = generate_heuristic_population(pop_size, genotype_length, sample_heuristic)
print("Heuristic Population:")
for individual in population:
    print(individual)

import random
def generate_random_population(pop_size, genotype_length, genotype_type='binary', min_val=0, max_val=1):
    population = []
    for _ in range(pop_size):
        if genotype_type == 'binary':
            genotype = [random.randint(0, 1) for _ in range(genotype_length)]  # Binary genotype
        elif genotype_type == 'integer':
            genotype = [random.randint(min_val, max_val) for _ in range(genotype_length)]  # Integer genotype
        elif genotype_type == 'float':
            genotype = [random.uniform(min_val, max_val) for _ in range(genotype_length)]  # Float genotype
        population.append(genotype)
    return population

# 2. Heuristic Population
def generate_heuristic_population(pop_size, genotype_length, genotype_type='binary', heuristic=None, min_val=0, max_val=1):
    population = []

    for i in range(pop_size // 2):
        if genotype_type == 'binary':
            heuristic_genotype = [1 if i < genotype_length // 2 else 0 for i in range(genotype_length)]
        elif genotype_type == 'integer':
            heuristic_genotype = [min_val + i % (max_val + 1) for i in range(genotype_length)]
        elif genotype_type == 'float':
            heuristic_genotype = [min_val + i * (max_val - min_val) / genotype_length for i in range(genotype_length)]

        population.append(heuristic_genotype)
    population.extend(generate_random_population(pop_size // 2, genotype_length, genotype_type, min_val, max_val))

    return population
pop_size = 10
genotype_length = 8

print("Random Population (Binary Genotype):")
binary_population = generate_random_population(pop_size, genotype_length, genotype_type='binary')
for individual in binary_population:
    print(individual)

print("\nRandom Population (Integer Genotype):")
integer_population = generate_random_population(pop_size, genotype_length, genotype_type='integer', min_val=0, max_val=9)
for individual in integer_population:
    print(individual)

print("\nRandom Population (Float Genotype):")
float_population = generate_random_population(pop_size, genotype_length, genotype_type='float', min_val=0.0, max_val=1.0)
for individual in float_population:
    print(individual)

# 2. Heuristic Population Generation (Binary, Integer, Float)
print("\nHeuristic Population (Binary Genotype):")
binary_heuristic_population = generate_heuristic_population(pop_size, genotype_length, genotype_type='binary')
for individual in binary_heuristic_population:
    print(individual)

print("\nHeuristic Population (Integer Genotype):")
integer_heuristic_population = generate_heuristic_population(pop_size, genotype_length, genotype_type='integer', min_val=0, max_val=9)
for individual in integer_heuristic_population:
    print(individual)

print("\nHeuristic Population (Float Genotype):")
float_heuristic_population = generate_heuristic_population(pop_size, genotype_length, genotype_type='float', min_val=0.0, max_val=1.0)
for individual in float_heuristic_population:
    print(individual)

"""question 2
**Parent Selection using different methods.**

*   Roulette Wheel Selection (Fitness Proportional)
Tournament Selection
Rank Selection
Stochastic Universal Sampling (SUS)


"""

import random

def fitness_function(individual):
    return sum(individual)

def roulette_wheel_selection(population):
    total_fitness = sum(fitness_function(individual) for individual in population)
    selection_probs = [fitness_function(individual) / total_fitness for individual in population]

    parent = random.choices(population, selection_probs, k=1)[0]
    return parent

def tournament_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    tournament_fitness = [(individual, fitness_function(individual)) for individual in tournament]

    parent = max(tournament_fitness, key=lambda x: x[1])[0]
    return parent

def rank_selection(population):
    ranked_population = sorted(population, key=lambda x: fitness_function(x), reverse=True)

    rank_sum = sum(range(1, len(population) + 1))
    selection_probs = [rank / rank_sum for rank in range(1, len(population) + 1)]

    parent = random.choices(ranked_population, selection_probs, k=1)[0]
    return parent

def stochastic_universal_sampling(population):
    total_fitness = sum(fitness_function(individual) for individual in population)
    distance = total_fitness / len(population)
    start_point = random.uniform(0, distance)

    pointer = start_point
    cumulative_fitness = 0

    for individual in population:
        cumulative_fitness += fitness_function(individual)
        if cumulative_fitness >= pointer:
            return individual
        pointer += distance
population = [[random.randint(0, 1) for _ in range(5)] for _ in range(10)]

print("Initial Population:")
for i, individual in enumerate(population):
    print(f"Individual {i+1}: {individual}, Fitness: {fitness_function(individual)}")

print("\nParent Selection Using Different Methods:")

parent_rw = roulette_wheel_selection(population)
print(f"Roulette Wheel Selection: {parent_rw}, Fitness: {fitness_function(parent_rw)}")
parent_ts = tournament_selection(population)
print(f"Tournament Selection: {parent_ts}, Fitness: {fitness_function(parent_ts)}")
parent_rs = rank_selection(population)
print(f"Rank Selection: {parent_rs}, Fitness: {fitness_function(parent_rs)}")
parent_sus = stochastic_universal_sampling(population)
print(f"Stochastic Universal Sampling: {parent_sus}, Fitness: {fitness_function(parent_sus)}")



"""q3
**Single Point Crossover**: This method randomly selects a crossover point, then swaps the genetic material (genes) after the crossover point between two parents.
**Two Point Crossover:** Two crossover points are chosen. The genes between these two points are swapped between the parents to create offspring.
**Uniform Crossover**: This method randomly chooses genes from either parent with equal probability for each position in the chromosome.


"""

import random
def print_chromosome(chromosome):
    print(' '.join(map(str, chromosome)))


def single_point_crossover(parent1, parent2):
    length = len(parent1)
    crossover_point = random.randint(1, length - 1)
    print(f'Crossover Point: {crossover_point}')

    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    print("Offspring 1 (Single Point Crossover):", end=" ")
    print_chromosome(offspring1)
    print("Offspring 2 (Single Point Crossover):", end=" ")
    print_chromosome(offspring2)

    return offspring1, offspring2


def two_point_crossover(parent1, parent2):
    length = len(parent1)
    point1 = random.randint(1, length - 1)
    point2 = random.randint(1, length - 1)


    if point1 > point2:
        point1, point2 = point2, point1

    print(f'Crossover Points: {point1}, {point2}')

    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    print("Offspring 1 (Two Point Crossover):", end=" ")
    print_chromosome(offspring1)
    print("Offspring 2 (Two Point Crossover):", end=" ")
    print_chromosome(offspring2)

    return offspring1, offspring2


def uniform_crossover(parent1, parent2):
    length = len(parent1)
    offspring1 = []
    offspring2 = []

    for i in range(length):
        if random.random() < 0.5:
            offspring1.append(parent1[i])
            offspring2.append(parent2[i])
        else:
            offspring1.append(parent2[i])
            offspring2.append(parent1[i])

    print("Offspring 1 (Uniform Crossover):", end=" ")
    print_chromosome(offspring1)
    print("Offspring 2 (Uniform Crossover):", end=" ")
    print_chromosome(offspring2)

    return offspring1, offspring2


parent1 = [1, 0, 1, 0, 1, 1, 0]
parent2 = [0, 1, 1, 1, 0, 0, 1]

print("Parent 1:", end=" ")
print_chromosome(parent1)
print("Parent 2:", end=" ")
print_chromosome(parent2)

offspring_sp1, offspring_sp2 = single_point_crossover(parent1, parent2)
offspring_tp1, offspring_tp2 = two_point_crossover(parent1, parent2)
offspring_uc1, offspring_uc2 = uniform_crossover(parent1, parent2)

"""q4
Bit Flip Mutation (for binary chromosomes)
Swap Mutation (for permutations)

Gaussian Mutation (for real-valued chromosomes)
mutation_value = current_gene_value + N(0, mutation_strength)

"""

import random
def print_chromosome(chromosome):
    print(' '.join(map(str, chromosome)))
def bit_flip_mutation(chromosome, mutation_rate=0.1):
    new_chromosome = chromosome[:]
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            new_chromosome[i] = 1 - chromosome[i]  # Flip the bit (0 -> 1, 1 -> 0)
    return new_chromosome

def swap_mutation(chromosome, mutation_rate=0.1):
    new_chromosome = chromosome[:]
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        new_chromosome[i], new_chromosome[j] = new_chromosome[j], new_chromosome[i]
    return new_chromosome

def gaussian_mutation(chromosome, mutation_rate=0.1, mutation_strength=0.5):
    new_chromosome = chromosome[:]
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            # Apply Gaussian noise (small random change)
            new_chromosome[i] += random.gauss(0, mutation_strength)
    return new_chromosome


parent_binary = [1, 0, 1, 0, 1, 1, 0]
print("Parent Binary Chromosome:", end=" ")
print_chromosome(parent_binary)

offspring_binary = bit_flip_mutation(parent_binary, mutation_rate=0.2)
print("Offspring Binary Chromosome (Bit Flip Mutation):", end=" ")
print_chromosome(offspring_binary)

parent_permutation = [3, 1, 4, 5, 2]
print("\nParent Permutation Chromosome:", end=" ")
print_chromosome(parent_permutation)


offspring_permutation = swap_mutation(parent_permutation, mutation_rate=0.5)
print("Offspring Permutation Chromosome (Swap Mutation):", end=" ")
print_chromosome(offspring_permutation)


parent_real = [0.1, 0.5, 0.3, 0.7]
print("\nParent Real-Valued Chromosome:", end=" ")
print_chromosome(parent_real)


offspring_real = gaussian_mutation(parent_real, mutation_rate=0.3, mutation_strength=0.2)
print("Offspring Real-Valued Chromosome (Gaussian Mutation):", end=" ")
print_chromosome(offspring_real)
