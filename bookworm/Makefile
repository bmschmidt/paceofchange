
all: jsoncatalog.txt unigrams.txt paceofchange

paceofchange:
	git clone git@github.com:Bookworm-Project/BookwormDB $@

unigrams.txt:
	python makeUnigrams.py > $@

jsoncatalog.txt:
	python makeJSONcatalog.py > $@
