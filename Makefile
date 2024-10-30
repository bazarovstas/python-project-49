install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl

package-reinstall:
	pip install --upgrade --force-reinstall dist/*.whl


brain-games:
	poetry run brain-games
