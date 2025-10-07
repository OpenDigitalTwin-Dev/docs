**********************
编译安装
**********************

按照如下操作在FENGSim中编译安装Geant4。

* 首先克隆FENGSim。

.. code-block:: bash
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将PS克隆到 ``FENGSim/toolkit`` 路径下。

.. code-block:: bash
  
    git submodule init
    git submodule update toolkit/PS
    
* 运行以下命令，在Ubuntu24.04下编译Geant4。 

.. code-block:: bash
		
    cd FENGSim/toolkit/PS/geant4
    ./install   
