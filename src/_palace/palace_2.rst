**********************
编译安装
**********************

按照如下操作在FENGSim中编译Palace。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git

* 将MultiX克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/MultiX.git

* 将NLA克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/NLA.git
  
* 将CEM克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/CEM.git

* 在 ``FENGSim/toolkit/MultiX/extern/ALE/`` 中有一个install脚本，运行该脚本。 ::
  
    cd FENGSim/toolkit/MultiX/extern/ALE/
    ./install.sh
    
* 在 ``FENGSim/toolkit/CEM/palace`` 中有一个install脚本，直接运行该脚本可以在Ubuntu24.04下编译Palace，无需其他操作。 ::
  
    cd FENGSim/toolkit/CEM/palace
    ./install

编译后，Palace安装在 ``FENGSim/toolkit/CEM/install/palace_install`` 路径下。

这里需要注意的是， ``FENGSim/toolkit/CEM/palace/palace/models/postoperator.cpp`` 编译有问题。需要将以下函数名中的Coeff和VCoeff去掉。 ::

  RegisterVCoeffField
  DeregisterVCoeffField
  RegisterCoeffField
  DeregisterCoeffField
  CoeffFieldMapType
  VCoeffFieldMapType
  GetCoeffFieldMap
  GetVCoeffFieldMap

并将以下函数调用注销掉。 ::

  paraview_bdr.SetBoundaryOutput(true);
  paraview_bdr.RegisterField(*)
  paraview.RegisterField("U_e", U_e.get());
  paraview.RegisterField("U_m", U_m.get());
  paraview.RegisterField("S", S.get());

如果用阿里云服务器root账户编译Palace，Petsc编译中的mpi并行会报错，如果是用docker中root账户，Palace并行计算也会报错，因此采用非root账户。

  
