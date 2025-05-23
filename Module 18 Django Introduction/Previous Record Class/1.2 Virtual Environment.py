# --------------------------------------------
# How Does a Virtual Environment Work in Python?
# --------------------------------------------


# Step 1: Installing virtualenv
# This installs the virtualenv package using pip.
# It allows you to create isolated Python environments.
# Run this command in your terminal or command prompt:
####     $ pip install virtualenv


# Step 2: Test your installation
# This checks if virtualenv was installed correctly by printing its version.
####     $ virtualenv --version


# Step 3: Create and name your virtual environment
# This command creates a new virtual environment named 'my_env'.
# You can change 'my_env' to any name you prefer.
####    $ virtualenv my_env


# Step 4: Activate the virtual environment
# This step enables the virtual environment so that you can install packages inside it.
# On Windows, use:
####   $ source ./my_env/Scripts/activate



# Step 5: Deactivate the virtual environment
# When you're done working, deactivate the environment to return to the system Python.
####    $ deactivate


# ✅ Note:
# A virtual environment is useful for managing dependencies and avoiding conflicts between different Python projects.
# It creates a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.

