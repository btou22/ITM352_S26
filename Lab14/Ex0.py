import importlib

packages = ["scipy", "statsmodels", "matplotlib"]

for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"{pkg} is installed")
    except ImportError:
        print(f"{pkg} is NOT installed")