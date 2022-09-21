"""
- script to create a path based on a node set and a set with the start node
- sets need to be defined on assembly level
- open odb in abaqus cae and run script
- to check see Tools > Path > Manager or the tree afterwards
"""


# to be defined by user before
set_nodes = 'edge-path' # set with the edge where the path should be
set_startnode = 'node-path' # set with point of that edge to indicate start of path
pathname = 'myPath' # name of the path that is created by this script

#############################################################################################

from abaqus import *
from abaqusConstants import *
from caeModules import visualization
import numpy as np

vps = session.viewports.values()[0]
odbName = vps.displayedObject.name
odb = session.odbs[odbName]

set_nodes = set_nodes.upper()
set_startnode = set_startnode.upper()

#############################################################################################

instancename = odb.rootAssembly.nodeSets[set_startnode].nodes[0][0].instanceName
start_node = odb.rootAssembly.nodeSets[set_startnode].nodes[0][0]

path_nodes = []
path_nodes.append(start_node.label)

num_nodes = len(odb.rootAssembly.nodeSets[set_nodes].nodes[0])

for i in range(num_nodes-1):
	min_dist = 1e6
	for node in odb.rootAssembly.nodeSets[set_nodes].nodes[0]:
		if node.label not in path_nodes:
			dist = np.linalg.norm(start_node.coordinates - node.coordinates)
			if dist < min_dist:
				min_dist = dist
				min_node = node

	path_nodes.append(min_node.label)
	start_node = min_node
	

print '\nClosed loop = first node of path is also last node'
answer = getInput('Form closed loop? (y/n):')
if answer in ['y', 'Y', 'yes', 'j', 'ja']:
	path_nodes.append(path_nodes[0])


session.Path(name=pathname, type=NODE_LIST, expression=((instancename, (
	tuple(path_nodes))), ))

print '\nPath "'+pathname+'" was created. Check path!'
