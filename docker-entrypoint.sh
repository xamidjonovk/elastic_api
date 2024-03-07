#!/bin/sh
# Wait for Elasticsearch to be available
until curl -s http://elasticsearch:9200/; do
    echo "Waiting for Elasticsearch..."
    sleep 1
done

echo "Elasticsearch is up - executing command"
echo "y" | python manage.py search_index --rebuild

exec "$@"
