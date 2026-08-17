.DEFAULT_GOAL := help

help: ## Show available targets
	@grep -hE '^[a-z-]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*##/\t/' | expand -t20

generate: ## Regenerate catalog/, templates/, INDEX.md, README block, gist bundle
	python3 scripts/generate.py

check: generate ## Fail if generated files are stale or a secret-like string slipped in
	@git diff --exit-code -- catalog templates INDEX.md README.md skills/build-skill/build-skill.gist.md \
		|| (echo "\nGenerated files are stale. Commit the output of 'make generate'." && exit 1)
	@! grep -rEln '(sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{32,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)' \
		--include='*.md' --include='*.json' --include='*.py' . \
		|| (echo "\nSecret-like string found — skills reference connector and env-var NAMES only." && exit 1)
	@echo "checks passed"
