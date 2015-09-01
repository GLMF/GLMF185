all: build

install: build
	rsync -avz export/ login@www.example.net:/srv/www/htdocs/

build: clean
	sed -i /^-resource/d compile.hxml
	ls tpl/*.html | sed s',tpl/\(.*\).html,-resource tpl/\1.html@\1,' >> compile.hxml
	haxe compile.hxml
	cp -f tpl/styles.css export/

sqlite:
	mkdir -p export/data
	chmod -R o+w export/data

clean:
	rm -rf export/{lib,res}
	rm -f export/index.php
	rm -f export/styles.css
