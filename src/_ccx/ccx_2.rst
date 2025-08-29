**********************
编译安装
**********************

按照如下操作在FENGSim中编译CalculiX和CalculiX GraphiX。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将MultiX克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/MultiX.git
  
* 在 ``FENGSim/toolkit/MultiX/extern/Calculix`` 中有一个install脚本，直接运行该脚本可以在Ubuntu24.04下编译CalculiX和CalculiX GraphiX，无需其他操作。 ::
  
    cd FENGSim/toolkit/MultiX/extern/Calculix
    ./install
    
