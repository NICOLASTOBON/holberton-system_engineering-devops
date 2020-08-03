# Using Puppet, create a manifest that kills a process named killmenow.

Exec { 'pkill -f ./killmenow':
  path => '/usr/bin',
}
