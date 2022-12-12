# Kills a proccess named `killmenow`

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => shell,
  path     => '/usr/bin/',
}
