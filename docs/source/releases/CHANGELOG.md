    # # # Distribution Statement A. Approved for public release. Distribution unlimited.
    # # #
    # # # Author:
    # # # Naval Research Laboratory, Marine Meteorology Division
    # # #
    # # # This program is free software: you can redistribute it and/or modify it under
    # # # the terms of the NRLMMD License included with this program. This program is
    # # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
    # # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
    # # # for more details. If you did not receive the license, for more information see:
    # # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

# v1.6.0: 2022-11-28, open source release
## GEOIPS#119: 2022-11-18, simplify README
### Documentation
#### Simplify README and installation
* Remove README_PLUGIN.md - this is no longer serving as a template, merely an example.
* Update README.md to standard contents
    * use links to geoips repo as appropriate
    * Include actual information about the package.
* Remove setup.sh, docs/installation.rst
    * Rely on default setup.py pip install, and geoips installation documentation
* Rename template_plugin_overview.rst and index to geoips_plugin_example
    * Rename documentation files from template_plugin to geoips_plugin_example
```
renamed:    docs/template_plugin_overview.rst -> docs/geoips_plugin_example_overview.rst
renamed:    docs/template_plugin_index.rst -> docs/geoips_plugin_index.rst
deleted:    docs/installation.rst
deleted:    setup.sh
deleted:    README_PLUGIN.md
modified:   docs/geoips_plugin_example_overview.rst
modified:   docs/geoips_plugin_index.rst
modified:   README.md
```


# v1.5.2: 2022-09-22, bug - update ABI AWS path

## GEOIPS#75: 2022-09-16, bug fixes
### Bug fixes
* **tests/scripts/abi_aws.sh**: $GEOIPS/tests/data -> $GEOIPS_TEST_DATA

## GEOIPS#12: 2022-09-21, geoips_template_plugin -> geoips_plugin_example
### Refactor
* Rename repo from geoips_template_plugin -> geoips_plugin_example
* Update all files / directories from geoips_template_plugin -> geoips_plugin_example


# v1.5.1: 2022-07-15, update prefix for distro stmts on \*.md files to spaces

### Documentation Updates
* Update \*.md Distro statement headers to use 4 spaces prefix rather than ### (formatting improvement)


# v1.5.0: 2022-06-09, geoips2->geoips, update GEOIPS\_REPO\_URL

### v1.5.0post1: 2022-06-16, remove NRL specific environment from config\_plugin

#### Bug fixes
* **config_plugin**
    * Remove NRL specific environment

### Refactor
* **config_plugin**
    * Update GEOIPS\_REPO\_URL to github

### Documentation Updates
* **README.md**
    * Update GEOIPS\_REPO\_URL to github

### Bug fixes
* **abi_aws.sh test script**
    * Update sector location to $GEOIPS/tests/sectors/static/goes16.yaml


# v1.4.7: 2022-05-06, template\_plugin->geoips\_template\_plugin, update/clarify README
### Improvements
* Replace all instances of template_plugin with geoips_template_plugin
* Separate installation and test instructions from template modification instructions.
    * README.md - installation and test
    * README_PLUGIN.md - directions for creating a new plugin repo
* Add references to README_PLUGIN.md and tests/README.md to README.md
    * Direct developers to additional information on creating a new plugin repo, and creating test scripts.

### Bug fixes
* Remove $ from export GEOIPS_REPO_URL


# v1.4.5: 2022-03-18, compare_paths->compare_path, setup_template_plugin.sh->setup.sh

### Refactor
* Replace compare_paths with compare_path in test scripts
    * abi_aws.sh Infrared-Test single_source
* Rename setup_template_plugin.sh -> setup.sh, install_template_plugin -> install
    * Support setup.sh install if setup_template_plugin.sh does not exist.

### Documentation Updates
* Adding basic template_plugin documentation
    * Style templates
        * layout.html
        * style.css
    * Standard documentation content
        * template_plugin_index.rst
        * template_plugin_overview.rst
        * installation.rst


# v1.4.2: 2022-02-05, Add --resampled_read to ABI single_source test script

### Refactor
    * Add --resampled_read to ABI single_source test script call


# v1.3.0: 2021-11-25, remove "sat ops" from base\_paths

### Breaking Interface Changes
    * GEOIPSFINAL-\>ANNOTATED\_IMAGERY\_PATH
        * test_fname.py


# v1.2.5: 2021-11-18, updated to standard interfaces

### Improvements
    * Updated all modules to comply with standard interfaces, to pass test_interfaces.py
        * output.py (imagery_test call signature)


# v1.2.4: 2021-11-12, 89H->Infrared for template product

### Improvements
    * Replaced 89H template product with ABI Infrared test product
        * Data available via NOAA AWS
        * Use static sector rather than TC to simplify output
    * Include template config_plugin for reference
    * Simplify README.md installation and testing steps


# v1.2.3: 2021-11-05, simplified test script

### Improvements
    * Removed old testing construct
    * Simplified test script includes an explicit command line call with a valid return code
        * amsr2.sh


# v1.2.2: 2021-10-25, README clarification, bug fixes in setup/test scripts

### Improvements
    * Clarify README for using template_plugin to create new functionality

### Bug fixes
    * Correct typo in test script, metoctiff -> template_plugin for path to test modules
    * install_offline_cartopy data -> install_cartopy_offlinedata for consistency in setup


# v1.2.1: 2021-10-05, Test repo output updates, and code refactor/simplification

### Breaking Test Repo Updates
    * Updated cartopy to 0.20.0 and matplotlib to v3.4.3
        * test repo outputs incompatible with matplotlib < 3.4.0 and cartopy < 0.19.0
        * Older versions have figures that are very slightly shifted from later versions
        * Exclusively a qualitative difference, but it *does* cause the test comparisons to fail

### Major New Functionality
    * Added exhaustive "test_all.sh" script with successful 0 return.
        * Input data stored within standard test_data_<sensor> repos, test outputs stored within template_plugin repo
    * Including standard plugin functionality, and standard README/setup/test functionality to use as a template
      for future products.  All template functionality duplicates those found in geoips, but with slightly
      modified names (ie geoips_fname -> test_fname). Tests are fully functional, complete with output products
      for full testing.
        * algorithm example
        * filename_format example
        * interpolation example
        * output_format example
        * user_colormap example

### Improvements
    * Standardized and formalized the README, setup script, and test script format for all plugin repos
    * Removed requirement to link test scripts from plugin repos into the main geoips test directory
