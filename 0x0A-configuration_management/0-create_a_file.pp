# A Puppet manifest that create a file in /tmp

file { 'school':
  ensure  => file,
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}

