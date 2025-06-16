# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Example xrdict_to_outlist family output formatter.

Example output formatter demonstrating receiving a dictionary of xarrays as an
argument, and returning a list of products that were produced. This output family
does not require an an expected list of output filenames in advance.
"""

import logging
from geoips.filenames.base_paths import PATHS as gpaths
from geoips.filenames.base_paths import make_dirs
from pathlib import Path

LOG = logging.getLogger(__name__)

interface = "output_formatters"
family = "xrdict_to_outlist"
name = "example_xrdict_to_outlist_output_formatter"


def call(xarray_dict, variable_name=None):
    """Output multiple arbitary data files."""
    print("output formatter")
    output_path = Path(gpaths["GEOIPS_OUTDIRS"], "outputs")
    make_dirs(output_path)
    dataset_name, variable_name = variable_name.split(":")
    data = xarray_dict[dataset_name][variable_name]
    output_fnames = []
    for ii in range(0, 10):
        output_fname = Path(output_path, f"line_{ii}")
        with open(output_fname, "w") as fobj:
            data_list = data.to_dict()["data"][ii]
            data_str = " ".join([str(jj) for jj in data_list])
            fobj.write(data_str)
        output_fnames += [str(output_fname)]
    return output_fnames
