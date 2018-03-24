#!/bin/bash

#write out current crontab
sudo crontab -l > mycron

#echo new cron into cron file
sudo echo "*/1 * * * * /usr/bin/python $(pwd)/run_task.py >> $(pwd)/run_task.log" >> mycron

#install new cron file
sudo crontab mycron
sudo rm mycron
