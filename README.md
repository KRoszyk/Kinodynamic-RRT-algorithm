# Kinodynamic_RRT_algorithm
In this project I applied the RRT algorithm for OpenAI’s Car Racing Game.
The main issue of this problem was to keep the racer on the track with the car moving at high speed.
This problem is often solved by using nueral networks, hovewer I decided to solve it with path planning algorithm called RRT.

# What is RRT?
RRT (Rapidly-exploring random tree) is a path planning algorithm. 
In kinodynamic RRT, compared to regular RRT, the set of controls is sampled instead of the new vertex coordinates.

**The main steps of its operation with an illustration are presented below:**

- Randomize a set of controls in a given movement space.

- If this set gets you closer to your goal - add it to the control graph, if not - don't add it.

- Connect this newly added graph vertex to the nearest vertex.

- Repeat these operations until one of the controls is within the range of the assumed endpoint environment 
![Screenshot](https://github.com/KRoszyk/Kinodynamic_RRT_algorithm/blob/master/images/graph.PNG)

# What's in the code?

The code consists of 3 files:

- **main_code.py** - this file is responsible for selecting the set of controls in relation to the previous actions. Each set consists of 3 values which are: the steering angle, throttle, brake. In this file, methods such as skeletonization, RRT search, and drawing the search tree are also called.

- **rrt.py** - this file contains the RRT class, having the methods described in the previous paragraph. A metric designed to infer whether a given control should be added to the graph has an experimentally selected gamma coefficient aimed at favoring points not only of the right position, but also of the appropriate orientation.

- **skelet.py** - this file contains a method which contains OpenCV morphologic operations responsible for creating the optimal path and determining the destination point for each render. 

# Final results of the project

After applying the RRT algorithm, the car moves correctly on the track. Thanks to the use of the appropriate steering and speed ratios, the car is able to overcome even the most complicated paths.


Below are the screenshots for the car running on the track and the RRT tree created during the program running.

![Screenshot](https://github.com/KRoszyk/Kinodynamic_RRT_algorithm/blob/master/images/racer.jpg)
![Screenshot](https://github.com/KRoszyk/Kinodynamic_RRT_algorithm/blob/master/images/rrt_graph.png)

# Notes for starting the Gym environment
The best option to download the Gym environment is to run the following command in the terminal:

```
pip install gym
```
If you have any problem with the make method from the gym environment, use the following command. It helped me. :)
```
pip install box2d
```
