#!/bin/bash
addgroup $1
chown $USER:$1 $2
chmod g+rx $2
