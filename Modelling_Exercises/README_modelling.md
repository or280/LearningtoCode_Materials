## iPython Notebooks for Part II Materials Science C1: Introduction to Materials Modelling

<ol>
<li>

[Buffon's Needle: buffons_needle.ipytb](https://partiic1-jae1001.notebooks.azure.com/j/notebooks/buffons_needle.ipynb)

**Description**

Illustrates the principle of statistical sampling methods (rudimentary Monte Carlo) for estimating
the value of pi by dropping a needle randomly onto a lined grid. It can be be shown (see lectures
and example sheet q.5) that the value of pi is related to the ratio of number of times the needles
land intersecting the grid to the total number of throws.

**Usage**

No user defined parameters required. Interactive widget should launch at runtime.
Start the process by pressing Play/Pause button. Control speed of drops by Faster/Slower buttons
As needles drop, the cumulative estimate of pi is displayed, along with the Z-score (measure of 
how many standard deviations away from 'real' value of pi the estimate is). Can show (see examples
sheet q.5) that convergence should go as reciprocal of square root of number of drops.

**Credits**

Original Python code written by Andrew Fowler (University of Cambridge), with some modifications
by James Elliott
</li>

<li>

[Democritus: democritus.ipytb](https://partiic1-jae1001.notebooks.azure.com/j/notebooks/democritus.ipynb)

**Description**

Simple molecular dynamics (MD) simulation of 2D periodic Lennard-Jones fluid at constant temperature
and volume (NVT ensemble). Illustrates the principle of continuous time MD using a differentiable
potential function to calculate forces. Uses velocity Verlet algorithm to integrate the equations of
motion. Outputs temperature, pressure and density (and their standard errors) in dimensionless units.

**Usage**

Requires definition of initial particle positions (x,y) coords from plain text file 'initial.dat'
An example 'initial.dat' with 36 particles is given with the notebook (must be in same path as notebook)
Main user defined parameter is BoxSize, which controls the size (area) of square box.
Initial value of BoxSize = 11.0, and suggest to vary between 7.0 and 25.0 to answer q.3 
Do not change the number of particles or dimensionality of the box unless you know what you're doing!

**Credits**

Python code by Jacob Martin (University of Cambridge) adapted from original FORTRAN by Furio Ercolessi
(SISSA, Trieste) and some modifications by James Elliott
</li>

<li>

[Potts model: potts.ipynb](https://partiic1-jae1001.notebooks.azure.com/j/notebooks/potts.ipynb)

**Description**

Implementation of Monte Carlo (MC) model for grain growth (Potts model) at constant temperature. Uses
the Metropolis algorithm to simulate the coarsening of random grain structure on square lattice.

**Usage**

User editable settings are size of array (N,M), number of possible grain orientations (set by default
to NxM, but can make N = 2 to recover Ising model), and total number of Monte Carlo steps (MCS). Outputs
are the grain microstructure after each Monte Carlo step, and the number of unique grain orientations
as a function of steps. Advisable to keep the array sizes below 100 to avoid excessive compute time.
Typically requires around 1000 MCS to achieve convergence.

4/3/2020 - - added variants: [Ising model: potts_zener.ipynb](https://partiic1-jae1001.notebooks.azure.com/j/notebooks/potts_zener.ipynb) which implements the substitution of inert sites on the lattice (precipitates) to simulate the effects of Zener pinning discussed in lecture 5. The fraction of inert sites on lattice (f) can be controlled by additional user-defined parameter f_defects. For *low* fractions of pinning sites (< 5%) the Zener-Smith formula predicts that stagnation grain size should vary with reciprocal of f. NOTE: there is a known issue with the way the defects are added, which means the fraction of inert sites may be lower than f_defects, but this effect should be small for low f. ALSO: for for f = 0, the code *should* reproduce same scaling as original Potts code, BUT this has not been thoroughly tested, so best to use the original code for testing the scaling of grain size with MCS (time).

**Credits**

Python code by Fabian A. (Stack Exchange) and modified by James Elliott
</li>

<li>

[Ising model: ising.ipynb](https://partiic1-jae1001.notebooks.azure.com/j/notebooks/ising.ipynb)

**Description**

Implementation of Monte Carlo (MC) model for Ising model for a ferromagnet (special case of Potts model for 2 orientations, or spins, see section 6.4 in notes)) at constant temperature. Uses the Metropolis algorithm (6.3) to simulate the evolution of spin lattice on square lattice.

**Usage**

User editable settings are size of array (N,M) and total number of Monte Carlo steps (MCS). Outputs
are the spin microstructure after each Monte Carlo step, and the net magnetisation per spin (i.e. the difference between number of spin up minus spin down states) as a function of steps. Advisable to keep the array sizes below 100 to avoid excessive compute time. Try experimenting with behaviour of model above and below the critical (Curie) temperature for 2D square lattice (approximately 2.27 in dimensionless units).

2/3/2020 - added two variants: [Ising model: ising_highT.ipynb](https://partiic1-jae1001.notebooks.azure.com/j/notebooks/ising_highT.ipynb) and [Ising model: ising_lowT.ipynb](https://partiic1-jae1001.notebooks.azure.com/j/notebooks/ising_lowT.ipynb) which simulate above and below the Curie temperature, respectively, so these can be shown in lectures without rerunning the code.

**Credits**

Python code by Fabian A. (Stack Exchange) and modified by James Elliott
</li>