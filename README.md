# Savanna Ecosystem Simulation

A stochastic Python simulation of wildlife populations in a savanna ecosystem. It tracks African wild dogs, hyenas, warthogs, impalas, zebras and cheetahs over 50 simulated years.

**Author:** Luca Brandao  
**Coursework:** CTIP152 SS3 · Bachelor of Business Information Systems, STADIO Higher Education  
**Stack:** Python

## Features

- Six initial species populations and individual age/health records.
- Births, mortality, migration and ageing during each year.
- Random drought, famine and baby-boom events that alter rates.
- Per-species statistics and a total population for each time step.
- A generated plain-text report, with an annotated notebook alternative.

## Requirements and setup

Use Python 3.10 or newer. No third-party packages are required for the script. From this project folder:

```sh
python simulation.py
```

Alternatively open `simulation.ipynb` in Jupyter and run the cells in order.

## Using the project

The run writes `Savanna Simulation.txt` in the working directory. It contains a year-by-year event log, birth/death/migration counts, final population sizes and a sampled individual. Running it again replaces that generated report. Change the initial populations, average rates or `num_of_years` near the top of the script to explore another scenario.

## How it works

Individuals are dictionaries held in a population list. Each iteration applies births, mortality and migration, then updates ages and health. Event probabilities modify the base rates. `dynamics.py` contains the extracted population helper functions; `events.py` contains event-probability helpers. The main script/notebook retains the integrated coursework implementation.

## Project files

- `simulation.py`: complete simulation entry point.
- `simulation.ipynb`: original annotated workflow.
- `dynamics.py`: population helper functions and their default settings.
- `events.py`: drought, famine and baby-boom probability helpers.

## Portfolio preparation

Sampling falls back to the surviving species population when no older individual is available. Default settings were added to the extracted `dynamics.py` helper so it can be imported and used independently.

Notebook outputs, personal submissions, IDE settings, compiled classes, dependency folders and assignment/presentation files are not included. See [PROJECT.md](PROJECT.md) for the academic context.

## Limitations and troubleshooting

The model is an educational simplification, not an ecological prediction tool. It does not model spatial movement, predation, food networks or calibrated species-specific rates. Results vary because the simulation is random. Generated reports are ignored by Git.

## Portfolio

[My GitHub profile](https://github.com/Luca-Brandao) · [LinkedIn](https://www.linkedin.com/in/luca-brandao-a90961352/)
