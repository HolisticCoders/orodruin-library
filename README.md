# Orodruin Library
A Node library for Orodruin

# Installation.
- Clone this repository anywhere you want
- Register the library. This can be done in one of two ways:
  - For a permanent installation add the path to this repository to the environment variable `ORODRUIN_LIBRARIES`.
  - For a temporary one, run the following bit of code in a python environment where `orodruin` is installed.
    ```python
    from orodruin.core import LibraryManager
    from pathlib import Path
    
    LibraryManager.register_library(Path("/path/to/orodruin-library"))
    ```

