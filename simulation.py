import random as r

african_wild_dogs_population = 21
hyena_population = 17
warthog_population = 25
impala_population = 30
zebra_population = 22
cheetah_population = 15

int_pop = african_wild_dogs_population + hyena_population + warthog_population + impala_population + zebra_population + cheetah_population

avg_mort = 0.10
avg_bir = 0.21
avg_mig = 0.05
num_of_years = 50

avg_mortality_rate = {"African Wild Dog": avg_mort, "Hyena": avg_mort, "Warthog": avg_mort, "Impala": avg_mort, "Zebra": avg_mort, "Cheetah": avg_mort}
avg_birth_rate = {"African Wild Dog": avg_bir, "Hyena": avg_bir, "Warthog": avg_bir, "Impala": avg_bir, "Zebra": avg_bir, "Cheetah": avg_bir}
avg_migration_rate = {"African Wild Dog": avg_mig, "Hyena": avg_mig, "Warthog": avg_mig, "Impala": avg_mig, "Zebra": avg_mig, "Cheetah": avg_mig}

Initial_Population_Size = int_pop
Avg_Mortality_Rate = avg_mort
Avg_Birth_Rate = avg_bir
Avg_Migration_Rate = avg_mig
Time_Steps = num_of_years

Species = ["African Wild Dog", "Hyena", "Warthog", "Impala", "Zebra", "Cheetah"]

def initialize_population():
    population = []
    initial_counts = {"African Wild Dog": african_wild_dogs_population,"Hyena": hyena_population,"Warthog": warthog_population,"Impala": impala_population,"Zebra": zebra_population,"Cheetah": cheetah_population,}
    for species, count in initial_counts.items():
        for _ in range(count):
            age = r.randint(1, 15)
            health_status = "Healthy"
            if r.random() > 0.1:
                health_status = "Healthy"
            else:
                if 14 <= age <= 16:
                    if r.random() > 0.9:  
                        health_status = "Sick"
                else:
                    if r.random() > 0.95:  
                        health_status = "Sick"
            individual = {"species": species, "age": age, "health_status": health_status}
            population.append(individual)
    return population

def simulate_births(population, birth_rate):
    new_offspring = []
    births_by_species = {species: 0 for species in Species}
    for individual in population:
        if r.random() < birth_rate:
            offspring = {"species": individual["species"], "age": 0, "health_status": "Healthy"}
            new_offspring.append(offspring)
            births_by_species[individual["species"]] += 1
    return new_offspring, births_by_species

def simulate_mortality(population, mortality_rate):
    survived_population = []
    deaths_by_species = {species: 0 for species in Species}
    for individual in population:
        mortality_chance = mortality_rate * (2 if individual["health_status"] == "Sick" else 1)
        if individual["age"] >= 17 or r.random() < mortality_chance:
            deaths_by_species[individual["species"]] += 1
        else:
            survived_population.append(individual)
    return survived_population, deaths_by_species

def simulate_migration(population, migration_rate):
    migrated_population = []
    migrations_by_species = {species: 0 for species in Species}
    for individual in population:
        if r.random() >= migration_rate:
            migrated_population.append(individual)
        else:
            migrations_by_species[individual["species"]] += 1
    return migrated_population, migrations_by_species

def age_population(population):
    for individual in population:
        individual["age"] += 1
        if 14 <= individual["age"] <= 16:
            if r.random() > 0.9:  
                individual["health_status"] = "Sick"
        elif r.random() > 0.95: 
            individual["health_status"] = "Sick"
            
def is_drought():
    return r.random() < 0.1

def is_famine():
    return r.random() < 0.01

def is_baby_boom():
    return r.random() < 0.05
    
population = initialize_population()
final_population_each_year = []

with open("Savanna Simulation.txt", "w") as file:
    file.write("<---Savanna Wildlife Population Simulation--->\n\n")

    for t in range(1, Time_Steps + 1):
        file.write(f"---Year {t}---\n")

        drought = is_drought()
        if drought:
            file.write("Event: Drought. Water is scarce. Mortality rate increased :(\n")

        famine = is_famine()
        if famine:
            file.write("Event: Famine. Food and water are scarce. Mortality rate increased :(\n")

        baby_boom = is_baby_boom()
        if baby_boom:
            file.write("Event: Conditions are good for a Baby boom! Birth rate increased :)\n")

        current_mortality_rate = Avg_Mortality_Rate * (1.2 if drought else 1) * (1.5 if famine else 1)
        current_birth_rate = Avg_Birth_Rate * (1.5 if baby_boom else 1)

        births, births_by_species = simulate_births(population, current_birth_rate)
        population += births

        population, deaths_by_species = simulate_mortality(population, current_mortality_rate)

        population, migrations_by_species = simulate_migration(population, Avg_Migration_Rate)

        age_population(population)

        file.write("Species Statistics:\n")
        for species in Species:
            species_population = [ind for ind in population if ind["species"] == species]
            if species_population:
                random_individual = r.choice([ind for ind in species_population if ind["age"] > 0] or species_population)
                file.write(f"{species}: Births - {births_by_species[species]}, Deaths - {deaths_by_species[species]}, Migrations - {migrations_by_species[species]}, Final Population - {len(species_population)}, Random Individual - Age: {random_individual['age']}, Health Status: {random_individual['health_status']}\n")
            else:
                file.write(f"{species}: Births - {births_by_species[species]}, Deaths - {deaths_by_species[species]}, Migrations - {migrations_by_species[species]}, Final Population - 0, No individuals available\n")

        total_population = len(population)
        final_population_each_year.append(total_population)
        file.write(f"Total final population for year {t}: {total_population}\n\n")

    file.write("----Simulation complete----\n")



