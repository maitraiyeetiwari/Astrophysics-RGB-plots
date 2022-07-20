#ipython --pylab

import aplpy
import matplotlib.pyplot as mpl


#fig = mpl.figure(figsize=(10,10))
f = aplpy.FITSFigure('rcw49-rgb_2d.fits',north=True)

f.show_rgb('rcw49_rgb.png')

f.set_xaxis_coord_type('scalar')

f.set_yaxis_coord_type('scalar')

#f.recenter(156.05,-57.69, width=0.2,height=0.23)

f.recenter(156.05,-57.75, width=0.28,height=0.38)

f.add_label(0.2, 0.95, '[CII]', relative=True, size=20,color='red')
f.add_label(0.5, 0.95, '8 $\mu$m', relative=True, size=20,color='limegreen')
f.add_label(0.8, 0.95, '870 $\mu$m', relative=True, size=20,color='dodgerblue')


#f.show_markers(156.045,-57.76,marker='*',edgecolor='white',facecolor='white',s=100)
f.show_markers(156.01,-57.7,marker='*',edgecolor='magenta',facecolor='magenta',s=100) #O9V star
f.add_label(0.638, 0.63, 'O9V', relative=True, size=12,color='magenta')

f.show_markers(156.0,-57.755,marker='*',edgecolor='magenta',facecolor='magenta',s=200) #Wd2
f.add_label(0.657, 0.48, 'Wd2', relative=True, size=12,color='magenta')

f.show_markers(156.075,-57.805,marker='*',edgecolor='magenta',facecolor='magenta',s=100) #WR20b
f.add_label(0.445, 0.383, 'WR20b', relative=True, size=12,color='magenta')


f.set_xaxis_coord_type('longitude')

f.set_yaxis_coord_type('latitude')

f.axis_labels.set_ytext('Dec. (J2000)')

f.axis_labels.set_xtext('R.A. (J2000)')

# f.show_contour('cii_tdv_2_8.fits',levels=[50],colors='gray')

f.show_regions('nc.reg')
f.add_label(0.6, 0.845, 'northern cloud', relative=True, size=15,color='white')
f.show_regions('ridge.reg')
f.add_label(0.25, 0.48, 'ridge', relative=True, size=15,color='white')
f.show_regions('shell.reg')
f.add_label(0.253, 0.38, 'shell', relative=True, size=15,color='white')
f.show_regions('pillar.reg')
f.add_label(0.58, 0.32, 'pillar', relative=True, size=15,color='white')
f.show_regions('p1.reg')
f.add_label(0.685, 0.565, 'p1', relative=True, size=15,color='white')
f.show_regions('p3.reg')
f.add_label(0.35, 0.55, 'p3', relative=True, size=15,color='white')
f.show_regions('p7.reg')
f.add_label(0.45, 0.7, 'p7', relative=True, size=15,color='white')








f.save('rgb-regs-stars.png',dpi=300)










