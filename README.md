# Conway's Game of Life: Analyzing Population Behavior on Different Surfaces  

This project explores the dynamics of **Conway's Game of Life**, a well-known cellular automaton, on various surfaces (square, torus, sphere). The study investigates the impact of initial population density, board size, and surface type on population persistence and behavior over time.

---

## **Project Overview**  
- **Goal**: To analyze how different parameters (initial density, board size, surface type) affect the end population density and the number of iterations required to reach stability.  
- **Motivation**: Cellular automata like the Game of Life have applications in systems modeling, population dynamics, and understanding emergent behavior in complex systems.  
- **Surfaces Explored**:
  - **Square**: A bounded surface with edges.  
  - **Torus**: A surface that wraps horizontally and vertically.  
  - **Sphere**: A closed, curved surface where boundaries are redefined.  

---

## **Project Files and Organization**  
1. `notebooks/`: Contains the main Jupyter Notebook for simulations and visualizations.  
   - `GameOfLife_Analysis.ipynb`: The primary analysis notebook.  

2. `data/`: Stores data generated during simulations.  
   - `project_data_sphere.csv`: Processed data with population statistics for different surfaces.  

3. `src/`: Core Python functions and scripts.  
   - `game_of_life.py`: Contains utility functions for board setup, game advancement, and neighbor calculations.  
   - `visualization.py`: Functions for plotting results.  

4. `outputs/`: Generated visualizations and figures.  
   - Comparison plots and statistical summaries.  

5. `README.md`: This file, providing an overview of the project.  

6. `requirements.txt`: Dependencies and Python packages used in the project.  

---

## **Key Results**  
1. **Population Persistence**: Lifespan is highest on a sphere, followed by a torus, and then a square.  
2. **End Fraction**: The fraction of alive cells stabilizes around 0.03 across all surfaces and board sizes.  
3. **Iteration Behavior**: Iterations required for stability follow a bump function centered around an initial density of 0.4.  

---

## **Technologies Used**  
- **Python Libraries**:  
  - `NumPy`: Data handling and board initialization.  
  - `Pandas`: Data manipulation and statistical analysis.  
  - `Matplotlib` and `Seaborn`: Data visualization.
  - `IPython.display` : Board visualization
- **Jupyter Notebook**: For interactive data analysis.  

---

## **How to Run the Project**  

### Prerequisites  
1. Install Python 3.8+ and set up a virtual environment.  
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
