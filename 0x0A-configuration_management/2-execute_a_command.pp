# Kills a process

exec { 'kill_given_process':
    command     => 'pkill -f killmenow',
    refreshonly => true,
    onlyif      => 'pgrep -f killmenow',
    path        => '/usr/bin/:/bin/'
}

