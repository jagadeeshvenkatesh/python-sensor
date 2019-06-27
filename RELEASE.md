# Release Steps

_Note: To release a new Instana package, you must be a project member of the [Instana package project on Pypi](https://pypi.org/project/instana/).
Contact [Peter Giacomo Lombardo](https://github.com/pglombardo) to be added._

1. Before releasing, assure that [tests have passed](https://circleci.com/gh/instana/workflows/python-sensor) and that the package has also been manually validated in various stacks.
2. `git checkout master && git pull --rebase && pip install -U twine`
3. Bump the package version in `setup.py`
4. Create a [draft Release on Github](https://github.com/instana/python-sensor/releases)
5. `python setup.py sdist bdist_wheel` to create the whl file in `./dist/` 
6. Upload the package to Pypi with twine: `twine upload dist/instana-<version>*`
7. Validate the new release on https://pypi.org/project/instana/
8. Update Python documentation with latest changes: https://docs.instana.io/ecosystem/python/
9. Publish the draft release on [Github](https://github.com/instana/python-sensor/releases)