#!/bin/bash
echo "iniciado servidor dos sensores de temperatura e umidade"
sudo python /home/pi/server_sensor/server_sensor.py &
