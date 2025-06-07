**********************
编译安装
**********************

按照如下操作在FENGSim中编译安装Maxima。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将DAE克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    git submodule init
    git submodule update toolkit/DAE
    
* 运行以下命令，在Ubuntu24.04下编译Maxima。 ::
  
    cd FENGSim/toolkit/DAE/maxima
    ./install   
