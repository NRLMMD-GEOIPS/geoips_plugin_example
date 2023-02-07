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

GeoIPS Plugin Example
==========================

The geoips_plugin_example package is a GeoIPS-compatible plugin package, intended to serve as
an example for implementing different plugin types (ie, algorithms, filename formats, etc)
within the GeoIPS ecosystem. Please see the 
[GeoIPS Documentation](https://github.com/NRLMMD-GEOIPS/geoips/blob/main/README.md)
for more information on the GeoIPS plugin architecture and base infrastructure.

Package Overview
-----------------

The geoips_plugin_example plugin package includes duplicated versions of several
basic pieces of functionality originally contained within the main geoips repo,
in order to serve as an example for setting up a plugin package containing a variety of
different plugin types.

This package contains duplicated plugin examples of the following types:

* algorithms
* filename formats
* output formats
* interpolation routines
* colormaps
* product specification

There is a single test script which incorporates all of the modified modules in a single call.

* tests/scripts/abi_aws.sh

This example plugin package is intended to serve as an example, not necessarily as a template.
Template repositories are also available - with the intent to continue adding template repositories
for various use cases.  Please let us know if you have a specific use case you are interested in
implementing which could benefit from a template repo.

System Requirements
---------------------

* geoips >= 1.5.3
* numpy (to build dummy fortran)
* Test data repos contained in $GEOIPS_TESTDATA_DIR for tests to pass.

IF REQUIRED: Install base geoips package
------------------------------------------------------------
SKIP IF YOU HAVE ALREADY INSTALLED BASE GEOIPS ENVIRONMENT 

If GeoIPS Base is not yet installed, follow the
[installation instructions](https://github.com/NRLMMD-GEOIPS/geoips/blob/main/docs/installation.rst)
within the geoips source repo documentation:

Install geoips_template_plugin package
----------------------------------------
```bash
    # Assuming you followed the fully supported installation,
    # using $GEOIPS_PACKAGES_DIR and $GEOIPS_CONFIG_FILE:
    source $GEOIPS_CONFIG_FILE
    git clone https://github.com/NRLMMD-GEOIPS/geoips_plugin_example $GEOIPS_PACKAGES_DIR/geoips_plugin_example
    pip install -e $GEOIPS_PACKAGES_DIR/geoips_plugin_example
```

Test geoips_plugin_example installation
-----------------------------------------
```bash
    # Assuming you followed the fully supported installation,
    # using $GEOIPS_PACKAGES_DIR and $GEOIPS_CONFIG_FILE:
    source $GEOIPS_CONFIG_FILE
    $GEOIPS_PACKAGES_DIR/geoips_plugin_example/tests/test_all.sh
```
