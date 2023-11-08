# automate the issue fix of Apache is returning a 500 error

exec { 'fix_apache_error_config':
        command  => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}
