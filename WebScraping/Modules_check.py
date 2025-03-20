import subprocess
import importlib.util

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
                subprocess.check_call(["pip", "install", module])
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
            subprocess.check_call(["pip", "install", "--upgrade", module])
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
        return True

    except ImportError as e:
        print(f"Module import error after installation: {e}")
        return False