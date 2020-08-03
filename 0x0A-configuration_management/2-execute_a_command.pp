# Using Puppet, create a manifest that kills a process named killmenow.

Exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f ./killmenow',
}
