# Increase the ULIMIT in order to increase the amount of traffic an Nginx server can handle

exec { 'change_default_ulimit':
  command  => 'sed -i "s/15/2000/" /etc/default/nginx',
  provider => 'shell',
  notify   => Exec['restart_nginx_service']
}

exec { 'restart_nginx_service':
  command     => 'sudo service nginx restart',
  provider    => 'shell',
  refreshonly => true
}
