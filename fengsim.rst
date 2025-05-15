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
