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

Installation Guide
==================

This installation guide has installation steps specific to installing the geoips_template_plugin plugin, including
the base geoips conda install if not already installed.

Setup System Environment Variables
----------------------------------

```bash

    # Set up appropriate environment variables for all conda-based geoips_template_plugin setup steps
    # within this geoips_template_plugin README below

    # These steps will need to be copied and pasted into your shell any time you want to run the 
    # setup commands within this README.
    
    # Typical users do not have to make any modifications to the commands
    # within this README, and can copy and paste directly.

    # Once geoips_template_plugin has been installed, the "GEOIPS_CONFIG_FILE" specified below will be
    # sourced when running geoips_template_plugin, and the direct environment variable assignments
    # within this section are no longer required.

    # If you would like to have the GEOIPS_CONFIG_FILE automatically sourced so you do not have to manually run the 
    # source command for every new shell, you can add 
    # source </full/path/to/config/file>
    # to your ~/.bashrc file

    # GEOIPS_REPO_URL should point to the base URL for git clone commands
    export GEOIPS_REPO_URL=https://github.com/NRLMMD-GeoIPS

    # GEOIPS_BASEDIR will contain all source, output, and external dependencies
    # Ensure this is consistently set for all installation / setup steps below
    export GEOIPS_BASEDIR=$HOME/geoproc

    # This config file must be sourced ANY TIME you want to run the geoips geoips_template_plugin plugin
    export GEOIPS_CONFIG_FILE=$GEOIPS_BASEDIR/geoips_packages/geoips_template_plugin/setup/config_plugin

```

Clone geoips_template_plugin git repositories required for setup scripts
-----------------------------------------------------------
```bash
    mkdir -p $GEOIPS_BASEDIR/geoips_packages/

    git clone $GEOIPS_REPO_URL/geoips.git $GEOIPS_BASEDIR/geoips_packages/geoips
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips pull
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips checkout -t origin/dev
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips checkout dev
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips pull

    git clone $GEOIPS_REPO_URL/geoips_template_plugin.git ${GEOIPS_BASEDIR}/geoips_packages/geoips_template_plugin
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_template_plugin pull
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_template_plugin checkout -t origin/dev
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_template_plugin checkout dev
    git -C ${GEOIPS_BASEDIR}/geoips_packages/geoips_template_plugin pull
```

IF REQUIRED: Install and test base geoips conda environment
------------------------------------------------------------
```bash
    # SKIP IF YOU HAVE ALREADY INSTALLED BASE GEOIPS CONDA ENVIRONMENT 
    # This prompts you through all the steps of installing the geoips conda environment from scratch,
    # using the parameters specified above.  This only needs to be done once per system, skip if you
    # already ran this command and successfully installed the geoips conda environment.
    $GEOIPS_BASEDIR/geoips_packages/geoips/base_install_and_test.sh dev
```

Install geoips_template_plugin package
-------------------------
```bash
    $GEOIPS_BASEDIR/geoips_packages/geoips_template_plugin/setup.sh repo_clone

    # Watch out for "GIT PULL FAILED" or "GIT CHECKOUT FAILED" log outputs -
    # those are legitimate failures and must be addressed before continuing
    $GEOIPS_BASEDIR/geoips_packages/geoips_template_plugin/setup.sh repo_update

    source $GEOIPS_CONFIG_FILE
    pip install -e $GEOIPS_BASEDIR/geoips_packages/geoips
    $GEOIPS_BASEDIR/geoips_packages/geoips_template_plugin/setup.sh install
```

Test geoips_template_plugin installation - these test scripts provide you with the full command line calls
---------------------------------------------------------------------------------------------
```bash
    source $GEOIPS_CONFIG_FILE

    # This runs the single ABI test script
    $GEOIPS_PACKAGES_DIR/geoips_template_plugin/tests/scripts/abi_aws.sh

    # This runs EVERY possible functionality test for this repo, and returns 0 if they all pass.
    $GEOIPS_PACKAGES_DIR/geoips_template_plugin/tests/test_all.sh
```

Modify geoips_template_plugin repository for your own geoips plugin
---------------------------------------------------------------------------------------------

Please follow instructions within `README_PLUGIN.md` for modifying template_plugin to create your own
geoips plugin repository.


Create test scripts for your new geoips plugin
---------------------------------------------------------------------------------------------

Please follow instructions  within `tests/README.md` for adding appropriate test scripts to your
new geoips plugin repository.

Valid test scripts are required to ensure functionality operates as expected,
and to provide sample outputs for reference.
