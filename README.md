# Midi Middle Manager

This is a tool that discretizes midi input so that DefleMask interprets simultaneous keystrokes correctly.

Tested on MacOS 14.4.1. Might work in other environments

## Setup

```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

* Run [Midinous](https://midinous.com) to generate Midi output
* Run this script (`source .venv/bin/activate; python3 ./main.py`)
* Run [DefleMask](https://www.deflemask.com)
* In DefleMask, Options -> Midi Config and listen to the port labeled "mmm"
* In DefleMask, record
