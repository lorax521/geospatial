import numpy as np

def distance_matrix(x, y, xi, yi):
    """ Creates a matrix with the distance from a given point (x1, y1)
    to all other points

    Keyword arguments:
        x: 1d array -- point locations on the x-axis
        y: 1d array -- point locations on the y-axis
        xi: float -- x-axis point location of unknown value
        yi: float -- y-axis point location of unknown value
    
    Return:
        dist_mx: 1d array -- distances from every x,y point to xi,yi
    """
    obs = np.vstack((x, y)).T
    interp = np.vstack((xi, yi)).T

    # Make a distance matrix between pairwise observations
    d0 = np.subtract.outer(obs[:,0], interp[:,0])
    d1 = np.subtract.outer(obs[:,1], interp[:,1])

    dist_mx = np.hypot(d0, d1)
    return dist_mx

def idw(x,y,z,xi,yi):
    """ Inverse Distance Weighting - interpolates an unknown value at a 
    specified point by weighting the values of it's nearest neighbors

    Keyword arguments:
        x: 1d array -- point locations on the x-axis
        y: 1d array -- point locations on the y-axis
        z: 1d array -- point values at each location
        xi: float -- x-axis point location of unknown value
        yi: float -- y-axis point location of unknown value
    
    Return:
        zi: float -- interpolated value at xi, yi
    """
    neighbors = 12
    power = 2
    dist_all = distance_matrix(x,y, xi,yi)
    dist_n = np.asarray([np.sort(dist_all, axis=None)[x] for x in range(neighbors)])
    indicies = [np.where(dist_all == x)[0][0] for x in dist_n]
    z_n = z[indicies]
    if 0 not in dist_n:
        weights = power / dist_n
    else:
        dist_n += 0.000000001
        weights = power / dist_n
    weights /= weights.sum(axis=0)
    zi = np.dot(weights.T, z_n)
    return zi
