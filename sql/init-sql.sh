#!/usr/bin/env bash

mysql -u user -ppassword test < "/docker-entrypoint-initdb.d/tables.sql"
