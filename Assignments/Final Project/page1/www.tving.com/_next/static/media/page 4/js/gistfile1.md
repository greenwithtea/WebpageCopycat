Put this into the server's .htaccess file (assuming that it's an Apache):

```
<IfModule mod_headers.c>
  <FilesMatch "\.css$">
    Header set Access-Control-Allow-Origin "*"
  </FilesMatch>
</IfModule>
```
