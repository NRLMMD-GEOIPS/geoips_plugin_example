# This file is a template, and might need editing before it works on your project.

# This Dockerfile uses a multistage build
#
# In the first stage, named "pygcc" we install gcc/gfortran, then remove the 
# apt-get cache. We then use the resulting layer twice.
#
# First, we start from `pygcc`, then copy in our package, install numpy, and build
# our package. This leaves extra stuff, like the package source, behind.
#
# Second, to create the smallest possible image we restart from `pygcc`, then copy
# Python's site-packages directory into the new stage. This leaves everything extra
# behind.

# For questions, contact jeremy.solbrig@colostate.edu


# Start from the slim python image and install gfortran, then clean up the apt-get cache
FROM python:3.6-slim as pygcc

RUN apt-get update -y && \
    apt-get install -y gfortran && \
    # Clean up the apt-get cacue
    rm -rf /var/lib/apt/lists/*

# Multistage build
# Use the pygcc stage to build the algorithm package
FROM pygcc as install

ARG RUN_TESTS=false
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN if [ "${RUN_TESTS}" = true ]; then \
        pip install numpy pytest pytest-coverage && \
        pip install -e . && \
        pytest --cov=default_package ; \
    else \
        pip install --no-cache numpy && \
        pip install --no-cache . ; \
    fi

# FROM pygcc as install
# 
# WORKDIR /usr/src/app
# COPY . /usr/src/app
# 
# RUN pip install --no-cache numpy && \
#     pip install --no-cache .

# Start again from the pygcc stage and copy in the python packages
# This ensure that we have all of the GCC libraries that we need
# as well as the python packages, but that we remove anything extra
# like the original source code
FROM pygcc
COPY --from=install /usr/local/lib/python3.6/site-packages/ \
    /usr/local/lib/python3.6/site-packages/
