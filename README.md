# InfectionSim
`infectionSim` is a python GUI application with command-line variable for simulate the spread of an airborne infectious disease through a population, modeling transmission dynamics and individual infection outcomes. 
Individuals may be **healthy (and susceptible), infected (sick), vaccinated or carrier**
The model is conceptually inspired by respiratory infections such as **COVID-19, influenza, and measles**

Note: The probabilistic formulation used in this model is not scientifically accurate, but it provides a good visual representation of how an infectious disease spreads through a population (it is not modelled with differential equations).

## Features

Type of possible cells status and color coding:
- healthy people = blue cells
- vaccinated or immune people = green cells
- carrier people = yellow cells
- infected (with symptoms or not) = red cells
- non people (to indicate the absence of trasmission media) = black cells

Initial variables:
- % density of population = N people / N total cells 
- % healthy people = N healthy people / N total people
- % carrier people = N carrier people / N total people
- % sick people = N sick people / N total people
- % vaccinated people = N vaccinated people / N total people
Note: The percentages of healthy, sick, carrier, and vaccinated individuals must add up to 100%.

## Requirements

- Python 3.9 or newer
- the dependencies wrote in the requirements.txt file

The application uses:
- `numpy` for the matrix handling
- `pygame-ce` for GUI managing and keyboard features
Other eventual libraries are builtin

## Installation

1. Clone the repository and enter its directory:

	```bash
	git clone https://github.com/zj4ck3/infectionSim.git
	cd infectionSim
	```

2. Create and activate a virtual environment (recommended):

	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

	On Windows PowerShell, activate it with:

	```powershell
	.venv\Scripts\Activate.ps1
	```

3. Install the dependencies:

	```bash
	python3 -m pip install -r requirements.txt
	```

4. Install the package in editable mode:

	```bash
	python3 -m pip install -e .
	```

## Usage

Start the application with:

```bash
python3 src/main.py
```

Usage:
- initialization = it asks you some command-line variables about density of population and starting information.
- running phase:
  - SPACE = Pause the simulation
  - Click "X" = Quit the simulation

## Project Structure

```text
infectionSim/
├── src/                    # Source code
│   ├── main.py             # Application entry point
│   ├── simulation.py       # Pygame rendering and simulation updates
│   └── person.py           # Person class and health status transitions
├── tests/                  # Automated tests
│   ├── test_person.py      # Tests for person.py
│   └── test_simulation.py  # Tests for simulation.py
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
├── README.md               # Project documentation
└── pyproject.toml          # Project metadata and test configuration
```

## Contributing

Bug reports, suggestions, and pull requests are welcome. Before submitting a change, verify that the application starts successfully and that the tests are all passed

## License

This project is licensed under the [MIT License](LICENSE).