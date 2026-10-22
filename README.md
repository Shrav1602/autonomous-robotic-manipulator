# Autonomous Robotic Manipulator

## Project Overview

This project aims to develop an autonomous robotic manipulator capable of
performing pick-and-place tasks.

The project follows a step-by-step approach, combining programming,
robotics theory, simulation, electronics, and control systems.

## Objectives

- Develop Python programming skills through practical robotics applications.
- Implement forward and inverse kinematics.
- Understand trajectory planning and robot dynamics.
- Implement feedback control.
- Learn C++ and ROS 2.
- Simulate a robotic manipulator.
- Integrate sensors and actuators.
- Develop an autonomous pick-and-place system.

## Technology Stack

- Python
- Git and GitHub
- NumPy
- Matplotlib
- C++
- ROS 2
- Robot simulation tools

Additional tools will be introduced as the project progresses.

## Development Roadmap

1. Python fundamentals and object-oriented programming
2. Robotic manipulator modelling
3. Forward kinematics
4. Inverse kinematics
5. Trajectory planning
6. Robot dynamics and feedback control
7. C++ fundamentals
8. ROS 2 and robot simulation
9. Motion planning and perception
10. Autonomous pick-and-place

## Current Status

- [x] Create GitHub repository
- [ ] Set up project structure
- [ ] Create the initial Python robot model
- [ ] Implement forward kinematics
- [ ] Visualise the robotic manipulator

## Learning Approach

Each milestone will combine theoretical understanding, implementation,
testing, and documentation.

The objective is not just to make the robot work, but to understand the
engineering principles behind its behaviour.

## 2D Geometry and Coordinate Conventions

### Coordinate System

* The robot's base is located at the origin `(0, 0)`.
* The positive x-axis points to the right.
* The positive y-axis points upward.
* All link lengths and coordinates use the same length unit.

### Joint Angles

* Joint angles are provided in degrees.
* Positive angles represent counterclockwise rotation.
* A zero-degree angle points along the positive x-axis.
* Angles are converted to radians internally before applying trigonometric functions.

### Two-Link Forward Kinematics

* `link1_length` and `link2_length` represent the lengths of the two links.
* `angle1_degrees` is measured from the positive x-axis.
* `angle2_degrees` is measured relative to the first link.
* The absolute orientation of the second link is the sum of the two joint angles.

The first joint coordinates are calculated as:

`x1 = L1 * cos(theta1)`

`y1 = L1 * sin(theta1)`

The final endpoint is calculated as:

`x2 = x1 + L2 * cos(theta1 + theta2)`

`y2 = y1 + L2 * sin(theta1 + theta2)`

### Validation

* Single-link endpoint calculations have been tested at 0°, 90°, 180°, and 270°.
* Two-link forward kinematics have been tested with five joint-angle configurations.
* Automated tests use approximate floating-point comparisons to account for numerical precision.
