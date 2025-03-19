#!/bin/sh

waitress-serve --listen=0.0.0.0:8000 --call link_sharing_app:create_app
