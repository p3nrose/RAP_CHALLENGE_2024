# Cheatsheet
From home directory make a symlink: ln -s ~/rap/lawn_mower/ ~/colcon_ws/src/

# RAP 2024 Challenge

RAP-EN 2024 Challenge Project (graded)

You are tasked with writing the software for a robotic lawnmower for solar plants using ROS2.

## Goals

The robot functionality should be as follows:

* on first initialization, the robot should use a depth camera to build a 3D/2D map of the solar plant;
* based on this map, the plant owner should be able to design a navigation plan that the robot will follow to cut the grass in the plant and come back to its starting point;
* while following the navigation plan, the robot should be able to avoid obstacles that were not part of the environment when the map was built;
* *stretch goal*: depending on the nature of the obstacle, (i.e., static versus dynamic) the robot will decide whether to trigger a map update.

## Deliverables (for grading)

**Note**: Your code should use other ROS2 packages without requiring their modification. Copy or include the scripts and launchfiles from other projects if needed. Use package dependency configuration or an install script to include dependency installation.

Required deliverables (in a single git repository, one or more ROS packages at your choice):
* A .world file modeling your solar plant to be used in Gazebo Classic;
* A Turtlebot3 waffle robot model extended with the additional sensors you may need;
* A launchfile for starting the 3D Mapping + saving a 2D map (you can use icclab_summit_xl rtabmap.py.launch as an example);
* A way to specify and send a navigation plan to the robot;
* The logic and launchfiles to start and follow the navigation plan for the robot, including collision avoidance;
* (Optional) The logic to detect if an obstacle is a cat (dynamic obstacle, no remapping needed) or "something else" triggering a map update in the obstacle area.


# Conditions, Hints, Assumptions

Hints and simplifying assumptions:
* You are allowed to use anything you find online, including AI for code generation. You should however be able to explain the code and the functioning of your project;
* You can use any gazebo model / starting world file you find online to create your world. Keep it bounded (e.g., with a fence or a wall) and small for demonstration (e.g., 20-40 sqm);
* You can assume to be using a planar lidar and AMCL for localization; extra points if you are able to just use the camera for localization;
* Some references of (possibly) useful projects are: Nav2, opennav_coverage, rtabmap, yolov8_ros (untested), ORB-SLAM3-ROS2-Docker (untested);
* Some inspiration of what's possible is here: https://sheeprobotics.ai/
