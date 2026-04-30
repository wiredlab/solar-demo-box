

SOURCE=$(wildcard *.adoc)
INCLUDE_DIRS=css fig

NO_RENDER=refs.html subs.html template.html
HTMLS=$(filter-out $(NO_RENDER), $(SOURCE:.adoc=.html))
PDFS=$(HTMLS:.html=.pdf)

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
ASCIIDOCTOR_OPTS+=-a stylesdir@=css
ASCIIDOCTOR_OPTS+=-a stylesheet@=asciidoctor-local.css
ASCIIDOCTOR_OPTS+=-a scriptsdir@=js
ASCIIDOCTOR_OPTS+=-a sectanchors@
ASCIIDOCTOR_OPTS+=-a sectnums@
ASCIIDOCTOR_OPTS+=-a section-refsig@='&sect;'
ASCIIDOCTOR_OPTS+=-a source-highlighter@=rouge
ASCIIDOCTOR_OPTS+=-a stem@=latexmath
ASCIIDOCTOR_OPTS+=-a eqnums@=all
ASCIIDOCTOR_OPTS+=-a toc@=left
ASCIIDOCTOR_OPTS+=-a xrefstyle@=short
#ASCIIDOCTOR_OPTS+=-a env-handout



define source_epoch
SOURCE_DATE_EPOCH=$(shell (git log -1 --pretty=%ct -- $(1); date +%s) | head -1)
endef

default: html


html: $(HTMLS) $(RESOURCES)

pdf: $(PDFS)

#	    $(INCLUDE_DIRS) *.html \


web: html pdf
	rsync -avuP \
	    --include='.htaccess' \
	    --exclude='.*' \
	    $(HTMLS) $(PDFS) \
	    fig css common js \
	    dan@tesla.whiteaudio.com:/var/www/www.agnd.net/valpo/solar/

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


#guidebook.pdf: $(SOURCE)

%.xml: %.adoc
	$(call source_epoch, $<) $(ASCIIDOCTOR) \
	    -b docbook \
	    $(ASCIIDOCTOR_OPTS) \
	    $<


# NOTE: font-awesome and mathjax dir trees are expected to be at the server root
%.html: %.adoc
	$(call source_epoch, $<) $(ASCIIDOCTOR) \
	    $(ASCIIDOCTOR_OPTS) \
	    --out-file "$@" "$<"
	    #--out-file - "$<" | sed -e 's,https://cdnjs.cloudflare.com/ajax/libs,,' > "$@"

# NOTE: font-awesome and mathjax dir trees are expected to be at the server root
%.handout.html: %.adoc
	$(call source_epoch, $<) $(ASCIIDOCTOR) \
	    $(ASCIIDOCTOR_OPTS) \
	    -a env-handout \
	    --out-file "$@" "$<"
	    #--out-file - "$<" | sed -e 's,https://cdnjs.cloudflare.com/ajax/libs,,' > "$@"



#syllabus.html: syllabus.adoc
#	$(call source_epoch, $<) $(ASCIIDOCTOR) \
#	    $(ASCIIDOCTOR_OPTS) \
#	    -a !linkcss \
#	    $<

#	    -r asciidoctor-mathematical \

#%.pdf: %.adoc
#	$(call source_epoch, $<) $(ASCIIDOCTOR) \
#	    -a mathematical-format=svg \
#	    -a allow-uri-read \
#	    $(ASCIIDOCTOR_OPTS) \
#	    $<

%.pdf: %.handout.html
	google-chrome --headless \
	    --run-all-compositor-stages-before-draw \
	    --virtual-time-budget=1000 \
	    --print-to-pdf-no-header \
	    --no-pdf-header-footer \
	    --print-to-pdf=$@ $<

#%.pdf: %.adoc
#	$(call source_epoch, $<) $(ASCIIDOCTOR) \
#	    -r asciidoctor-pdf -b pdf \
#	    -r asciidoctor-mathematical \
#	    -a mathematical-format=svg \
#	    $(ASCIIDOCTOR_OPTS) \
#	    $<

#%.pdf: %.adoc
#	$(call source_epoch, $<) \
#	./asciidoctor-web-pdf-linux-v1.0.0-alpha.14/asciidoctor-web-pdf \
#	    $(ASCIIDOCTOR_OPTS) \
#	    -a allow-uri-read \
#	    -a stylesheet="+web-pdf.css" \
#	    $<

clean:
	rm $(SOURCE:.adoc=.html)

