#ipython -pylab

import aplpy

aplpy.make_rgb_cube(['rcw49-cii-tpeakv-pol.fits', 'glimpse_8micron1.fits',
                     'atlasgal.fits'], 'rcw49-rgb.fits')

#rcw-rgb_2d is also generated



aplpy.make_rgb_image('rcw49-rgb.fits','rcw49_rgb.png')

