# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/* \
             --procflow single_source \
             --reader_name abi_netcdf \
             --resampled_read \
             --product_name Infrared-Test \
             --compare_path "$GEOIPS_PACKAGES_DIR/geoips_plugin_example/tests/outputs/abi_aws/<product>_image" \
             --output_formatter imagery_test \
             --filename_formatter test_fname \
             --sector_list goes_east \

retval=$?

exit $retval
