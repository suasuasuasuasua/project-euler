# Project Euler

## Overview

Solving the problems from [Project Euler](https://projecteuler.net/archives) so
that my brain stops rotting on League of Legends and Elden Ring xd.

I will be using [`devenv`](https://devenv.sh/) to manage the project
dependencies since I'll be programming in multiple languages, namely...

- [`python`](https://www.python.org/)
- [`rust`](https://www.rust-lang.org/)
- ...

Using `nix` to manage the project dependencies will make my life easy as I
develop across different systems.

## Setup

Follow the instructions from [`devenv`](https://devenv.sh/getting-started/)
using the instructions found here.

### Install `nix`

```bash
### Via https://zero-to-nix.com/start/install (recommended)
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install

### Via https://devenv.sh/getting-started/
## Linux
sh <(curl -L https://nixos.org/nix/install) --daemon

## macOS
curl -L https://raw.githubusercontent.com/NixOS/experimental-nix-installer/main/nix-installer.sh | sh -s install

## WSL2
sh <(curl -L https://nixos.org/nix/install) --no-daemon
```

### Install `devenv`

```bash
## General
nix-env -iA devenv -f https://github.com/NixOS/nixpkgs/tarball/nixpkgs-unstable

## NixOS
# Add the following to your configuration.nix somewhere
environment.systemPackages = [ 
  pkgs.devenv
];
```

#### `devenv.nix`

Defines the configuration for the `devenv` shell. This is where we define all
the tooling, packages, scripts, services, processes, etc. that we need for the
project.

#### `devenv.yaml`

The `yaml` defines the sources for all the packages, i.e. where are we getting
the cached builds or build instructions for `nix`.

## Usage

Call `devenv shell` to install all the project dependencies specified in
`./devenv.nix`, then spawn a development shell with all the proper
dependencies set up.
