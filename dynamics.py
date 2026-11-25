import random

african_wild_dogs_population = 21
hyena_population = 17
warthog_population = 25
impala_population = 30
zebra_population = 22
cheetah_population = 15
Species = ["African Wild Dog", "Hyena", "Warthog", "Impala", "Zebra", "Cheetah"]

def initialize_population():
    population = []
    initial_counts = {"African Wild Dog": african_wild_dogs_population,"Hyena": hyena_population,"Warthog": warthog_population,"Impala": impala_population,"Zebra": zebra_population,"Cheetah": cheetah_population,}
    for species, count in initial_counts.items():
        for _ in range(count):
            age = random.randint(1, 15)
            health_status = "Healthy"
            if random.random() > 0.1:
                health_status = "Healthy"
            else:
                if 14 <= age <= 16:
                    if random.random() > 0.9:  
                        health_status = "Sick"
                else:
                    if random.random() > 0.95:  
                        health_status = "Sick"
            individual = {"species": species, "age": age, "health_status": health_status}
            population.append(individual)
    return population

def simulate_births(population, birth_rate):
    new_offspring = []
    births_by_species = {species: 0 for species in Species}
    for individual in population:
        if random.random() < birth_rate:
            offspring = {"species": individual["species"], "age": 0, "health_status": "Healthy"}
            new_offspring.append(offspring)
            births_by_species[individual["species"]] += 1
    return new_offspring, births_by_species

def simulate_mortality(population, mortality_rate):
    survived_population = []
    deaths_by_species = {species: 0 for species in Species}
    for individual in population:
        mortality_chance = mortality_rate * (2 if individual["health_status"] == "Sick" else 1)
        if individual["age"] >= 17 or random.random() < mortality_chance:
            deaths_by_species[individual["species"]] += 1
        else:
            survived_population.append(individual)
    return survived_population, deaths_by_species

def simulate_migration(population, migration_rate):
    migrated_population = []
    migrations_by_species = {species: 0 for species in Species}
    for individual in population:
        if random.random() >= migration_rate:
            migrated_population.append(individual)
        else:
            migrations_by_species[individual["species"]] += 1
    return migrated_population, migrations_by_species

def age_population(population):
    for individual in population:
        individual["age"] += 1
        if 14 <= individual["age"] <= 16:
            if random.random() > 0.9:  
                individual["health_status"] = "Sick"
        elif random.random() > 0.95: 
            individual["health_status"] = "Sick"