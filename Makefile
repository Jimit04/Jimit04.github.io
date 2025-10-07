# Makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD  ?= sphinx-build
SOURCEDIR    = docs/source
BUILDDIR     = docs/build
AUTOBUILD    = sphinx-autobuild

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Custom targets
livehtml:
	@$(AUTOBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" --host 0.0.0.0 --port 8000 --watch "$(SOURCEDIR)"

clean:
	rm -rf "$(BUILDDIR)"
	rm -rf docs/build
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

install:
	pip install -r requirements.txt

setup: install
	pre-commit install

# GitHub Pages deployment
deploy: html
	ghp-import -n -p -f docs/build/html

# Development server
dev: livehtml

# Check links
linkcheck:
	@$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck"

# Run tests
test:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

# Code formatting
format:
	black src/ tests/
	black docs/source/conf.py

# Code linting
lint:
	flake8 src/ tests/
	flake8 docs/source/conf.py

# All checks
 check: format lint test linkcheck

# Build all formats
all: html pdf epub

pdf:
	@$(SPHINXBUILD) -b pdf "$(SOURCEDIR)" "$(BUILDDIR)/pdf"

epub:
	@$(SPHINXBUILD) -b epub "$(SOURCEDIR)" "$(BUILDDIR)/epub"