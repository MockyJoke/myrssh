#!/bin/bash

#write out current crontab
crontab -l > mycron

#echo new cron into cron file
echo "*/1 * * * * /usr/bin/python $(pwd)/run_task.py > $(pwd)/run_task.log" >> mycron

#install new cron file
crontab mycron
rm mycron
