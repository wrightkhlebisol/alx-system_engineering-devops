# Create a tmp file with Puppet

file { '/tmp/school':
    ensure => 'file',
    content => 'I love Puppet',
    mode => '0744',
    owner => 'www-data',
    group => 'www-data',
}
