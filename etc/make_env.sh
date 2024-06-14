#!/bin/sh

echo "TZ=Asia/Almaty" > ../.denv
echo "DEBUG=off" >> ../.denv

echo "POSTGRES_PASSWORD=$1" >> ../.denv
echo "POSTGRES_USER=$2" >> ../.denv
echo "POSTGRES_DB=$3" >> ../.denv
echo "POSTGRES_HOST=$4" >> ../.denv
#echo "SECRET_KEY=$5" >> ../.denv

echo "APP_INSTANCE=$5" >> ../.denv

echo "BOT_API_KEY=$6" >> ../.denv
echo "BOT_CHAT_ID=$7" >> ../.denv

echo "DOMAINS=neotelecom.kg" >> ../.denv
echo "TOS=--agree-tos" >> ../.denv
echo "EMAIL=it@neotelecom.kg" >> ../.denv
