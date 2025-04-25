######################
CCX
######################

**********************
参考资料
**********************

CalculiX网站为 `<https://www.calculix.de/>`_ 和 `<https://www.dhondt.de/>`_ ， `<https://www.dhondt.de/>`_ 上面可以找到使用说明 `<https://www.dhondt.de/ccx_2.22.pdf>`_ 和一些算例，
还有一个算例集在 `<https://github.com/calculix/CalculiX-Examples>`_ ，需要注意的是CalculiX-Examples算例集中每个例子的README.md中有详细的操作介绍。CalculiX配备了一个前后处理软件CalculiX GraphiX。

**********************
编译安装
**********************

按照如下操作在FENGSim中编译CalculiX和CalculiX GraphiX。

* 首先克隆FENGSim。 ::
  
    git clone https://github.com/OpenDigitalTwin-Dev/FENGSim.git
  
* 再将NSM克隆到 ``FENGSim/toolkit`` 路径下。 ::
  
    cd FENGSim/toolkit
    git clone https://github.com/OpenDigitalTwin-Dev/NSM.git
  
* 在 ``FENGSim/toolkit/NSM/extern/Calculix`` 中有一个install.sh脚本，直接运行该脚本可以在Ubuntu24.04下编译CalculiX和CalculiX GraphiX，无需其他操作。 ::
  
    cd FENGSim/toolkit/NSM/extern/Calculix
    ./install.sh
    
**********************
算例测试
**********************

在 ``FENGSim/starter/ccx/Mesh1`` 目录中保存了一个模态算例，按照其中README.md的介绍，运行以下命令。 ::
  
  cd FENGSim/starter/ccx/Mesh1
  mkdir Refs
  ./../../../toolkit/NSM/extern/Calculix/bin/cgx -b pre.fbl
  ./../../../toolkit/NSM/extern/Calculix/bin/ccx_2.21 modal
  ./../../../toolkit/NSM/extern/Calculix/bin/cgx -b shapes.fbl

这里需要注意的是该算例会生成.gif动画文件，然后保存在 ``FENGSim/starter/ccx/Mesh1/Refs`` 目录中。
算例的运行可以直接执行上面的命令，也可以运行test.py脚本，但是由于可执行程序目录不一定是test.py脚本中的默认目录，脚本运行会有问题，另外test.py脚本自动创建了Refs目录，
如果运行命令，需要手动创建该目录。

+------------------------------------+------------------------------------+-----------------------------------+
| .. image:: fig/modal/shape_1.gif   | .. image:: fig/modal/shape_2.gif   | .. image:: fig/modal/shape_3.gif  |
|    :width: 200px                   |    :width: 200px                   |    :width: 200px                  |
+------------------------------------+------------------------------------+-----------------------------------+
| .. image:: fig/modal/shape_4.gif   | .. image:: fig/modal/shape_5.gif   | .. image:: fig/modal/shape_6.gif  |
|    :width: 200px                   |    :width: 200px                   |    :width: 200px                  |
+------------------------------------+------------------------------------+-----------------------------------+
| .. image:: fig/modal/shape_7.gif   | .. image:: fig/modal/shape_8.gif   | .. image:: fig/modal/shape_9.gif  |
|    :width: 200px                   |    :width: 200px                   |    :width: 200px                  |
+------------------------------------+------------------------------------+-----------------------------------+
| .. image:: fig/modal/shape_10.gif  | .. image:: fig/modal/shape_11.gif  | .. image:: fig/modal/shape_12.gif |
|    :width: 200px                   |    :width: 200px                   |    :width: 200px                  |
+------------------------------------+------------------------------------+-----------------------------------+

.. image:: fig/shape_7.gif
   :scale: 50 %
   :alt: alternate text
   :align: center
	   
**********************
前后处理文件格式
**********************
