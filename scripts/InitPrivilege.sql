use mysql;
update user set host = '%' where user = 'root';
update user set plugin = 'mysql_native_password' where user = 'root';
flush privileges;
