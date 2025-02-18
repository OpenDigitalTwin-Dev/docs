.. toctree::
   :maxdepth: 2

######################
OpenFOAM
######################

**********************
参考资料
**********************

OpenFOAM的网站有两个，分别是www.openfoam.com和openfoam.org，推荐使用openfoam.org，www.openfoam.com国内打不开。
在openfoam.org网站的Download菜单中，可以选择Compiling Sources，其中有OpenFOAM详细的编译介绍，一共分为5步。
这里需要注意的是OpenFOAM通过操作系统的包管理器apt安装第三方库，在第1步中有详细介绍需要安装哪些库。
在openfoam.org网站的Resources菜单中，C++ Source Guide是程序介绍，Technical Guides是计算流体力学介绍，
User Guide是使用说明。在User Guide中，第2节介绍了3个例子的使用，直接调用OpenFOAM已有的求解器可执行程序，第3节介绍了基于OpenFOAM开发的APPs是如何编译和使用的。

**********************
编译
**********************

基于FENGSim编译OpenFOAM：

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将CFD克隆到FENGSim/toolkit/路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/CFD.git
  
* 在FENGSim/toolkit/CFD/openfoam中有一个install脚本，该脚本是根据Compiling Sources写的，直接运行该脚本可以在Ubuntu24.04下编译OpenFOAM，无需其他操作。 ::
  
    cd FENGSim/toolkit/CFD/openfoam
    ./install

OpenFOAM有两个仓库，分别是OpenFOAM-dev和ThirdParty-dev，dev可以换成版本号，例如OpenFOAM-12和ThirdParty-12。需要将OpenFOAM-dev和ThirdParty-dev保存在同一路径下，
在OpenFOAM-dev目录下运行编译命令的同时会编译ThirdParty-dev中的第三方库。


**********************
算例
**********************

**********************
前处理文件格式
**********************


######################
SU2
######################

**********************
文档
**********************

**********************
编译
**********************

**********************
算例
**********************

**********************
前处理文件格式
**********************

