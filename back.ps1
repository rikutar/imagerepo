# Backup
Write-Host "Loading functions"

function backup() 
{
    docker exec $args[0] /usr/bin/mysqldump -u root --password=root $args[1] > backup.sql
    Write-Host "Database has been stored to backup.sql"
}

# Restore
function restore() {
    cat backup.sql | docker exec -i args[0] /usr/bin/mysql -u root --password=root args[1]
}
