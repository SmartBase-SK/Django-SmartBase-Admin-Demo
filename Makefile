#COLORS
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

ifeq ($(FAIL_FAST), 1)
	FFAST := --failfast
else
	FFAST :=
endif

ifeq ($(APP),)
	TEST_APP :=
else
	TEST_APP = $(APP)
endif

# ifeq ($(PATTERN),)
# 	FILE_PATTERN := test*.py
# else
# 	FILE_PATTERN := $(PATTERN)*.py
# endif

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
HELP_FUN = \
	%help; \
	while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([a-zA-Z\-]+)\s*:.*\#\#(?:@([a-zA-Z\-]+))?\s(.*)$$/ }; \
	print "usage: make [target]\n\n"; \
	for (sort keys %help) { \
	print "${WHITE}$$_:${RESET}\n"; \
	for (@{$$help{$$_}}) { \
	$$sep = " " x (32 - length $$_->[0]); \
	print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
	}; \
	print "\n"; }

help: ##@other Show this help.
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

migrations: ## create new migrations after model changes
	python manage.py makemigrations
migrate: ## run already created mirgations
	python manage.py migrate
shell:  ## run python shell with django setup in current virtualenv
	python manage.py shell
tests:  ## run unit test with IS_TETS=true
	export IS_TEST=true && python manage.py test $(TEST_APP) $(FFAST) --keepdb
server:  ## run server for development
	python manage.py runserver 0:8000
setup: ## install requirements via pip
	pip install -r requirements.txt
reverse:  ## create js collect static reverse
	python manage.py collectstatic_js_reverse
fix:  ## run fix_migrations command
	python manage.py fix_migrations
pyclean:  ## remove all pyc and __pycache__ files
	find . -type f -name "*.py[co]" -delete && find . -type d -name "__pycache__" -delete
msg:  ## run makemessages script
	python manage.py makemessages --no-location
compile: ## run compilemessages
	python manage.py compilemessages
feed: ## run es_feed_index
	python manage.py es_feed_index
