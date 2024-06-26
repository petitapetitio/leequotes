[![PyPI version fury.io](https://badge.fury.io/py/ansicolortags.svg)](https://pypi.python.org/pypi/leequotes/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=plastic)](http://makeapullrequest.com)
***

# leequotes

A python package that provides Bruce Lee quotes

A simple website showcasing the leequotes lib is available at http://lxnd.pythonanywhere.com/

# How to install

From a terminal, run the following command:
```shell
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the package
pip install leequotes
```

# How to use

Here is a minimal example of how to use the package:
```python
from leequotes import leequotes

quote = leequotes.random()
print(quote)
```


# How to update the package (for clients)

To update the package, run the following command:
```shell
pip intall --upgrade leequotes
```

# How to update the package (for maintainers)

Once the modification is developed : 
1. Increment the version in `pyproject.toml`
2. Run `python -m build` to build the package
3. Delete the old builds in the `dist` folder (if any)
4. Run `twine upload dist/*`to upload the builds on PyPI

Notes : 
- Once uploaded, the package is immutable. If you need to make changes, you will need to increment the version again.
- To test the package locally, you can run `pip install dist/<the-local-build>.whl`

# Useful links

- The google sheet where the quotes are maintained : https://docs.google.com/spreadsheets/d/1PbIU9R8N4NF8xAjC81YHqXPQumMo0bNEnzSHMo7K3v4
- The live demo : http://lxnd.pythonanywhere.com/