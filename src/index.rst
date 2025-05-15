###########################
文档模板介绍
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

Sphinx和reStructuredText介绍链接为 `<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ 。
该文档模板下载地址为 `<https://github.com/readthedocs/sphinx_rtd_theme>`_ 中的docs文件夹，使用文档链接为 `<https://sphinx-rtd-theme.readthedocs.io/>`_ ，
是ReadtheDocs自己做的Sphinx模板。

采用了 `<https://sphinx-rtd-theme.readthedocs.io/>`_ 中的Configuration中的以下内容，加入到了 ``FENGSim/docs/src/conf.py`` 中。

.. code:: python

    html_theme_options = {
        'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
        'analytics_anonymize_ip': False,
        'logo_only': False,
        'prev_next_buttons_location': 'bottom',
        'style_external_links': False,
        'vcs_pageview_mode': '',
        'style_nav_header_background': 'white',
        'flyout_display': 'hidden',
        'version_selector': True,
        'language_selector': True,
        # Toc options
        'collapse_navigation': True,
        'sticky_navigation': True,
        'navigation_depth': 4,
        'includehidden': True,
        'titles_only': False
    }

需要注意以下几点操作：

* ``FENGSim/docs/.readthedocs.yaml`` 中有两处路径设置，分别为configuration: src/conf.py和- requirements: requirements.txt。
* ``FENGSim/docs/requirements.txt`` 中列出了需要ReadtheDocs安装的软件包。
* ``FENGSim/docs/Makefile`` 中有两处路径设置，分别为SOURCEDIR=src和BUILDDIR=build。
* ``FENGSim/docs/src/conf.py`` 为Sphinx配置程序，设置了logo路径为html_logo="demo/static/Fengsim_logo_hi.png"， ``FENGSim/docs/src/demo/static/Fengsim_logo_hi.png`` 是logo图片。
