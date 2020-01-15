pgloader load
psql postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME} < migrations/001_fix_primary_keys.sql