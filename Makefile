# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = 
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = ReadtheDocsSphinxTheme
SOURCEDIR     = src
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".

all:
	rm -rf build
	sphinx-build -M html "$(SOURCEDIR)" "$(BUILDDIR)"

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
