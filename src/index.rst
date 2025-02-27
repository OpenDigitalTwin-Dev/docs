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
  
* 再将CFD克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/CFD.git
  
* 在 ``FENGSim/toolkit/CFD/openfoam`` 中有一个install脚本，该脚本是根据网站中Compiling Sources写的，直接运行该脚本可以在Ubuntu24.04下编译OpenFOAM，无需其他操作。 ::
  
    cd FENGSim/toolkit/CFD/openfoam
    ./install

OpenFOAM有两个仓库，分别是OpenFOAM-dev和ThirdParty-dev，dev可以换成版本号，例如OpenFOAM-12和ThirdParty-12。需要将OpenFOAM-dev和ThirdParty-dev保存在同一路径下，
在OpenFOAM-dev目录下运行的编译命令还会编译ThirdParty-dev目录中的第三方库。OpenFOAM-dev目录下有三个子目录，分别为applications、test、tutorials，test和tutorials里有很多测试例子，例子里主要包括前处理文件，
applications里有APP开发的例子，例子里主要包括二次开发的程序。OpenFOAM中使用了wmake编译工具，wmake是用脚本程序开发的，采用wmake又写了脚本程序Allwmake去执行编译，例如在OpenFOAM-dev目录下有Allwmake脚本程序。
编译安装完后，为了运行可执行程序或者调用链接库，需要配置环境变量，运行如下命令。 ::
  
    cd FENGSim/toolkit/CFD/openfoam
    source OpenFOAM/etc/bashrc
    echo $FOAM_INST_DIR

如果要编译APP，在 ``FENGSim/starter/openfoam/mkdir`` 中有一个例子，运行如下命令，会发现在当前目录下编译生成了可执行程序Test-mkdir，运行可执行程序，在当前目录下创建了一个test目录。 ::
  
    cd FENGSim/starter/openfoam/mkdir
    wmake
    ./Test-mkdir

**********************
算例
**********************

测试OpenFoam中的求解器，在 ``FENGSim/toolkit/CFD/openfoam/OpenFOAM-dev/applications/`` 路径下有两个目录，分别为modules和solvers。其中modules里是各个求解器模块，
见User Guide中第3.5节，求解器模块会编译成链接库，例如 ``modules/fluid`` 模块编译后，得到 ``FENGSim/toolkit/CFD/openfoam/OpenFOAM-dev/platforms/linux64GccDPInt32Opt/lib/libfluid.so`` 。
solvers里是求解器，通过solvers调用modules里的模块，见User Guide中第3.6节，求解器会编译成可执行程序，例如 ``solvers/foamRun`` 编译后，得到 ``FENGSim/toolkit/CFD/openfoam/OpenFOAM-dev/platforms/linux64GccDPInt32Opt/bin/foamRun`` 。

在 ``FENGSim/starter/openfoam/platHole`` 目录中是一个固体算例，运行如下命令。 ::
  
    cd FENGSim/starter/openfoam/platHole
    ./Allrun
    foamToVTK

这里一定要注意，需要运行环境变量的配置文件。生成的vtk文件在 ``FENGSim/starter/openfoam/platHole/VTK`` 目录中，可以用paraview打开，如下图。
    
.. image:: fig/openfoam_1.png
   :scale: 50 %
   :alt: alternate text
   :align: center


	   
**********************
前处理文件格式
**********************

继续 ``FENGSim/starter/openfoam/platHole`` 目录中的固体算例，该目录下有三个子目录，分别为0、constant、system，其中0目录中的文件定义了边界条件，constant目录中的文件定义了物理参数，例如弹性模量和泊松比，system目录中的文件定义了网格剖分、求解器、时间步、离散以及解法器。

运行blockMesh可以进行网格剖分，剖分后的网格数据保存在 ``platHole/constant/polyMesh`` 目录中的5个文件，分别为points、faces、owner、neighbour、boundary。和有限元网格有所区别，points是网格所有顶点，faces是网格所有单元面，单元面按照先内部单元面和后边界单元面排序，边界单元面按照几何模型面排序。owner定义了每个单元面归属的单元，如果是内部单元面，除了归属单元，还有相邻单元，相邻单元编号保存在neighbour中，这里需要注意的是neighbour对应了faces中的内部单元面，faces中内部单元面排在边界单元面前面。boundary是所有边界单元面，同一几何模型面上的边界单元面集合是按照faces中单元面编号起始位置以及个数定义。

######################
SU2
######################

**********************
文档
**********************

SU2网站为 `<https://su2code.github.io/docs_v7/home/>`_ 。在网站Docs菜单中的Build From Source里介绍了编译操作，在Quick Start中给出了一个示范例子。在网站Docs菜单中的Users Guide中的Mesh File中介绍了网格格式。

**********************
编译和安装
**********************

按照如下操作在FENGSim中编译SU2，如果已经克隆了FENGSim和CFD，请忽略前两步。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将CFD克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/CFD.git
  
* 在 ``FENGSim/toolkit/CFD/su2`` 中有一个install脚本，该脚本是根据网站中Build From Source写的，直接运行该脚本可以在Ubuntu24.04下编译SU2，无需其他操作。 ::
  
    cd FENGSim/toolkit/CFD/su2
    ./install

编译后，SU2安装在 ``FENGSim/toolkit/CFD/install/su2_install`` 路径下。


**********************
算例
**********************

在 ``FENGSim/starter/su2/quickstart`` 目录中保存了网站Docs菜单中Quick Start的例子，运行如下命令。 ::
  
    cd FENGSim/starter/su2/quickstart
    mpirun -np 4 ./../../../toolkit/CFD/install/su2_install/bin/SU2_CFD inv_NACA0012.cfg

这里需要注意在Ubuntu24.04下必须按照并行运行，否则报错，但是Ubuntu20.04没有问题。
Ubuntu24.04下用apt安装的paraview打开flow.vtu报错，要用老一点版本的paraview，例如ParaView-5.11.2-MPI-Linux-Python3.9-x86_64。

.. image:: fig/su2_1.png
   :scale: 50 %
   :alt: alternate text
   :align: center

SU2给了很多例子，在 ``FENGSim/toolkit/CFD/su2/TestCases`` 目录中，网格文件比较大，保存在另外一个仓库中 `<https://github.com/su2code/TestCases.git>`_ 。在网站Tutorials菜单中有这些例子的详细介绍。
	   
**********************
前处理文件格式
**********************
SU2网格格式非常简单，首先给出体单元定义和编号，其次给出顶点坐标和编号，最后给出边界面标识，每个边界面包括的边界面单元和编号。前处理只有两个文件，一个网格文件，一个求解器配置文件，
例如 ``FENGSim/starter/su2/quickstart`` 目录中的 ``inv_NACA0012.cfg`` 和 ``mesh_NACA0012_inv.su2`` ，其中 ``mesh_NACA0012_inv.su2`` 是网格文件。


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

