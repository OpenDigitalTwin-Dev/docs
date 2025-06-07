
**********************
前后处理
**********************

LAMMPS通过in文件中关键字来设置仿真需要的参数，关于各个关键词的意思与设置规则，请访问 `LAMMPS官方网站 <https://lammps.sandia.gov/>`_ 或查阅其 `官方文档 <https://docs.lammps.org/Manual.html>`_。

对于LAMMPS模拟前的数据准备和模拟后的数据分析，最简单的方式可以在in文件中设置dump关键字来控制输出数据文件和相应的图片文件。
更精细的后处理则通常需要使用其他辅助工具。例如，利用VMD或OVITO可以对lammpstrj文件进行可视化分析；而对于复杂的系统设置，可能还需要编写自定义脚本或修改LAMMPS源代码来满足特定需求。

此外，LAMMPS提供了强大的重启功能，允许用户在遇到意外中断后继续之前的模拟。这可以通过在输入脚本中添加restart命令实现，例如：

.. code-block:: bash

    restart ${restartFreq} restart.*

其中`${restartFreq}`是保存重启文件的频率，而`restart.*`则是重启文件的模板名称。

