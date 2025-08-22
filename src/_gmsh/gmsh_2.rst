**********************
编译安装
**********************

按照如下操作在FENGSim中编译安装Gmsh。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
    
* 在 ``FENGSim/toolkit/Geometry/gmsh_4_8_4`` 路径下有一个install.sh脚本，直接运行该脚本可以在Ubuntu24.04下编译安装Gmsh，安装路径为 ``FENGSim/toolkit/Geometry/install/gmsh_install`` ，无需其他操作。 ::
  
    cd FENGSim/toolkit/Geometry/gmsh_4_8_4
    ./install.sh
