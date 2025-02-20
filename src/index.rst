.. toctree::
   :maxdepth: 2

######################
OpenFOAM
######################

**********************
参考资料
**********************

OpenFOAM的网站有两个，分别是 `<https://www.openfoam.com>`_ 和 `<https://openfoam.org>`_ ，推荐使用openfoam.org，www.openfoam.com国内打不开。
在openfoam.org网站的Download菜单中，可以选择Compiling Sources，其中有OpenFOAM详细的编译介绍，一共分为5步。
这里需要注意的是OpenFOAM通过操作系统的包管理器apt安装了一些第三方库，在第1步中有详细介绍需要安装哪些库。
在openfoam.org网站的Resources菜单中，C++ Source Guide是程序介绍，Technical Guides是计算流体力学介绍，
User Guide是使用说明。在User Guide中，在第2节中介绍了3个例子的使用，调用OpenFOAM已有求解器的可执行程序，在第3节中介绍了基于OpenFOAM开发APP的编译和使用。

**********************
编译和安装
**********************

按照如下操作在FENGSim中编译OpenFOAM。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将CFD克隆到FENGSim/toolkit/路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/CFD.git
  
* 在FENGSim/toolkit/CFD/openfoam中有一个install脚本，该脚本是根据网站中Compiling Sources写的，直接运行该脚本可以在Ubuntu24.04下编译OpenFOAM，无需其他操作。 ::
  
    cd FENGSim/toolkit/CFD/openfoam
    ./install

OpenFOAM有两个仓库，分别是OpenFOAM-dev和ThirdParty-dev，dev可以换成版本号，例如OpenFOAM-12和ThirdParty-12。需要将OpenFOAM-dev和ThirdParty-dev保存在同一路径下，
在OpenFOAM-dev目录下运行的编译命令还会编译ThirdParty-dev目录中的第三方库。OpenFOAM-dev目录下有三个子目录，分别为applications、test、tutorials，test和tutorials里有很多测试例子，例子里主要包括前处理文件，
applications里有APP开发的例子，例子里主要包括二次开发的程序。OpenFOAM中使用了wmake编译工具，wmake是用脚本程序开发的，采用wmake又写了脚本程序Allwmake去执行编译，例如在OpenFOAM-dev目录下有Allwmake脚本程序。
编译安装完后，为了运行可执行程序或者调用链接库，需要配置环境变量，运行如下命令。 ::
  
    cd FENGSim/toolkit/CFD/openfoam
    source OpenFOAM/etc/bashrc
    echo $FOAM_INST_DIR

**********************
算例
**********************


在FENGSim/starter/openfoam/platHole目录中是一个固体算例，运行如下命令。 ::
  
    cd FENGSim/starter/openfoam/platHole
    ./Allrun
    foamToVTK

这里一定要注意，需要运行环境变量的配置文件。生成的vtk文件在FENGSim/starter/openfoam/platHole/VTK目录中，可以用paraview打开，如下图。
    
.. image:: fig/openfoam_1.png
   :scale: 50 %
   :alt: alternate text
   :align: center


	   
**********************
前处理文件格式
**********************

继续FENGSim/starter/openfoam/platHole目录中的固体算例，该目录下有三个子目录，分别为0、constant、system，其中0目录中的文件定义了边界条件，constant目录中的文件定义了物理参数，例如弹性模量和泊松比，system目录中的文件定义了网格剖分、求解器、时间步、离散以及解法器。

######################
SU2
######################

**********************
文档
**********************

**********************
编译和安装
**********************

**********************
算例
**********************

**********************
前处理文件格式
**********************

######################
Palace
######################

**********************
文档
**********************

**********************
编译和安装
**********************

**********************
算例
**********************

**********************
前处理文件格式
**********************

