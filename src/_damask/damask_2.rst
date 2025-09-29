**********************
编译安装
**********************

按照如下操作在FENGSim中编译安装DAMASK。

* 首先克隆FENGSim。

.. code-block:: bash
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将NLA克隆到 ``FENGSim/toolkit`` 路径下。

.. code-block:: bash

   cd FENGSim
   git submodule init
   git submodule update toolkit/NLA

* 再将MultiX克隆到 ``FENGSim/toolkit`` 路径下。

.. code-block:: bash

   cd FENGSim/toolkit
   git clone https://github.com/OpenDigitalTwin-Dev/MultiX.git
    
* 运行以下命令，在Ubuntu24.04下编译DAMASK。 

.. code-block:: bash
		
    cd FENGSim/toolkit/MultiX/extern/DAMASK
    ./install.sh
