# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Example xarray_dict_to_xarray_dict algorithm plugin.

This example plugin demonstrates an algorithm receiving a dictionary of xarrays as
input, and returning a dictionary of xarrays.
"""

import logging
from typing import Any, Dict

LOG = logging.getLogger(__name__)

interface = "algorithms"
family = "xarray_dict_to_xarray_dict"
name = "example_xarray_dict_to_xarray_dict_algorithm"


def call(
    xarray_dict: Dict[str, Dict[str, Any]],
    input_variable_name: str = None,
    output_variable_name: str = None,
    extra: str = None,
):
    """xarray_dict_to_xarray_dict algorithm plugin."""
    # Pull dataset name and variable name out of variable specification
    input_dataset_name, input_variable_name = input_variable_name.split(":")
    output_dataset_name, output_variable_name = output_variable_name.split(":")
    xarray_dict[output_dataset_name][output_variable_name] = (
        xarray_dict[input_dataset_name][input_variable_name] * 2
    )
    print("algorithm")
    return xarray_dict
