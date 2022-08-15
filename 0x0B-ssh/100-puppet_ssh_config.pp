# Set up your client SSH configuration file so that you can connect to a
# server without typing a password

file_line { 'PasswordAuthentication':
    path => '/etc/ssh/ssh_config',
    line => '   PasswordAuthentication no',}

file_line { 'IdentifyFile':
    path => '/etc/ssh/ssh_config',
    line => '   IdentityFile ~/.ssh/school',}
