# Kills a process

exec { 'kill_given_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
}

