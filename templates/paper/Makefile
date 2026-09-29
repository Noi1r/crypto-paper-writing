# Makefile -- build with latexmk.
# Targets: all (anonymous submission), camera (proceedings), full (ePrint), check, anon, clean.
MAIN ?= main
LIMIT ?= 30
ROOT ?= $(shell if [ -d ../skills ]; then echo ..; else echo ../..; fi)

all: llncs.cls
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

camera: llncs.cls
	latexmk -pdf -interaction=nonstopmode -halt-on-error main_camera.tex

full: llncs.cls
	latexmk -pdf -interaction=nonstopmode -halt-on-error main_full.tex

llncs.cls:
	@kpsewhich llncs.cls >/dev/null 2>&1 || sh ./fetch_llncs.sh

check: all
	python3 $(ROOT)/skills/camera-ready/scripts/pdf_checks.py $(MAIN).pdf --log $(MAIN).log --limit $(LIMIT)

audit:
	python3 $(ROOT)/scripts/audit_tex.py $(MAIN).tex ../EVIDENCE.md
	@for f in sections/*.tex; do python3 $(ROOT)/scripts/audit_tex.py "$$f" ../EVIDENCE.md || exit $$?; done

anon: all
	python3 $(ROOT)/skills/anonymize-check/scripts/anon_check.py sections refs.bib macros.tex $(MAIN).pdf \
	  $(if $(wildcard .denylist.txt),--deny-file .denylist.txt,)

clean:
	latexmk -C $(MAIN).tex; latexmk -C main_camera.tex; latexmk -C main_full.tex
	rm -f *.bbl *.run.xml

.PHONY: all camera full check audit anon clean
