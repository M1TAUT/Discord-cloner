#!/bin/bash

BREAK_SYS=""
pip install --help 2>/dev/null | grep -q break-system-packages && BREAK_SYS="--break-system-packages"

pip install $BREAK_SYS discord.py-self colorama audioop-lts
