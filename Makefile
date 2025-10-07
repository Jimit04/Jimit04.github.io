# ============================================================================
# Sphinx-friendly Makefile for Jimit Vyas site
# ============================================================================

# ---- Config ----------------------------------------------------------------
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs/source
BUILDDIR      = docs/build
VENV          = .venv
PYTHON        = $(VENV)/bin/python
PIP           = $(VENV)/bin/pip
REQUIREMENTS  = requirements.txt

# ---- Colours ---------------------------------------------------------------
BLUE  := \033[36m
GREEN := \033[32m
RESET := \033[0m

# ---- Default goal ----------------------------------------------------------
.PHONY: help
help: ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(BLUE)%-15s$(RESET) %s\n", $$1, $$2}'

# ---- Setup -----------------------------------------------------------------
$(VENV)/bin/activate: requirements.txt
	@echo "$(GREEN)Creating venv & installing deps...$(RESET)"
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r $(REQUIREMENTS)
	touch $(VENV)/bin/activate

.PHONY: install
install: $(VENV)/bin/activate ## install dependencies (one-time)

# ---- Build -----------------------------------------------------------------
.PHONY: build
build: install ## build site → docs/build/html
	$(PYTHON) -m sphinx -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html
	@echo "$(GREEN)✔ Built at file://$(PWD)/$(BUILDDIR)/html/index.html$(RESET)"

# ---- Clean -----------------------------------------------------------------
.PHONY: clean
clean: ## remove build artefacts
	rm -rf $(BUILDDIR)
	@echo "$(GREEN)✔ Build folder cleaned$(RESET)"

# ---- Live preview ----------------------------------------------------------
.PHONY: serve
serve: build ## build + serve on http://localhost:8000
	@echo "$(GREEN)Serving at http://localhost:8000 ...$(RESET)"
	$(PYTHON) -m http.server -d $(BUILDDIR)/html