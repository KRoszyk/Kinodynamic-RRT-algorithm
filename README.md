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
