# Arm64 ROS2 Setup

## The Fairno_Hardware asumes x86_64 architecure. To set up this repo for Arm64 functionality, following the steps below to adjust your Cmake;

### 0) Choose method:
    There is a hardwares folder in this repo that contains the fairino_hardware folder for x86 and another folder called "second_fairino_hardware". The latter of which should contain the source code for the aarch achitecture. If that does not work with your build, try the manual method by following the steps below

### 1) Install new XmlRPc library:
    sudo apt update
    sudo apt install libxmlrpc-c++8-dev


### 2) Clone the xmlrpc-c repository in the root direcory
    cd ~
    git clone https://github.com/mirror/xmlrpc-c.git
    cd xmlrpc-c/stable

### 3) Configure and build for aarch64:

    ./configure --host=aarch64-linux-gnu
    make
    sudo make install

### 4) Ensure the library is installed in a standard location (e.g., /usr/local/lib) and update the linker cache:

    sudo ldconfig

    
### 5) Fix CMake Configuration
The CMake error suggests a configuration issue. Common causes include:

Missing Dependencies: Ensure all dependencies for LibXmlRpc (e.g., libxml2) are installed:

    sudo apt install libxml2-dev

Incorrect CMake Paths: If LibXmlRpc is installed in a non-standard location, update CMAKE_PREFIX_PATH or CMAKE_LIBRARY_PATH in your colcon build command:

    colcon build --cmake-args -DCMAKE_PREFIX_PATH=/usr/local -DCMAKE_LIBRARY_PATH=/usr/local/lib
