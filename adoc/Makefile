

SOURCE=$(wildcard *.adoc)
INCLUDE_DIRS=css fig

FIGURES=$(wildcard fig/*)
CSSS=$(wildcard css/*)
COMMONS=$(wildcard common/*)

RESOURCES=$(FIGURES) $(CSSS) $(COMMONS)

ASCIIDOCTOR=bundle exec asciidoctor

# The trailing "@" soft sets the attribute, this allows overriding the value in
# the individual document if desired.
# https://docs.asciidoctor.org/asciidoc/latest/attributes/assignment-precedence/
ASCIIDOCTOR_OPTS=
ASCIIDOCTOR_OPTS+=-a docinfo@=shared,private
ASCIIDOCTOR_OPTS+=-a docinfodir@=common
ASCIIDOCTOR_OPTS+=-a icons@=font
ASCIIDOCTOR_OPTS+=-a imagesdir@=fig
ASCIIDOCTOR_OPTS+=-a linkcss@
ASCIIDOCTOR_OPTS+=-a scriptsdir@=js
ASCIIDOCTOR_OPTS+=-a sectanchors@
ASCIIDOCTOR_OPTS+=-a sectnums@
ASCIIDOCTOR_OPTS+=-a section-refsig@='&sect;'
ASCIIDOCTOR_OPTS+=-a source-highlighter@=rouge
ASCIIDOCTOR_OPTS+=-a stem@=latexmath
ASCIIDOCTOR_OPTS+=-a eqnums@=all
ASCIIDOCTOR_OPTS+=-a stylesdir@=css
ASCIIDOCTOR_OPTS+=-a stylesheet@=asciidoctor.css
ASCIIDOCTOR_OPTS+=-a toc@=left
ASCIIDOCTOR_OPTS+=-a xrefstyle@=short
#ASCIIDOCTOR_OPTS+=-a env-handout



define source_epoch
SOURCE_DATE_EPOCH=$(shell (git log -1 --pretty=%ct -- $(1); date +%s) | head -1)
endef

default: html


html: $(filter-out subs.html, $(SOURCE:.adoc=.html)) $(RESOURCES)

pdf: $(SOURCE:.adoc=.pdf)

#	    $(INCLUDE_DIRS) *.html \

#web: html
#	rsync -avuP \
#	    --include='.htaccess' \
#	    --exclude='.*' \
#	    --exclude='Makefile' \
#	    --delete-excluded \
#	    --delete \
#	    . \
#	    dan@tesla.whiteaudio.com:/var/www/www.agnd.net/valpo/341/guidebook/

web: html
	rsync -avuP \
	    --include='.htaccess' \
	    --exclude='.*' \
	    *.html fig css common js \
	    dan@tesla.whiteaudio.com:/var/www/www.agnd.net/valpo/340/

#fig: $(FIGURES)
fig:
	$(MAKE) -C fig


.PHONY: dev
#dev: .dev

#windowactivate $$(xdotool search --onlyvisible --name "Electronics Tour Book")
#dev: $(SOURCE:.adoc=.html)
#	-xdotool \
#	    windowactivate $$(xdotool search --desktop $$(xdotool get_desktop) --onlyvisible --name "Scheduling Bazaar") \
#	    key 'ctrl+r' \
#	    windowactivate $$(xdotool getwindowfocus) >/dev/null 2>&1
#	#touch .dev
dev:
	(ls *.adoc | entr make & python -m http.server)

guidebook.html: $(SOURCE) $(GUIDEBOOK_INCLUDES) common/docinfo.html

#guidebook.pdf: $(SOURCE)

%.xml: %.adoc
	$(call source_epoch, $<) $(ASCIIDOCTOR) \
	    -b docbook \
	    $(ASCIIDOCTOR_OPTS) \
	    $<

%.html: %.adoc
	$(call source_epoch, $<) $(ASCIIDOCTOR) \
	    $(ASCIIDOCTOR_OPTS) \
	    $<

%.handout.html: %.adoc
	$(call source_epoch, $<) $(ASCIIDOCTOR) \
	    $(ASCIIDOCTOR_OPTS) \
	    -a env-handout \
	    --out-file "$@" \
	    $<

#%.pdf: %.adoc
#	$(call source_epoch, $<) bundle exec asciidoctor-pdf \
#	    -r asciidoctor-mathematical \
#	    -a mathematical-format=svg \
#	    -a allow-uri-read \
#	    $(ASCIIDOCTOR_OPTS) \
#	    $<

#%.pdf: %.html
#	#specific fixup for htmlto and underlying phantomjs DPI issue
#	sed 's/<\/head>/<style>@media print{body{zoom:0.80;}}<\/style><\/head>/' $< > $<.tmp.html
#	~/node_modules/htmlto/bin/htmlto $<.tmp.html $@
#	rm $<.tmp.html

%.pdf: %.handout.html
	#specific fixup for htmlto and underlying phantomjs DPI issue
	sed 's/<\/head>/<style>@media print{@page{margin:0.8in; size:8.5in 11in;}}<\/style><\/head>/' $< > $<.tmp.html
	google-chrome --headless --run-all-compositor-stages-before-draw --virtual-time-budget=1000 --print-to-pdf-no-header --print-to-pdf=$@ $<.tmp.html
	rm $<.tmp.html


