.. toctree::
   :maxdepth: 2

######################
FENGSim
######################

**********************
参考资料
**********************


**********************
编译安装
**********************

将FENGSim一次性部署在服务器上，供多个用户使用。采用Docker避免部署对宿主机的影响，在 ``FENGSim/cli`` 路径下有两个脚本，分别为test-docker.sh和test-docker-gui.sh，这两个脚本默认FENGSim保存在路径 ``$HOME/FENGSim`` 中，运行脚本都会建立Ubuntu24.04容器并进入，test-docker-gui.sh建立的容器可以运行图形用户界面。

之后在宿主机上按照如下命令建立Docker组，并添加成员。 ::
  
  sudo groupadd -f docker
  sudo usermod -aG docker user_name

不同用户就都可以使用同一容器了，容器名称为test。 ::

  sudo docker ps -a
  sudo docker start test
  sudo docker exec -it test /bin/bash

FENGSim直接部署在阿里云服务器或者Docker，如果是root账户，在编译和运行求解器时候会产生mpi报错，例如Palace编译中Petsc会产生mpi报错，mpirun命令也会报错，因此要采用非root账户，在Docker容器中也可以采用adduser命令创建新用户，然后用新用户登录容器。

可以在Docker中编译FENGSim前后处理软件，由于Docker中是极简操作系统，有些Qt需要的链接库可能没有，设置环境变量，export QT_DEBUG_PLUGINS=1，根据报错安装相应的链接库，然后可以从Docker打开FENGSim图形用户界面。


求解器可执行程序可以建立软链接到 ``/usr/local/bin`` 目录中，建立软链接时要注意源文件和链接文件路径要写详细，不要用相对路径。

**********************
算例测试
**********************





**********************
前后处理文件格式
**********************








.. include:: ccx.rst









	     
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
编译安装
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
算例测试
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
前后处理文件格式
**********************

继续 ``FENGSim/starter/openfoam/platHole`` 目录中的固体算例，该目录下有三个子目录，分别为0、constant、system，其中0目录中的文件定义了边界条件，constant目录中的文件定义了物理参数，例如弹性模量和泊松比，system目录中的文件定义了网格剖分、求解器、时间步、离散以及解法器。

运行blockMesh可以进行网格剖分，剖分后的网格数据保存在 ``platHole/constant/polyMesh`` 目录中的5个文件，分别为points、faces、owner、neighbour、boundary。和有限元网格有所区别，points是网格所有顶点，faces是网格所有单元面，单元面按照先内部单元面和后边界单元面排序，边界单元面按照几何模型面排序。owner定义了每个单元面归属的单元，如果是内部单元面，除了归属单元，还有相邻单元，相邻单元编号保存在neighbour中，这里需要注意的是neighbour对应了faces中的内部单元面，faces中内部单元面排在边界单元面前面。boundary是所有边界单元面，同一几何模型面上的边界单元面集合是按照faces中单元面编号起始位置以及个数定义。

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




######################
Cantera
######################

**********************
参考资料
**********************

**********************
编译安装
**********************

**********************
算例测试
**********************

.. image:: fig/cantera.png
   :scale: 50 %
   :alt: alternate text
   :align: center
	   
**********************
前后处理文件格式
**********************







.. include:: palace.rst


######################
MBDyn
######################

**********************
参考资料
**********************

网站为 `<https://www.mbdyn.org/>`_ ，在网站Documentation中有Tutorials，还有一个日本小公司的网站上有很多例子 `<https://www.sky-engin.jp/en/>`_ 。

**********************
编译安装
**********************

**********************
算例测试
**********************

在 ``FENGSim/starter/mbdyn`` 目录下有一个自由落体的简单例子，运行如下命令。 ::
  
    cd FENGSim/starter/mbdyn
    ./../../toolkit/DAE/install/mbdyn_install/bin/mbdyn -f free_falling_body_E.mbd
    gnuplot
    plot 'free_falling_body_E.mov' using 3:4

.. image:: fig/mbdyn_1.png
   :scale: 50 %
   :alt: alternate text
   :align: center    


**********************
前后处理文件格式
**********************


######################
ROS2/MoveIt2
######################

**********************
参考资料
**********************

ROS2的参考文献见 `<https://docs.ros.org/>`_ ，我们选择的版本为Jazzy，编译脚本的参考文献见 `<https://docs.ros.org/en/jazzy/>`_ ，在Installation中的Alternatives中的Ubuntu(Source)中有编译安装介绍，
install脚本是按照该介绍写的。MoveIt2的编译脚本的参考文献见 `<https://moveit.ai/install-moveit2/source/>`_ ，install脚本是按照该介绍写的。MoveIt2 Tutorials的编译脚本的参考文献见 `<https://github.com/moveit/moveit2_tutorials>`_ ，在MoveIt Tutorials Source Build中有编译安装介绍。




**********************
编译安装
**********************

按照如下操作在FENGSim中编译ROS2、MoveIt2和MoveIt2_Tutorials。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git

* 将DAE克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/DAE.git

* 在 ``FENGSim/toolkit/DAE/ros2/ros2/`` 中有一个install脚本，运行该脚本安装ROS2。 ::
  
    cd FENGSim/toolkit/DAE/ros2/ros2/
    ./install
    
* 在 ``FENGSim/toolkit/DAE/ros2/moveit2/`` 中有一个install脚本，运行该脚本安装MoveIt2。 ::
  
    cd FENGSim/toolkit/DAE/ros2/moveit2/
    ./install

* 在 ``FENGSim/toolkit/DAE/ros2/moveit2_tutorials/`` 中有一个install脚本，运行该脚本安装MoveIt2_Tutorials。 ::
  
    cd FENGSim/toolkit/DAE/ros2/moveit2_tutorials/
    ./install

ROS2、MoveIt2、MoveIt2_Tutorials要清楚三个环节，第一个是代码的获取，第二个是库依赖关系的配置和安装，第三个是编译和安装。其中代码获取采用了Vcstool去下载仓库，见 `<https://github.com/dirk-thomas/vcstool>`_ 。库依赖关系配置文件在rosdistro中，见 `<https://github.com/ros/rosdistro/tree/master>`_ ，本应该采用 ``rosdep init`` 创建配置文件，但由于 ``rosdep init`` 中会出现下载问题，
可以修改20-default.list和__init__.py中的路径，直接调用rosdistro中的配置文件。ROS2和MoveIt2除了依赖apt中的库，还有ros自己的包管理器中的库。
编译采用工具colcon，见 `<https://colcon.readthedocs.io/en/released/>`_ ，由于编译过程中也存在下载问题，因此如果出现异常结束，需要重复操作。

ROS2、MoveIt2、MoveIt2_Tutorials的源代码都在 ``src`` 目录下，编译安装后会生成  ``build`` ， ``install`` ， ``log`` 三个目录。
安装依赖库的命令为 ``rosdep install`` ，需要注意路径设置，例如： ::

  rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"

中指定了路径为 ``src`` 也就是源代码目录，会从源代码目录中寻找package.xml的依赖配置文件，再例如： ::

  rosdep install -r --from-paths . --ignore-src --rosdistro jazzy -y

中指定了当前路径，是因为在 ``src`` 路径下运行的该命令。编译的命令为 ``colcon build`` ，需要注意在 ``src`` 的上一层路径下执行该命令。例如： ::

  cd FENGSim/toolkit/DAE/ros2/ros2/ros2_jazzy
  colcon build --symlink-install

在 ``FENGSim/toolkit/DAE/ros2/ros2/ros2_jazzy/install`` ， ``FENGSim/toolkit/DAE/ros2/moveit2/ws_moveit2/install`` 和 ``FENGSim/toolkit/DAE/ros2/moveit2_tutorials/install`` 以及 ``/opt/ros/jazzy/`` 目录下有setup.bash文件配置环境变量，在使用ROS2、MoveIt2、MoveIt2_Tutorials之前运行以下命令。 ::

  cd FENGSim/toolkit/DAE/ros2
  source ros2/ros2_jazzy/install/setup.bash
  source moveit2/ws_moveit2/install/setup.bash
  source moveit2_tutorials/install/setup.bash

``/opt/ros/jazzy/`` 是在MoveIt2安装过程中产生的，在MoveIt2编译需要调用通过ros包管理器安装的一些库，因此需要运行以下命令配置环境变量，否则编译过程中会有一些ros链接库找不到。 ::

  source /opt/ros/jazzy/setup.bash
  
ROS2、MoveIt2、MoveIt2_Tutorials的编译安装可以在Docker中进行，运行 ``FENGSim/cli/`` 目录下的脚本程序test-docker-gui.sh，可以创建一个可以
打开图形用户界面的Docker容器，需要注意的是容器、终端或者电脑重启后，再进入容器可能会打不开图形用户界面，需要重复操作下test-docker-gui.sh中的以下几条命令。 ::
  
  sudo xhost +si:localuser:root
  sudo chmod 777 /tmp/.docker.xauth
  XAUTH=/tmp/.docker.xauth




**********************
算例测试
**********************

运行以下命令： ::

  cd FENGSim/toolkit/DAE/ros2
  source ros2/ros2_jazzy/install/setup.bash
  source moveit2/ws_moveit2/install/setup.bash
  source moveit2_tutorials/install/setup.bash
  ros2 launch moveit2_tutorials demo.launch.py

.. image:: fig/ros2moveit2.gif
   :scale: 50 %
   :alt: alternate text
   :align: center    

**********************
前后处理文件格式
**********************
