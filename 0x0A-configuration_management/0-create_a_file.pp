file { '/tmp/school':
  content => 'I love puppet',
  owner => 'www-data',
  group => 'www-data',
  mode => '0744'
}
