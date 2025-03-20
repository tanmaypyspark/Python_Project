import subprocess
import importlib.util
import os
os.getcwd()
def get_pip_path():
    """
    Returns the path to the pip executable in the clean_env virtual environment.
    """
    base_path = os.getcwd()
    venv_path = os.path.join(base_path,"clean_env", "Scripts", "pip.exe")
    if os.path.exists(venv_path):
        return venv_path
    else:
        return "pip"  # Fallback to the default pip if clean_env is not found
# print(get_pip_path())
# print(os.getcwd())
def install_missing_modules(modules):
    """
    Installs missing Python modules using pip.

    Args:
        modules: A list of module names (strings).
    """
    pip_path = get_pip_path()
    for module in modules:
        if not is_module_installed(module):
            print(f"Installing {module}...")
            try:
                subprocess.check_call([pip_path, "install", module])
                print(f"{module} installed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {module}: {e}")

def upgrade_modules(modules):
    """
    Upgrades specified Python modules using pip.

    Args:
        modules: A list of module names (strings).
    """
    pip_path = get_pip_path()
    for module in modules:
        print(f"Upgrading {module}...")
        try:
            subprocess.check_call([pip_path, "install", "--upgrade", module])
            print(f"{module} upgraded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error upgrading {module}: {e}")


def is_module_installed(module_name):
  """
  Checks if a Python module is installed.

  Args:
      module_name: The name of the module (string).

  Returns:
      True if the module is installed, False otherwise.
  """
  return importlib.util.find_spec(module_name) is not None

def check_module_installation_path(module_name):
    """
    Prints the installation path of a specific module.

    Args:
        module_name: The name of the module (string).
    """
    try:
        module = importlib.import_module(module_name)
        print(f"{module_name} is installed at: {module.__file__}")
    except ImportError:
        print(f"{module_name} is not installed.")

def preSetupCheck():
    # Example usage:
    required_modules = ["pandas", "selenium", "beautifulsoup4", "bs4", "logging"] #beautifuolsoup4 is the correct name.
    install_missing_modules(required_modules)
    # Modules to upgrade
    modules_to_upgrade = ["certifi"]  # Add other modules here if needed
    upgrade_modules(modules_to_upgrade)
    # Now, you can safely import and use the modules in your main script:
    try:
        import pandas
        import selenium
        from bs4 import BeautifulSoup
        import logging

        print("All modules are available.")
        # Your main script logic here...
        for module in required_modules:
            check_module_installation_path(module)
        return True

    except ImportError as e:
        print(f"Module import error after installation: {e}")
        return False