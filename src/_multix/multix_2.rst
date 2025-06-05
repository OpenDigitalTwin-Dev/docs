**********************
编译安装
**********************

按照如下操作在FENGSim中编译安装MultiX。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将MultiX克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/MultiX.git
  
* 运行以下命令，在Ubuntu24.04下编译MultiX。 ::
  
    cd FENGSim/toolkit/MultiX/extern/ALE
    ./install.sh
    cd ../../
    mkdir build
    cd build
    cmake ..
    make -j4    
