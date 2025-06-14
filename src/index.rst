###########################
Introduction
###########################

 
该文档介绍了SDK中各个软件的参考文献、编译安装、算例测试、前后处理，未来将进一步包括SDK中的函数接口。

SDK下载地址为 `<https://github.com/OpenDigitalTwin-Dev/FENGSim>`_ ，网站地址为 `<https://www.opendigitaltwin.top/>`_ 。


.. Hidden TOCs

.. toctree::
   :maxdepth: 1
   :hidden:
      
   fengsim
   multix
   ccx
   openfoam
   su2
   cantera
   palace
   mbdyn
   ros2
   karamelo
   lammps
   maxima
   geometry
   sphinx


* 固体
   * 模态，homogeneous Dirichlet BC，homogeneous Neumann BC，非均匀材料
* 流体
   * Euler方程，可压，vertex-centered
* 电磁
   * 静电，ZeroCharge（homogeneous Neumann BC），Ground（homogeneous Dirichlet BC），Terminal（Dirichlet BC为常数）
   * 静磁，PEC（homogeneous Dirichlet BC），PMC（homogeneous Neumann BC），SurfaceCurrent（Source Term），非线性
* 多体动力学
   * 2自由度运动学方程
   * 6自由度运动学方程
   * 6自由度动力学方程
