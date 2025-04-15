    # # # This source code is subject to the license referenced at
    # # # https://github.com/NRLMMD-GEOIPS.

GeoIPS Plugin Example
=====================

The geoips_plugin_example package is a GeoIPS-compatible plugin package, intended to serve as
an example for implementing different plugin types (ie, algorithms, filename formats, etc)
within the GeoIPS ecosystem. Please see the
[GeoIPS Documentation](https://github.com/NRLMMD-GEOIPS/geoips#readme)
for more information on the GeoIPS plugin architecture and base infrastructure.

Package Overview
----------------

The geoips_plugin_example plugin package includes duplicated versions of several
basic pieces of functionality originally contained within the main geoips repo,
in order to serve as an example for setting up a plugin package containing a variety of
different plugin types.

This package contains duplicated plugin examples of the following types:

* algorithms
* filename formatters
* output formatters
* interpolators
* colormappers
* product specification

There is a single test script which incorporates all of the modified modules in a single call.

* tests/scripts/abi_aws.sh

This example plugin package is intended to serve as an example, not necessarily as a template.
Template repositories are also available - with the intent to continue adding template repositories
for various use cases.  Please let us know if you have a specific use case you are interested in
implementing which could benefit from a template repo.

System Requirements
---------------------

* geoips >= 1.13.0
* numpy (to build dummy fortran, not currently implemented)
* Test data repos contained in $GEOIPS_TESTDATA_DIR for tests to pass
  (command included below).

IF REQUIRED: Install base geoips package
------------------------------------------------------------
SKIP IF YOU HAVE ALREADY INSTALLED BASE GEOIPS ENVIRONMENT

If GeoIPS Base is not yet installed, follow the
[installation instructions](https://github.com/NRLMMD-GEOIPS/geoips#installation)
within the geoips source repo documentation:

Install geoips_plugin_example package
----------------------------------------

```bash
    # Ensure GeoIPS Python environment is enabled.
    git clone https://github.com/NRLMMD-GEOIPS/geoips_plugin_example.git $GEOIPS_PACKAGES_DIR/geoips_plugin_example
    pip install -e $GEOIPS_PACKAGES_DIR/geoips_plugin_example
```

Test geoips_plugin_example installation
-----------------------------------------
```bash
    # Ensure GeoIPS Python environment is enabled.

    # Install required test datasets
    $GEOIPS_PACKAGES_DIR/geoips/setup/check_system_requirements.sh aws_test_data abi_day_low_memory

    # Run test scripts once test datasets available
    $GEOIPS_PACKAGES_DIR/geoips_plugin_example/tests/test_all.sh
```
