# Install MariaDB, Nginx, Wordpress, php-fpm roles

Run:
```
ansible-playbook main.yaml
```

To install only one of them use tag:
```
ansible-playbook main.yaml --tags nginx
ansible-playbook main.yaml --tags mariadb
ansible-playbook main.yaml --tags wp
ansible-playbook main.yaml --tags php
```