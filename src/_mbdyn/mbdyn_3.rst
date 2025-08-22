**********************
算例测试
**********************

在 ``FENGSim/starter/mbdyn/free_falling`` 路径下有一个自由落体的简单例子，运行如下命令。 ::
  
    cd FENGSim/starter/mbdyn/free_falling
    ./../../../toolkit/DAE/install/mbdyn_install/bin/mbdyn -f free_falling_body_E.mbd
    gnuplot
    plot 'free_falling_body_E.mov' using 3:4

.. image:: fig/mbdyn_1.png
   :scale: 50 %
   :alt: alternate text
   :align: center    

在 ``FENGSim/starter/mbdyn/robot`` 路径下有UR3机械臂例子，运行如下命令。 ::
  
    cd FENGSim/starter/mbdyn/robot
    ./run


