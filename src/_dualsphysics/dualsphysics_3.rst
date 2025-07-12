**********************
算例测试
**********************

.. code-block:: bash

   cd FENGSim/toolkit/Particles/dualsphysics/examples/main/01_DamBreak
   ./xCaseDambreak_linux64_CPU.sh

这里需要注意的是运行 ``xCaseDambreak_linux64_CPU.sh`` ，需要将 ``FENGSim/toolkit/Particles/dualsphysics/bin`` 路径下的一些程序权限设置成可执行。
用Paraview软件打开 ``FENGSim/toolkit/Particles/dualsphysics/examples/main/01_DamBreak/CaseDambreak_out`` 路径下的 ``CaseDambreak_Box_Dp.vtk`` 文件和
``CaseDambreak_Building_Dp.vtk`` 文件，再打开 ``FENGSim/toolkit/Particles/dualsphysics/examples/main/01_DamBreak/CaseDambreak_out/particles`` 路径下的
``PartFluid_*.vtk`` 文件。

.. image:: fig/dualsphysics.gif
   :width: 640
   :alt: alternate text
   :align: center
