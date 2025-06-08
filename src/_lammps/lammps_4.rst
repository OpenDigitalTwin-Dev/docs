
**********************
前后处理
**********************

要生成可视化的结果，可以在输入文件中取消注释相关输出指令，生成dump.crack结果文件。以官方的裂纹扩展为例，去掉 ``FENGSim/starter/lammps/crack`` 路径下 ``in.crack`` 前处理文件中的dump开头几行的注释，形成如下的前处理文件。

.. code-block:: bash

    # 2d LJ crack simulation

    dimension	2
    boundary	s s p
    
    atom_style	atomic
    neighbor	0.3 bin
    neigh_modify	delay 5
    
    # create geometry
    
    lattice		hex 0.93
    region		box block 0 100 0 40 -0.25 0.25
    create_box	5 box
    create_atoms	1 box
    
    mass		1 1.0
    mass		2 1.0
    mass		3 1.0
    mass		4 1.0
    mass		5 1.0
    
    # LJ potentials
    
    pair_style	lj/cut 2.5
    pair_coeff	* * 1.0 1.0 2.5
    
    # define groups
    
    region	        1 block INF INF INF 1.25 INF INF
    group		lower region 1
    region		2 block INF INF 38.75 INF INF INF
    group		upper region 2
    group		boundary union lower upper
    group		mobile subtract all boundary
    
    region		leftupper block INF 20 20 INF INF INF
    region		leftlower block INF 20 INF 20 INF INF
    group		leftupper region leftupper
    group		leftlower region leftlower
    
    set		group leftupper type 2
    set		group leftlower type 3
    set		group lower type 4
    set		group upper type 5
    
    # initial velocities
    
    compute	  	new mobile temp
    velocity	mobile create 0.01 887723 temp new
    velocity	upper set 0.0 0.3 0.0
    velocity	mobile ramp vy 0.0 0.3 y 1.25 38.75 sum yes
    
    # fixes
    
    fix		1 all nve
    fix		2 boundary setforce NULL 0.0 0.0
    
    # run
    
    timestep	0.003
    thermo		200
    thermo_modify	temp new
    
    neigh_modify	exclude type 2 3
    
    dump		1 all atom 500 dump.crack
    
    dump		2 all image 250 image.*.jpg type type zoom 1.6 adiam 1.5
    dump_modify	2 pad 4
    
    #dump		3 all movie 250 movie.mpg type type zoom 1.6 adiam 1.5
    #dump_modify	3 pad 4
    
    run		5000


    
LAMMPS通过in文件中关键字来设置仿真需要的参数，关于各个关键词的意思与设置规则，请访问 `LAMMPS官方网站 <https://lammps.sandia.gov/>`_ 或查阅其 `官方文档 <https://docs.lammps.org/Manual.html>`_。

对于LAMMPS模拟前的数据准备和模拟后的数据分析，最简单的方式可以在in文件中设置dump关键字来控制输出数据文件和相应的图片文件。
更精细的后处理则通常需要使用其他辅助工具。例如，利用VMD或OVITO可以对lammpstrj文件进行可视化分析；而对于复杂的系统设置，可能还需要编写自定义脚本或修改LAMMPS源代码来满足特定需求。

此外，LAMMPS提供了强大的重启功能，允许用户在遇到意外中断后继续之前的模拟。这可以通过在输入脚本中添加restart命令实现，例如：

.. code-block:: bash

    restart ${restartFreq} restart.*

其中`${restartFreq}`是保存重启文件的频率，而`restart.*`则是重启文件的模板名称。

