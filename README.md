# Dora ROS Launch Files

Launch files for running Dora using the p2os packages provided by ROS, with a structure intended to match that used by the [STRANDS project](http://github.com/strands-project)

## Installation

To run Dora you need to install this package along with packages to control the robot base (p2os), pan-tilt unit (wu_ptu) and manage the transforms etc. (rocs_robot).

To install the necessary components, create a catkin workspace and use the following .rosinstall file, or use the URLs to install how you wish.

```
- git: {local-name: dora_launch, uri: 'https://github.com/uobirlab/dora_launch.git'}
- git: {local-name: wu_ptu, uri: 'https://github.com/uobirlab/wu_ptu.git'}
- git: {local-name: dora-control, uri: 'https://github.com/uobirlab/dora-control.git'}
```

You also need to install the dependencies of these packages before they build. The simplest way is to use rosdep from the top directory of your catkin workspace, e.g. (or similar)

```bash
rosdep install --from-paths src --ignore-src --rosdistro groovy -y -r
```

Some of the rocs_* packages will say that they need rosaria or libaria. Ignore that for now as we're not using Aria to control the robot. 

## Launch

To bring up the sensors and controllers launch

```bash
roslaunch dora_launch dora_bringup.launch
```

The ports are configured to work by default on Dora. You will need to have write access to `/dev/ttyUSB0`, `/dev/ttyUSB1` and `/dev/ttyACM0` for to talk to the robot. The easiest way to do this appears to be add yourself to the `dialout` group (e.g. `sudo usermod -a -G dialout <username>`). You might need to log out and log in again that the setting will take effect.

## Teleop

To control the robot with the joystick you have two choices: 

1. If you are using the older style Logitech controller (or any ROS-compatible joystick) you can use the p2os teleop package via:
```bash
roslaunch dora_launch dora_teleop.launch js:=<my joystick device, e.g. /dev/input/js1>
```
**Note that this teleop approach continually sends commands to `/cmd_vel` and thus interferes with move_base**

2. If you want STRANDS Project input you need to connect the newer silver controller, then the usual command should run:
```bash
roslaunch scitos_teleop teleop_joystick.launch js:=<my joystick device, e.g. /dev/input/js1>
```
Although not all functionality will be available.

## Navigation

To run Dora with 2D navigation plus 3D obstable avoidance, run 
```bash
roslaunch dora_launch dora_2d_nav.launch map:=<full path to maps .yaml file>
```
If you don't yet have a map you can run gmapping SLAM in the usual way.


