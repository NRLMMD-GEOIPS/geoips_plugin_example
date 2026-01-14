# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_abi/data/goes16_20200918_1950/* \
    --reader_name abi_netcdf \
    --resampled_read \
    --product_name Infrared-Test \
    --compare_path "$GEOIPS_PACKAGES_DIR/geoips_plugin_example/tests/outputs/abi_aws/<product>_image" \
    --output_formatter imagery_test \
    --filename_formatter test_fname \
    --sector_list goes_east
retval=$?

exit $retval
