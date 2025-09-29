**********************
编译安装
**********************

按照如下操作在FENGSim中编译安装OpenPhase。

* 首先克隆FENGSim。

.. code-block:: bash
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将Particles克隆到 ``FENGSim/toolkit`` 路径下。

.. code-block:: bash
  
    git submodule init
    git submodule update toolkit/Particles
    
* 运行以下命令，在Ubuntu24.04下编译OpenPhase。 

.. code-block:: bash
		
    cd FENGSim/toolkit/Particles/openphase
    ./install   
