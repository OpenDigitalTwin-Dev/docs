######################
SU2
######################

**********************
参考资料
**********************

SU2网站为 `<https://su2code.github.io/docs_v7/home/>`_ 。在网站Docs菜单中的Build From Source里介绍了编译操作，在Quick Start中给出了一个示范例子。在网站Docs菜单中的Users Guide中的Mesh File中介绍了网格格式。

**********************
编译安装
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
算例测试
**********************

在 ``FENGSim/starter/su2/quickstart`` 目录中保存了网站Docs菜单中Quick Start的例子，运行如下命令。 ::
  
    cd FENGSim/starter/su2/quickstart
    mpirun -np 4 ./../../../toolkit/CFD/install/su2_install/bin/SU2_CFD inv_NACA0012.cfg

这里需要注意在Ubuntu24.04下必须按照并行运行，否则报错，但是Ubuntu22.04没有问题。
Ubuntu24.04下用apt安装的paraview打开 ``flow.vtu`` 报错，要用老一点版本的paraview，例如ParaView-5.11.2-MPI-Linux-Python3.9-x86_64。

.. image:: fig/su2_1.png
   :scale: 50 %
   :alt: alternate text
   :align: center

SU2给了很多例子，在 ``FENGSim/toolkit/CFD/su2/TestCases`` 目录中，网格文件比较大，保存在另外一个仓库中 `<https://github.com/su2code/TestCases.git>`_ 。在网站Tutorials菜单中有这些例子的详细介绍。
	   
**********************
前后处理文件格式
**********************
SU2网格格式非常简单，首先给出体单元定义和编号，其次给出顶点坐标和编号，最后给出边界面标识，每个边界面包括的边界面单元和编号。前处理只有两个文件，一个网格文件，一个求解器配置文件，
例如 ``FENGSim/starter/su2/quickstart`` 目录中的inv_NACA0012.cfg和mesh_NACA0012_inv.su2，其中mesh_NACA0012_inv.su2是网格文件。

可以用Gmsh生成.su2的网格文件，并用Gmsh标识边界。在 ``FENGSim/starter/su2/quickstart`` 目录中的test.geo是Gmsh建模的脚本文件，可以用Gmsh导入，其中包括了导入airfoil的cad模型步骤，边界标识步骤，标识成airfoil和farfield两部分。再进行网格剖分，导出.msh和.su2格式文件，如 ``FENGSim/starter/su2/quickstart`` 目录中的test.msh和test.su2。
