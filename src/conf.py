# -*- coding: utf-8 -*-

import sys
import os
import re

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('./demo/'))

from sphinx_rtd_theme import __version__ as theme_version
from sphinx_rtd_theme import __version_full__ as theme_version_full
from sphinx.locale import _

project = u'FENGSim'
slug = re.sub(r'\W+', '-', project.lower())
version = "1.0"
release = "1.0"
author = u'Dr. Jiping Xin'
copyright = author
language = 'en'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = []
locale_dirs = ['locale/']
gettext_compact = False

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

if sys.version_info < (3, 0):
    tags.add("python2")
else:
    tags.add("python3")

intersphinx_mapping = {
    'rtd': ('https://docs.readthedocs.io/en/stable/', None),
    'rtd-dev': ('https://dev.readthedocs.io/en/stable/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
    
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'navigation_depth': 5,
    'style_nav_header_background': '#BFBFBF',
    'version_selector': False,
    'flyout_display':'hidden',
    'display_version': True,   
    'prev_next_buttons_location':'top'
}
html_context = {}

if not 'READTHEDOCS' in os.environ:
    html_static_path = ['_static/']
    html_js_files = ['debug.js']
    html_context["DEBUG"] = True

html_logo = "demo/static/Fengsim_logo_hi.png"
html_show_sourcelink = True
html_favicon = "demo/static/favicon.ico"

htmlhelp_basename = slug


latex_documents = [
  ('index', '{0}.tex'.format(slug), project, author, 'manual'),
]

man_pages = [
    ('index', slug, project, [author], 1)
]

texinfo_documents = [
  ('index', slug, project, author, slug, project, 'Miscellaneous'),
]


# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value',
        doc_field_types=[
            PyField(
                'type',
                label=_('Type'),
                has_arg=False,
                names=('type',),
                bodyrolename='class'
            ),
            Field(
                'default',
                label=_('Default'),
                has_arg=False,
                names=('default',),
            ),
        ]
    )
