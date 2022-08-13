# create a manifest that kills a process named killmenow

exec { 'killmenow':
  path    => '/usr/bin/pkill killmenow',
}
