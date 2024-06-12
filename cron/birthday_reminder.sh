#!/bin/bash

# Activate the virtual environment
source /home/dktshume/virtualenv/dkts/backend/3.11/bin/activate

# Run birthday_reminder script
python /home/dktshume/dkts/backend/cron/birthday_reminder.py
