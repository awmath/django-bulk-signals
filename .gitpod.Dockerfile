FROM docker.io/gitpod/workspace-full:latest

# fix non persistent pip packages: https://github.com/gitpod-io/gitpod/issues/7077
ENV PIP_USER=yes
