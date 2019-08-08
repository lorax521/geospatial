"""
Create kdtree as follows:
kdtree = cKDTree(xy)

Where xy is a 2d array of coordinate pairs like below:
array([[-81.720001,  24.48    ],
   [-81.919998,  24.530001],
   [-82.160004,  24.549999],
   ...,
   [-82.449997,  37.799999],
   [-82.400002,  37.799999],
   [-82.449997,  37.849998]])
"""

import numpy as np
from scipy.spatial import cKDTree

def idw(kdtree,z,xi,yi):
    """ Inverse Distance Weighting - interpolates an unknown value at a 
    specified point by weighting the values of it's nearest neighbors

    Keyword arguments:
        kdtree: scipy.spatial.ckdtree -- kdtree made from a 2d array of x and y coordinates as the columns 
        z: 1d array -- point values at each location
        xi: float -- x-axis point location of unknown value
        yi: float -- y-axis point location of unknown value
    
    Returns:
        zi: float -- interpolated value at xi, yi

    """
    neighbors = 12
    power = 2
    distances, indicies = kdtree.query([xi,yi], k=neighbors)
    z_n = z[indicies]
    if 0 not in distances:
        weights = power / distances
    else:
        distances += 0.000000001
        weights = power / distances
    weights /= weights.sum(axis=0)
    zi = np.dot(weights.T, z_n)
    return zi
