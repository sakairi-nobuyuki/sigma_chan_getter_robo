SRCS = db_oparators  pyproject.toml  sigma_chan_db  tweet_getter tests
POETRY_PREFIX = poetry run


format:
	$(foreach DIR, $(SRCS), $($(POETRY_PREFIX) black $(DIR) --config pyproject.toml))
	$(foreach DIR, $(SRCS), $($(POETRY_PREFIX) isort $(DIR) --profile black))