
### File Directory
The Python interpreter has a built-in sys.path variable, which includes the location of the standard Python code. The environment variable PYTHONPATH is an empty or colon-separated string of direc‐ tory names that tells Python which parent directories to check before sys.path to find the imported modules or packages. So, if you change to your new fastapi direc‐ tory, type this (on Linux or macOS) to ensure that the new code under it will be checked first when importing:

`$ export PYTHONPATH=$PWD/src`
