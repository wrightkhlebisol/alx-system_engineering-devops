# Configure ssh_config
#$ssh_path = '/etc/ssh/sshd_config'

#file_line { 'Turn off passwd auth':
#  path => $ssh_path,
#  line => 'PasswordAuthentication no',
#}

#file_line { 'Declare identity file':
#  path => $ssh_path,
#  line => 'IdentityFile ~/.ssh/school',
#}

$host_config = '/etc/ssh/ssh_config'

file { $host_config:
  ensure  => 'present',
  content => "Host *\n\tPasswordAuthentication no\n\tIdentityFile /root/.ssh/school"
}
