# iRAP WebEngine Package for ROS 1

The iRAP WebEngine package for ROS 1 enables you to open your web server using Flask in Python, facilitating the running of GUI applications. This package automatically launches `rosbridge_websocket`.

## Installation

**ROS must be installed**

1. This repository requires the installation of the ROSbridge Suite. Details about ROSbridge Suite can be found at [http://wiki.ros.org/rosbridge_suite](http://wiki.ros.org/rosbridge_suite). You can install it directly using the following command in your terminal. For example, if you are using ROS Noetic:

    ```bash
    sudo apt-get install ros-noetic-rosbridge-server
    ```

2. Create your Catkin workspace. If you don't have one, you can follow the instructions in the ROS tutorial [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).

3. Copy this package to your workspace's `src` directory.

4. Don't forget to run `catkin_make`.

5. Replace your build app folder with the contents in `irap_webengine/scripts/build`.

6. Finally, launch the server with `rosbridge_websocket` using the following command:

    ```bash
    roslaunch irap_webengine irap_webengine.launch
    ```

