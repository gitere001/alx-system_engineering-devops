# installs nginx with custom http header

exec {'update':
	provider => shell,
	command => 'sudo apt-get -y update',
	before => Exec['install nginx'],
}

exec {'install Nginx':
	provider => shell,
	command => 'sudo apt-get -y install nginx',
	before => Exec['add_custom_header'],

}

# add custom HTTP header
exec { 'add_custom_header':
  provider => shell,
  command  => 'sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
  before   => Exec['test_nginx_config'],
}

# Test Nginx configuration for errors
exec { 'test_nginx_config':
  provider => shell,
  command  => 'sudo nginx -t',
  before   => Exec['restart_nginx'],
}

# Restart Nginx to apply the configuration changes
exec { 'restart_nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
