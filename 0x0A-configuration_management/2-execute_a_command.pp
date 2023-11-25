# Kills a process

exec { 'kill_given_process':
    command     => '/usr/bin/pkill -f killmenow',
    refreshonly => true,
    onlyif      => '/usr/bin/pgrep -f killmenow',
}

