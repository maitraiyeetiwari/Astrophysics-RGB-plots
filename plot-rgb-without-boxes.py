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
f.show_markers(156.0,-57.755,marker='*',edgecolor='magenta',facecolor='magenta',s=200) #Wd2
f.add_label(0.657, 0.48, 'Wd2', relative=True, size=12,color='magenta')
f.set_xaxis_coord_type('longitude')

f.set_yaxis_coord_type('latitude')

f.axis_labels.set_ytext('Dec. (J2000)')

f.axis_labels.set_xtext('R.A. (J2000)')

f.add_label(0.25, 0.845, 'northern cloud', relative=True, size=15,color='white')

f.add_label(0.15, 0.48, 'ridge', relative=True, size=15,color='white')

f.add_label(0.15, 0.38, 'shell', relative=True, size=15,color='white')
f.add_label(0.7, 0.32, 'pillar', relative=True, size=15,color='white')


f.save('rcw49-rgb-regs.png',dpi=500)
