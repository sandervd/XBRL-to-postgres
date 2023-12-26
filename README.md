# Installation 
## Git
https://git-scm.com/download/win

git clone --recurse-submodules https://github.com/sandervd/XBRL-to-postgres.git

## Docker desktop
https://www.docker.com/products/docker-desktop/

docker compose exec arelle python arelleCmdLine.py -f https://filings.xbrl.org/549300ZKLIF7RP6EH823/2022-12-31/ESEF/BE/1/tessenderlogroup-2022-12-31-en.zip -v --plugins "xbrlDB" --store-to-XBRL-DB 'postgres,5432,postgres,password,arelle,10,pgOpenDB'



