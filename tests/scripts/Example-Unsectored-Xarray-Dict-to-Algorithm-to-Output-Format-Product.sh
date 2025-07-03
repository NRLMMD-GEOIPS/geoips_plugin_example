# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_sar/data/STAR_SAR_20230208221222_SH112023_11S_FIX_3km.nc \
    --procflow single_source \
    --reader_name sar_winds_netcdf \
    --product_name Example-Unsectored-Xarray-Dict-to-Algorithm-to-Output-Format-Product \
    --output_formatter example_xrdict_to_outlist_output_formatter \
    --output_formatter_kwargs '{"variable_name": "WINDSPEED:double_wind_speed"}' \
    --filename_formatter geoips_fname \
    --compare_path $GEOIPS_PACKAGES_DIR/geoips_plugin_example/tests/outputs/Example-Unsectored-Xarray-Dict-to-Algorithm-to-Output-Format-Product/ \
    --minimum_coverage 0 \
    --no_presectoring
ss_retval=$?

exit $((ss_retval))
