#### # # Distribution Statement A. Approved for public release. Distribution unlimited.
#### # # 
#### # # Author:
#### # # Naval Research Laboratory, Marine Meteorology Division
#### # # 
#### # # This program is free software:
#### # # you can redistribute it and/or modify it under the terms
#### # # of the NRLMMD License included with this program.
#### # # 
#### # # If you did not receive the license, see
#### # # https://github.com/U-S-NRL-Marine-Meteorology-Division/
#### # # for more information.
#### # # 
#### # # This program is distributed WITHOUT ANY WARRANTY;
#### # # without even the implied warranty of MERCHANTABILITY
#### # # or FITNESS FOR A PARTICULAR PURPOSE.
#### # # See the included license for more details.

# geoips_template_plugin installation and test

Please see README.md for installation and testing instructions for the geoips_template_plugin repository as-is
(prior to making any modifications for implementing your own functionality).

Once you have successfully installed and tested geoips_template_plugin repository, proceed to making modifications
for your own purposes.

# Repository Template for new Python-based GeoIPS Algorithms

This is a template that provides the base set of files for a new Python-based GeoIPS plugin.
Note that the files from the template are copied over verbatim,
and must be edited to work for any real algorithm.

## Usage

If you're on GitLab, just select this template when you're creating a new repository.
If you're on something other than GitLab, maybe this can be used natively, but if not,
just clone the repository without history, then push it to your Git server.
Something like this:

```
git clone <this repository> --depth 0
...
Create a repository on your git server
...
git remote add origin <repository URL>
git push -u origin master
```

Once that is done, you can start making changes.

1. `LICENSE` Update as needed / appropriate
2. `geoips_template_plugin/`: Change the `geoips_template_plugin/` directory to the name of your package.
3. `setup.sh`: setup script to support non-pip-installable dependencies.
    * Update appropriately for your package requirments (possibly no changes required)
    * If setup.sh not required, setup.py will be used for pip-based installation
4. `VERSION`: Set VERSION number for this package - if tied closely to geoips, track geoips versions as appropriate
5. `setup.py` Update to reflect the new package name and any installation requirements or entry points.
                Entry points are linked to `geoips_template_plugin/interface_modules` packages/modules
6. `geoips_template_plugin/interface_modules` Update for functionality you require in this plugin.
7. `geoips_template_plugin/yaml_configs` Update for functionality you require in this plugin.
8. OPTIONAL `geoips_template_plugin/default_algorithm.py` Example code importing from pre-compiled binaries
        If required, update to reflect the name of the algorithm and add the algorithm code.
        Create additional new files, directories, or anything else you need.
        You can safely delete this file if no "helper" functions and modules are needed.
9. `__init__.py` Add any top level imports you might need in `__init__.py`
10. `tests/`
```
        * `pytest` Update unit tests for code validation
        * `test_all.sh` Update for full functionality tests for your package (calls all pytests and tests/scripts/*.sh)
        * `tests/scripts/*.sh` Include test scripts to exhaustively test ALL functionality included within repository
        * `tests/outputs` Remove current "outputs" and update with your "correct" output.
                            run_procflow will create an "outputs" directory with scripts to update with current output.
                            These outputs are used for test comparisons, to ensure correct functionality.
```
11. README.md include a description of your algorithm, and detailed installation instructions (see template below).
        Probably start by doing a search and replace for "geoips_template_plugin" -> "my_package_name" within
        the geoips_template_plugin README.md, then update with additional specifics for your package.
12. REMOVE README_PLUGIN.md This file is not needed for geoips plugins - it is for reference only when developing
        a new plugin.

## Files that should be okay as-is

The following files should work correctly with no modifications (and they will not hurt anything if you are not
using Docker or GitLab)

- `Dockerfile`
- `.gitignore`
- `.gitlab-ci.yml`
