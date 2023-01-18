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

#!/bin/bash

run_procflow $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/* \
             --procflow single_source \
             --reader_name abi_netcdf \
             --resampled_read \
             --product_name Infrared-Test \
             --compare_path "$GEOIPS_PACKAGES_DIR/geoips_plugin_example/tests/outputs/abi_aws/<product>_image" \
             --output_format imagery_test \
             --filename_format test_fname \
             --sector_list goes16 \
             --sectorfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/static/goes16.yaml
retval=$?

exit $retval
