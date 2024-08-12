# Conway's Game of Life Simulation

This project is a simulation of Conway's Game of Life, implemented in Python using the Pygame library. Conway's Game of Life is a cellular automaton devised by mathematician John Conway. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

## Features

- **Grid-Based Simulation**: The simulation runs on a grid where each cell can either be alive or dead.
- **Real-Time Updates**: The grid updates in real-time, showing the progression of cells according to Conway's rules.
- **Customizable Grid Size**: The grid size can be adjusted to suit different simulation scales.
- **Interactive Controls**: Start, pause, and reset the simulation as needed.

## Installation

### Prerequisites

- Python 3.x
- Pygame library

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/game-of-life.git
    cd game-of-life
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Simulation

To start the simulation, run the following command:

```bash
python main.py
