 | # # # Distribution Statement A. Approved for public release. Distribution unlimited.
 | # # #
 | # # # Author:
 | # # # Naval Research Laboratory, Marine Meteorology Division
 | # # #
 | # # # This program is free software: you can redistribute it and/or modify it under
 | # # # the terms of the NRLMMD License included with this program. This program is
 | # # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
 | # # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
 | # # # for more details. If you did not receive the license, for more information see:
 | # # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

GeoIPS 2.0 Overview
===================

Please see GeoIPS 2.0 Documentation Overview for high level information on the plugin infrastructure.


geoips_plugin_example Repository
==================================

This repository provides a working example of GeoIPS 2.0 plugin functionality.

It includes the following examples of Python plugins:

* filename_formats
    * test_fname: identical to "geoips_fname" in geoips repository, but renamed "test_fname"
* output_formats
    * imagery_test: identical to "imagery_clean" in geoips repository, but renamed "imagery_test"
* algorithms
    * single_channel_test: identical to "single_channel" in geoips repository, but renamed "single_channel_test"
* interpolation
    * interp_gauss_test: identical to "interp_gauss" in geoips repository, but renamed "interp_gauss_test"
* user_colormaps
    * Infrared_Test: identical to "Infrared" in geoips repository, but renamed "Infrared_Test"

It includes the following examples of YAML product parameter plugins:

* geoips_plugin_example/yaml_configs/product_inputs/abi.yaml
    * Infrared-Test product using variables B14BT
    * Functionality included in geoips_plugin_example abi.yaml product input is appended to functionality in all other repos
* geoips_plugin_example/yaml_configs/product_params/visir/Infrared-Test.yaml
    * Infrared-Test product parameters identical to Infrared product parameters in geoips repository
    * Infrared-Test product accessible via the "Infrared-Test" product name either command line
        or within a YAML output configuration file.


Creating your own plugin repository
===================================

This geoips_plugin_example can be used as a reference for how different aspects of the geoips plugin infrastructure
can be implemented.  There are separate "template" plugin package repositories that can be used to actually
create a new plugin package from scratch.  Please see GeoIPS documentation for additional information on
plugin development and template repositories.
