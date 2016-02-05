DROP TABLE ipdata;

CREATE TABLE
    ipdata(
        id serial PRIMARY KEY,
        registry VARCHAR(50) NOT NULL,
        country_code VARCHAR(2),
        network_addr INET NOT NULL,
        cidr INTEGER NOT NULL,
        subnetmask INET NOT NULL,
        addr_cidr INET NOT NULL,
        addr_subnetmask TEXT NOT NULL,        
        count_of_adresses INTEGER,
        status_make_date DATE,
        status VARCHAR(50)
    );

\copy ipdata(registry,country_code,network_addr,cidr,subnetmask,addr_cidr,addr_subnetmask,count_of_adresses,status_make_date,status) FROM ipdata.csv with csv;
