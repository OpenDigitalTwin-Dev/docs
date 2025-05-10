######################
Karamelo
######################

**********************
参考资料
**********************

Karamelo的网址为 `<https://github.com/adevaucorbeil/karamelo>`_ ，有两篇文章非常详细介绍了MPM方法和软件开发，分别为：

* A. de Vaucorbeil, V. P. Nguyen, and C. Nguyen-Thanh, “Karamelo: an open source parallel c++ package for the material point method,” Computational Particle Mechanics, oct 2020.
* `<https://www.researchgate.net/publication/343096803_Material_point_method_after_25_years_theory_implementation_and_applications>`_

Karamelo的程序文档为 `<https://adevaucorbeil.github.io/karamelo/html/index.html>`_　。

**********************
编译安装
**********************

在Karamelo的程序文档 `<https://adevaucorbeil.github.io/karamelo/html/index.html>`_　中的Getting started中有Karamelo编译安装的详细介绍，在 ``FENGSim/toolkit/NSM/extern/Karamelo`` 路径下的install安装脚本就是
根据Getting started写的。Karamelo还有额外的第三方依赖库matplotlib-cpp和gzstream，保存在 ``FENGSim/toolkit/NSM/extern/Karamelo/third-party`` 路径下。

按照如下操作在FENGSim中编译Karamelo。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将NSM克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/NSM.git
  
* 在 ``FENGSim/toolkit/NSM/extern/Karamelo`` 中有一个install脚本，直接运行该脚本可以在Ubuntu24.04下编译Karamelo，无需其他操作。 ::
  
    cd FENGSim/toolkit/NSM/extern/Karamelo
    ./install

还有一个uninstall脚本可以删除。


**********************
算例测试
**********************

在 ``FENGSim/starter/karamelo/ex_1`` 路径下保存了算例two-disks.mpm，按照如下命令操作执行。 ::

  cd FENGSim/starter/karamelo/ex_1
  ./../../../toolkit/NSM/extern/Karamelo/build/karamelo -i two-disks.mpm

在 ``FENGSim/starter/karamelo/ex_1`` 路径下会产生dump_p.*.LAMMPS系列结果文件。
OVITO是一个专业的粒子仿真可视化软件，保存在 ``FENGSim/toolkit/NSM/extern/Karamelo/ovito-basic-3.10.6-x86_64/bin/`` 路径下，按照如下命令操作执行，查看结果文件。 ::

  cd FENGSim/starter/karamelo/ex_1
  ./../../../toolkit/NSM/extern/Karamelo/ovito-basic-3.10.6-x86_64/bin/ovito &

用OVITO打开dump_p.*.LAMMPS的文件，可以查看结果动画。

.. image:: fig/karamelo.gif
   :scale: 50 %
   :alt: alternate text
   :align: center

如果采用了并行计算，每个进程会单独生成结果文件，有一个Python脚本可以将所有进程文件合并起来，OVITO其实也具备这个功能，但是需要付费的专业版本。按照如下命令执行并行操作。 ::

  cd FENGSim/starter/karamelo/ex_1
  mpirun -np 2 ./../../../toolkit/NSM/extern/Karamelo/build/karamelo -i two-disks.mpm

由于采用了２个进程并行，在 ``FENGSim/starter/karamelo/ex_1`` 路径下会产生dump_g.proc-0.*.LAMMPS和dump_g.proc-1.*.LAMMPS两个系列结果文件，按照如下命令执行合并操作。 ::

  cd FENGSim/starter/karamelo/ex_1
  python3 ../../../toolkit/NSM/extern/Karamelo/ovito_merge_dumps.py

在 ``FENGSim/starter/karamelo/ex_1`` 路径下会产生dump.*.dump系列结果文件，可以用OVITO打开查看结果动画。
    
**********************
前后处理文件格式
**********************
