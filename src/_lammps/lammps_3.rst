
**********************
算例测试
**********************


LAMMPS提供了一系列示例案例帮助用户快速上手。比如，通过运行`examples/README`中的描述，您可以尝试一些简单的模拟任务，如裂纹扩展、流体流动、摩擦接触等。
以官方的裂纹扩展为例，去掉dump几行的注释，形成如下的输入文件

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

执行LAMMPS程序运行计算并输出dump文件及图片

.. code-block:: bash

    lmp_serial < in.crack

要生成可视化的结果，可以在输入文件中取消注释相关输出指令，生成一系列JPG或PPM图像文件，或者产生快照文件供VMD等可视化工具读取。
然后可以看到从第0步到第5000步一共21张图片，第5000步结果如下图

 .. image:: fig/lammps/.image.5000.jpg
    :align: center
