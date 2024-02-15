# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:58:42 2023

@author: DECLINE
"""

import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

def set_axes_radius(ax, origin, radius):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])
c = ['r', 'c', 'g', 'm', 'w', 'y', 'orange']     
#          00000001111111122222222223333333333334444444444444455555555666666666666667777777777778888888888888888999999999999999991010101010101010
#           width, lenght, lt height, rt height, height btw t, height, spire height, spire base, spire location, transept length, transept width
amiens =   [48.78, 145,    68.2, 61.7, 59,   56,   112,  4, 74,  70,    29.3]
beauvais = [58,    72.5,   67.2, 67.2, 67.2, 67.2, 67.2, 0, 10,  58,    18]
chartres = [48,    130.2,  115,  105,  46,   51,   51,   0, 100, 63.4,  31]
laon =     [30.65, 110.5,  56,   56,   34,   30,   48,   6, 80,  56,    22]
metz =     [33,    136,    69,   93,   58,   58,   58,   0, 91,  46.8,    16.34]
orleans =  [53,    143.85, 88,   88,   52,   57,   114,  4, 100, 66.74, 18]
paris =    [48,    127,    69,   69,   45,   43,   96,   4, 67,  48,    14] 
reims =    [48.8,  149.17, 81.5, 81.5, 53,   59,   87,   3, 140, 61,    30.7]
rouen =    [61.6,  144,    82,   75,   36,   36,   151,  5, 110, 57,    24.6]
senlis =   [24,    76,     78,   45,   26.5, 30,   30,   0, 40,  34,    13]
sens =     [48.5,  122,    38,   66,   26.5, 38,   38,   0, 0,   34,    23]
soissons = [38,    116,    38,   66,   38,   38,   38,   0, 85,  56,    12] # transept 56??38??

#cath = [amiens, beauvais, chartres, laon, orleans, paris
#reims, rouen, senlis, sens, soissons]

cath = [paris, amiens, senlis]

def set_axes_equal(ax: plt.Axes):
#Set 3D plot axes to equal scale.
    mx = 0
    my = 0
    mz = []
    for j in range(len(cath)):
        if cath[j][0]+cath[j][0]/10>mx:
            mx = cath[j][0]+cath[j][0]/10
        if cath[j][1]+cath[j][1]/10>my:
            my = cath[j][1]+cath[j][1]/10
        mz.append(max(cath[j][2], cath[j][3], cath[j][6]))
    
    ax.set_xlim([0, mx])
    ax.set_ylim([0, my])
    ax.set_zlim([0, max(mz)])
    limits = np.array([ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    set_axes_radius(ax, origin, radius)

fig = plt.figure(dpi=300)
ax = fig.add_subplot(111, projection='3d')

for i in range(len(cath)):
    mx = 0
    my = 0
    mz = []
    for j in range(len(cath)):
        if cath[j][0]+cath[j][0]/10>mx:
            mx = cath[j][0]+cath[j][0]/10
        if cath[j][1]+cath[j][1]/10>my:
            my = cath[j][1]+cath[j][1]/10
        mz.append(max(cath[j][2], cath[j][3], cath[j][6]))
    
    ax.set_xlim([0, mx])
    ax.set_ylim([0, my])
    ax.set_zlim([0, max(mz)])


    faces = []
    for j in range(21):
        faces.append(np.zeros([4,3]))
    
    # Bottom face
    faces[0][:,0] = [0,0,cath[i][0],cath[i][0]]
    faces[0][:,1] = [0,cath[i][1],cath[i][1],0]
    faces[0][:,2] = [0,0,0,0]
    
    # Top face minus facade
    faces[1][:,0] = [0,0,cath[i][0],cath[i][0]]
    faces[1][:,1] = [cath[i][0]/3,cath[i][1],cath[i][1],cath[i][0]/3]
    faces[1][:,2] = [cath[i][5],cath[i][5],cath[i][5],cath[i][5]]
    
    # Top face between towers
    faces[2][:,0] = [cath[i][0]/3,cath[i][0]/3,2*cath[i][0]/3,2*cath[i][0]/3]
    faces[2][:,1] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[2][:,2] = [cath[i][4],cath[i][4],cath[i][4],cath[i][4]]
    
    # Left tower top face
    faces[3][:,0] = [0,0,cath[i][0]/3,cath[i][0]/3]
    faces[3][:,1] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[3][:,2] = [cath[i][2],cath[i][2],cath[i][2],cath[i][2]]
    
    # Right tower top face
    faces[5][:,0] = [2*cath[i][0]/3,2*cath[i][0]/3,cath[i][0],cath[i][0]]
    faces[5][:,1] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[5][:,2] = [cath[i][3],cath[i][3],cath[i][3],cath[i][3]]
    
    # Left tower front face
    faces[4][:,0] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[4][:,1] = [0,0,0,0]
    faces[4][:,2] = [0,0,cath[i][2],cath[i][2]]
    
    # Right tower front face
    faces[6][:,0] = [2*cath[i][0]/3,cath[i][0],cath[i][0],2*cath[i][0]/3]
    faces[6][:,1] = [0,0,0,0]
    faces[6][:,2] = [0,0,cath[i][3],cath[i][3]]
    
    # Front face between towers
    faces[7][:,0] = [cath[i][0]/3,2*cath[i][0]/3,2*cath[i][0]/3,cath[i][0]/3]
    faces[7][:,1] = [0,0,0,0]
    faces[7][:,2] = [0,0,cath[i][4],cath[i][4]]
    
    # Left tower inner face
    faces[8][:,0] = [cath[i][0]/3,cath[i][0]/3,cath[i][0]/3,cath[i][0]/3]
    faces[8][:,1] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[8][:,2] = [cath[i][4],cath[i][4],cath[i][2],cath[i][2]]
    
    # Right tower inner face
    faces[9][:,0] = [2*cath[i][0]/3,2*cath[i][0]/3,2*cath[i][0]/3,2*cath[i][0]/3]
    faces[9][:,1] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[9][:,2] = [cath[i][4],cath[i][4],cath[i][3],cath[i][3]]
    
    # Left tower outer face
    faces[10][:,0] = [0,0,0,0]
    faces[10][:,1] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[10][:,2] = [0,0,cath[i][2],cath[i][2]]
    
    # Right tower outer face
    faces[11][:,0] = [cath[i][0],cath[i][0],cath[i][0],cath[i][0]]
    faces[11][:,1] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[11][:,2] = [0,0,cath[i][3],cath[i][3]]
    
    # Left tower back face
    faces[12][:,0] = [0,cath[i][0]/3,cath[i][0]/3,0]
    faces[12][:,1] = [cath[i][0]/3,cath[i][0]/3,cath[i][0]/3,cath[i][0]/3]
    faces[12][:,2] = [cath[i][5],cath[i][5],cath[i][2],cath[i][2]]
    
    # Right tower back face
    faces[13][:,0] = [2*cath[i][0]/3,cath[i][0],cath[i][0],2*cath[i][0]/3]
    faces[13][:,1] = [cath[i][0]/3,cath[i][0]/3,cath[i][0]/3,cath[i][0]/3]
    faces[13][:,2] = [cath[i][5],cath[i][5],cath[i][3],cath[i][3]]
    
    # Right face minus tower
    faces[14][:,0] = [cath[i][0],cath[i][0],cath[i][0],cath[i][0]]
    faces[14][:,1] = [cath[i][0]/3,cath[i][1],cath[i][1],cath[i][0]/3]
    faces[14][:,2] = [0,0,cath[i][5],cath[i][5]]
    
    # Left face minus tower
    faces[15][:,0] = [0,0,0,0]
    faces[15][:,1] = [cath[i][0]/3,cath[i][1],cath[i][1],cath[i][0]/3]
    faces[15][:,2] = [0,0,cath[i][5],cath[i][5]]

    # Back face
    faces[16][:,0] = [0,cath[i][0],cath[i][0],0]
    faces[16][:,1] = [cath[i][1],cath[i][1],cath[i][1],cath[i][1]]
    faces[16][:,2] = [0,0,cath[i][5],cath[i][5]]

    # Spire front face
    faces[17][:,0] = [cath[i][0]/2-cath[i][7],cath[i][0]/2+cath[i][7],cath[i][0]/2,cath[i][0]/2]
    faces[17][:,1] = [cath[i][8]-cath[i][7],cath[i][8]-cath[i][7],cath[i][8],cath[i][8]]
    faces[17][:,2] = [cath[i][5],cath[i][5],cath[i][6],cath[i][6]]
    
    # Spire back face
    faces[18][:,0] = [cath[i][0]/2-cath[i][7],cath[i][0]/2+cath[i][7],cath[i][0]/2,cath[i][0]/2]
    faces[18][:,1] = [cath[i][8]+cath[i][7],cath[i][8]+cath[i][7],cath[i][8],cath[i][8]]
    faces[18][:,2] = [cath[i][5],cath[i][5],cath[i][6],cath[i][6]]
    
    # Spire left face
    faces[19][:,0] = [cath[i][0]/2-cath[i][7],cath[i][0]/2-cath[i][7],cath[i][0]/2,cath[i][0]/2]
    faces[19][:,1] = [cath[i][8]-cath[i][7],cath[i][8]+cath[i][7],cath[i][8],cath[i][8]]
    faces[19][:,2] = [cath[i][5],cath[i][5],cath[i][6],cath[i][6]]
    
    # Spire right face
    faces[20][:,0] = [cath[i][0]/2+cath[i][7],cath[i][0]/2+cath[i][7],cath[i][0]/2,cath[i][0]/2]
    faces[20][:,1] = [cath[i][8]-cath[i][7],cath[i][8]+cath[i][7],cath[i][8],cath[i][8]]
    faces[20][:,2] = [cath[i][5],cath[i][5],cath[i][6],cath[i][6]]
    
    # Transept left face
    faces[19][:,0] = [cath[i][0]/2-cath[i][7],cath[i][0]/2-cath[i][7],cath[i][0]/2,cath[i][0]/2]
    faces[19][:,1] = [cath[i][8]-cath[i][7],cath[i][8]+cath[i][7],cath[i][8],cath[i][8]]
    faces[19][:,2] = [cath[i][5],cath[i][5],cath[i][6],cath[i][6]]
    
    # Transept right face
    faces[20][:,0] = [cath[i][0]/2+cath[i][7],cath[i][0]/2+cath[i][7],cath[i][0]/2,cath[i][0]/2]
    faces[20][:,1] = [cath[i][8]-cath[i][7],cath[i][8]+cath[i][7],cath[i][8],cath[i][8]]
    faces[20][:,2] = [cath[i][5],cath[i][5],cath[i][6],cath[i][6]]

    ax.add_collection3d(Poly3DCollection(faces, facecolors=c[i], linewidths=1, edgecolors='k', alpha=.25))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    set_axes_equal(ax)
    ax.set_box_aspect([1, 1, 1])
    #ax.legend()
plt.show()