#
# Draws the golden ratio rectangle
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

from numpy import *
import matplotlib 
from matplotlib import pyplot as plt
matplotlib.rcParams['toolbar'] = 'None'
plt.rcParams['figure.facecolor'] = 'moccasin'


# =========================================================================

def goldRect():

  """ plots the golden rectangle  """
    
  phi = (1 + sqrt(5.0)) / 2
  x = [0,phi,phi,0,0]
  y = [0,0,1,1,0]
  u = [1,1]
  v = [0,1]

  plt.axis('equal')
  plt.axis('off')
  plt.text(phi/2,1.1,'$\phi$') 
  plt.text((1+phi)/2,-0.1,'$\phi - 1$') 
  plt.text(-0.1, 0.5,'1')
  plt.text( 0.5,-0.1,'1')
  plt.plot(x,y,'-b')
  plt.plot(u,v,'--b')
  plt.show()

# ============================= mainProgram ===============================

goldRect()
help(goldRect)

# =========================================================================
