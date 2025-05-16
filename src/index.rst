###########################
File Format
###########################


.. Hidden TOCs

.. toctree::
   :maxdepth: 1
   :hidden:
      
   fengsim
   ccx
   openfoam
   su2
   cantera
   palace
   mbdyn
   ros2
   karamelo

Sphinx和reStructuredText的介绍链接为 `<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ 。
该模板下载链接为 `<https://github.com/readthedocs/sphinx_rtd_theme>`_ ，其中docs文件夹为该模板，模板使用文档链接为 `<https://sphinx-rtd-theme.readthedocs.io/>`_ ，
是ReadtheDocs自己做的Sphinx模板。 `<https://sphinx-rtd-theme.readthedocs.io/>`_ 中的Configuration中有模板格式参数介绍，
可以在 ``FENGSim/docs/src/`` 路径下的conf.py中用html_theme_options设置，conf.py是Sphinx编译的配置文件。

需要注意以下几点操作：

* ``FENGSim/docs/`` 路径下的.readthedocs.yaml文件中有两处路径设置，需要设置conf.py和requirements.txt的路径。
* ``FENGSim/docs/`` 路径下的requirements.txt文件中列出了需要ReadtheDocs安装的软件包，其中sphinx-rtd-theme需要指定3.0.2版本，否则 ``FENGSim/docs/src`` 路径下的conf.py中的html_theme_options中的version_selector会有问题。
* ``FENGSim/docs/`` 路径下的Makefile文件中有两处路径设置，分别为SOURCEDIR和BUILDDIR，SOURCEDIR为conf.py和.rst文件的路径，BUILDDIR为编译结果路径。
* ``FENGSim/docs/src/`` 路径下的conf.py文件为Sphinx配置程序，用html_logo设置了logo路径，Fengsim_logo_hi.png是logo图片。
