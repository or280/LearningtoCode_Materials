import numpy as np

# Unit cell parameters a, b, c, alpha, beta, gamma:
# cell lengths in nm and angles in radians.
cellparams = (0.541, 0.541, 0.541, np.pi/2, np.pi/2, np.pi/2)

# Fractional coordinates of atoms in the unit cell.
atoms = [( 'Zn', (0.25, 0.25, 0.25) ),
         ( 'Zn', (0.75, 0.75, 0.25) ),
         ( 'Zn', (0.75, 0.25, 0.75) ),
         ( 'Zn', (0.25, 0.75, 0.75) ),
         ( 'S', (0.0, 0.0, 0.0) ),
         ( 'S', (0.5, 0.5, 0.0) ),
         ( 'S', (0.5, 0.0, 0.5) ),
         ( 'S', (0.0, 0.5, 0.5) ),
        ]

# List of X-ray reflections (h, k, l) and multiplicities.
reflections = [((1,1,1), 8),
               ((2,0,0), 6),
               ((2,2,0), 12),
               ((3,1,1), 24),
               ((2,2,2), 8),
               ((4,0,0), 6),
               ((3,3,1), 24),
               ((4,2,0), 24),
               ((4,2,2), 24),
               ((5,1,1), 24),
               ((4,4,0), 12),
               ((5,3,1), 48),
               ((6,2,0), 24),
               ((5,3,3), 24)
              ]
