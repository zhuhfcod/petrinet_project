# Documentation

## Introduction
This project uses WebGME to complete the development of Design Studio based on mongoDB and Docker. The main goal of the project is to implement Petri Net in Design Studio. Petri Net is a modeling language describing distributed systems, mainly composed of place and transition. 

Petri Net can describe asynchronous and concurrent computer system models, and can also complete some software design, workflow management and parallel programming.

## How to install design studio
You can use docker to implement our project. The main step to install design studio:
1. Clone the repo into your computer
2. Edit the 'env.' file so that the BASE_DIR variable points to the main repository directory
3. Use docker to load design studio (docker-compose up -d)
4. connect to your server

## How to stall modeling once the studio is installed
1. Rebuild the complete solution
1) *docker-compose build*
2) *docker-compose up -d* to restart the server
2. Debug using the logs *docker-compose logs webgme*
3. Stop the server use *docker-compose stop*
4. Enter the WebGME container *docker-compose exec webgme bash*
5. To clean the host machine of unused images *docker system prune -f*
6. Adding new npm dependency *npm i -s yourNewPackageName*
7. Adding new interpreter/plugin to your DS 
Python: *npm run webgme new plugin -- --language Python MyPluginName*
JS: *npm run webgme new plugin MyPluginName*
8. Adding new visualizer to your DS *npm run webgme new viz MyVisualizerName*
9. Adding new seed to your DS *npm run webgme new seed MyProjectName -- --seed-name MySeedName*

## Feature provided in design studio
### Definition and Decoration
The circle represent places, the rectangle represent transition, the arcs composed by place-transition(P2S) and transition-place(S2P). Besides, the folder stores examples.

### Classications and ReachCheck (plugin)
Classications: We design a plugin to recognize the features of a petri net. (Free-choice petri net, State machine, Marked graph and Workflow net)
ReachCheck: Check whether each point in the graph can be reached
If you would like to use plugin, please use the play button on the first toolbar button should be available

### Examples
In our project, we create four different examples. In fact, they have different features and they belongs to different types.

### Visualization
Click SimSM to enter the visual interface, and control the entire process with buttons.

### Design Studio
We create a github repository to contain your design studio code. Then, you need to build a project seed containing the Petri Net metamodel (src/seeds/petrinet)



