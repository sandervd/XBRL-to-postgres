FROM arelle
FROM postgres:latest


COPY --from=arelle /usr/src/app/arelle/plugin/xbrlDB/sql/open/xbrlOpenPostgresDB.ddl /docker-entrypoint-initdb.d/01-xbrlOpenPostgresDB.sql
