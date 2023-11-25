# Kills a process

exec { 'kill_given_process':
    command  => 'pkill -f killmenow',
}

