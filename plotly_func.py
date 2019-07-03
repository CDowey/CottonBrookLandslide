# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:22:36 2019

@author: Colin.Dowey

"""


def raster_for_plotly(raster):
    '''
    A function that uses rasterio to gather the x and y vectors and z-array needed to convert a raster dataset
    to a Plotly surface.
    
    The result is a dictionary that contains the x-vector, y-vector, z-array, and affine matrix
    
    '''
    
    import rasterio as rio
    import numpy as np
    
    # Get affine matrix
    aff = raster.transform
    
    # Build x and y vectors
    x = range(0, raster.width)
    y = range(0, raster.height)

    x_zip = list(zip(x, [0]*len(x)))
    y_zip = list(zip([0]*len(y), y))
    
    # Multiply by the affine matrix to convert to actual coordinates
    x_vals = [(aff*c)[0] for c in x_zip]
    y_vals = [(aff*c)[1] for c in y_zip]
    
    # Build z-array
    z_array = raster.read()

    # Convert all values at raster edges to np nan instead of -999
    z_array[z_array < 0] = np.nan
    
    # Create dict
    out_for_plotly = {
        'x' : x_vals,
        'y' : y_vals,
        'z' : z_array[0],
        'aff' : aff    
    }
    
    return out_for_plotly