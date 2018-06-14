SOURCE_IP=$1
DESTINATION_IP=127.0.0.1:9200

echo "Deleting all indexes from local elastic search If present"

curl -XDELETE $DESTINATION_IP/*

echo "Exporting data from $1"
echo "indexes given as input  $2"

IFS=',' read -r -a indexes <<< "$2"

for index_name in "${indexes[@]}"
do
    echo "working on $index_name"
    # elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=analyzer
    # elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=mapping
    elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=data

done