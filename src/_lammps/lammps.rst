--------------------
dat转inp
--------------------

在 ``FENGSim/starter/ccx/oiltank`` 目录下有configure_modal.xml、oiltank.dat、dat2inp.py。
configure_modal.xml是配置文件，oiltank.dat是网格文件。
dat2inp.py提取configure_modal.xml文件中的数据，提取oiltank.dat文件中的数据，将.dat格式转成.inp格式，合并生成新的modal.inp。

dat2inp.py的运行结果如下图，文件名称不用输入后缀名。

.. image:: fig/ccx/oiltank.jpg
   :scale: 50 %
   :alt: alternate text
   :align: center

.dat文件格式很简单，如下第1行的31276为顶点个数，99818为单元个数，
第8行的sphere_tank为单元组名称，56644为单元个数，第12行outer_surface_nodes为顶点组名称，9247为顶点个数，其他类似。 ::
  
  3 4 31276 99818
  1 -8315 2.55536e-12 0
  ......
  31276 8315 0 10850 
  1 59 2 1 98
  ......
  99818 31180 31223 31222 31179
  8 sphere_tank 56644
  2601
  .....
  97218
  7 outer_surface_nodes 9247
  788
  .....
  30489
  7 inner_surface_nodes 8317
  862
  .....
  30415
  7 fixed_nodes 200
  1
  .....
  31222
  8 guandao 2866
  47324
  .....
  52495
  8 support 40308
  1
  .....
  99818
  7 guandao_fixed_nodes 24
  14829
  .....
  16488

运行以下命令。 ::
  
  cd FENGSim/starter/ccx/oiltank
  mkdir Refs
  ./../../../toolkit/MultiX/extern/Calculix/bin/ccx_2.21 modal
  ./../../../toolkit/MultiX/extern/Calculix/bin/cgx -b shapes.fbl
  python3 ./../../../toolkit/MultiX/extern/Calculix/ccx2paraview/ccx2paraview.py modal.frd vtk

.. image:: fig/ccx/oiltank.gif
   :scale: 50 %
   :alt: alternate text
   :align: center

