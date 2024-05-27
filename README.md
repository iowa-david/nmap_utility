# python nmap

nmap is a common port scanning utility that has been made available to use within python using python-nmap

## Description

nmap is often used by pen testers to check what ports are open, there are multiple scripts available within nmap that allow for even more detailed scanning.

Demo: https://www.youtube.com/watch?v=imYT87Sajhc

## Table of Contents

  - Requirements
  - Installation
  - Use
  - Three Main Points
  - Why I am interested
  - Areas of Improvement

## Requirements
  - nmap installed on your machine (many ports are available at https://nmap.org)
  - python3 ( Tested on python 3.10.0)
  - python-nmap installed (pip install python-nmap)

## Installation

Note: Use sudo where necessary

1. Clone the repository

   git clone https://github.com/ac0mm/greta.git

2. Change into the nmap-utility folder

          

## Use

  python3 nmap_utility.py

—set up to check the 1000 most commonly targeted ports and determine what ports are open

## Three Main Points
  - Provide a script to easily identify open ports
  - Provides a wrapper to nmap functionality
  - Offer encrypted and unencrypted means

## Why I am Interested

There are many common tools that are used for penetration testing and viewing the security of a network. Some of these are easier than others, the goal of this project is to leverage Python language to start to dive into common tools and see what can be completed within the tools inside a common scripting language.

## Areas of Improvement

- Ability to run nmap scripts. I attempted to get the scripts to run and many of the previous options no longer work from stack overflow and other resources.

- Menu options to allow for changing the parameters and listing the options of scripts with more detailed information about them to allow for an easier to use nmap experience.

- Integration within a SIEM tool to check information about vulnerabilities over time.

## for more information
[python3-nmap](https://pypi.org/project/python3-nmap/)

[invoking-nmap-nse-from-python](https://stackoverflow.com/questions/4273489/invoking-nmap-nse-from-python)

https://www.redhat.com/sysadmin/nmap-scripting-engine
