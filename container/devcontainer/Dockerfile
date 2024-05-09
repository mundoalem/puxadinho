# ######################################################################################################################
# LICENSE
# ######################################################################################################################

#
# This file is part of skibidi.
#
# The skibidi is free software: you can redistribute it and/or modify it under the terms of the GNU Affero
# General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# The skibidi is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License along with skibidi. If not, see
# <https://www.gnu.org/licenses/>.
#

# ######################################################################################################################
# PRELUDE
# ######################################################################################################################

#
# CHECKOV
#

# This is a container intended to be used as a remote development environment, we want to allow the user the ability to
# become root
#checkov:skip=CKV2_DOCKER_1:Ensure that sudo isn't used
#checkov:skip=CKV_DOCKER_7:Ensure the base image uses a non latest version tag

# ----------------------------------------------------------------------------------------------------------------------
# BASE IMAGE
# ----------------------------------------------------------------------------------------------------------------------

FROM mundoalem/devcontainer:latest

# ----------------------------------------------------------------------------------------------------------------------
# ARGUMENTS
# ----------------------------------------------------------------------------------------------------------------------

#
# DOCKER BUILDKIT
#

ARG BUILDARCH
ARG BUILDOS
ARG BUILDPLATFORM
ARG TARGETARCH
ARG TARGETOS
ARG TARGETPLATFORM

#
# PROJECT
#

ARG PROJECT_BUILD_DATE
ARG PROJECT_COMMIT
ARG PROJECT_VERSION

# ######################################################################################################################
# SETUP: BASE
# ######################################################################################################################

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

# ----------------------------------------------------------------------------------------------------------------------
# INSTALL SYSTEM PACKAGES
# ----------------------------------------------------------------------------------------------------------------------

RUN export DEBIAN_FRONTEND="noninteractive" \
    && apt-get update \
    && apt-get -y install --no-install-recommends \
    bats \
    bats-assert \
    bats-file \
    bats-support \
    build-essential \
    && apt-get autoremove -y \
    && apt-get clean autoclean -y \
    && rm -r /var/cache/* /var/lib/apt/lists/*

# ######################################################################################################################
# SETUP: CUSTOM (AS DEV USER)
# ######################################################################################################################

USER dev

#
# ENV
#

ENV HOME="/home/dev"

# ----------------------------------------------------------------------------------------------------------------------
# INSTALL PYTHON
# ----------------------------------------------------------------------------------------------------------------------

#
# ENV
#

#
#
#

COPY .python-version .

RUN pyenv update && \
    pyenv install

# ######################################################################################################################
# RUN
# ######################################################################################################################

#
# Empty
#

# ----------------------------------------------------------------------------------------------------------------------
# HEALTHCHECK
# ----------------------------------------------------------------------------------------------------------------------

HEALTHCHECK NONE

# ----------------------------------------------------------------------------------------------------------------------
# ENTRYPOINT
# ----------------------------------------------------------------------------------------------------------------------

ENTRYPOINT [ ]

# ----------------------------------------------------------------------------------------------------------------------
# COMMAND
# ----------------------------------------------------------------------------------------------------------------------

CMD [ ]
