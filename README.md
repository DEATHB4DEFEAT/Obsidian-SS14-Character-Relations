---
tags:
  - Hidden
creation date: 2024-07-23 22:03
summary: This is meant for people on GitHub, remove this from the web export.
---
# README

## NGINX

If you want to host this or something similar for whatever reason, here's my NGINX config:

```json
// /etc/nginx/sites-enabled/characters

server {
    server_name characters.simplemodbot.tk;

    root /home/death/death-share/Code/character-tree;
    error_page 404 /404.html;

    location = / {
        try_files $uri /home.html;
    }

    location / {
        try_files $uri /404.html;
    }
}
```
