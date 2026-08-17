[pytest]
DJANGO_SETTINGS_MODULE = blogicum.settings
pythonpath = .
norecursedirs = env/* venv/*
addopts = -vv -p no:cacheprovider --disable-warnings
testpaths = tests/
python_files = test_*.py
django_find_project = false
