-- it is getting abit tougher now
-- we are displaying the tables of arg 1 of script
if [ $# -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi
database="$1"
mysql -e "USE $database; SHOW TABLES;"
