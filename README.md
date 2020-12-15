# group_distance_calculator

![Python package](https://github.com/dbaumei/group_distance_calculator/workflows/Python%20package/badge.svg)

A tool that reads the addresses of sources and destinations and gives back the least amount of combined travel, either time or distance.

## Getting started

### Installation Requirements

To use this program, install Python 3.8 or higher and pip3 with

```
sudo apt install python3 python3-pip
```

Then, install `pipenv` with

`pip3 install pipenv`

and change to the directory of this repository.

In this directory, run

`pipenv install`

to install all Python modules needed.

### ORS API token

You will also need to obtain an API token for the Openrouteservice (ORS). To do so, [just follow the instructions linked on this page.](https://openrouteservice.org/plans/)
You can also share your API token with others, but be aware that the usage is limited per day and per minute.

To use the token with this application, save it in in the root directory of this repository in a file named `ors.key`.


## Issues

If you encounter any problems, please open an issue.
