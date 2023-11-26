# Configure ssh_config
$host_config = "~/.ssh/config"

file { $host_config
  ensure  => "present'",
  content => template("host_config.erb")
}
