#!/bin/bash
#cURL body size
curl -so /dev/null -w '%{size_download}\n' "$1"
