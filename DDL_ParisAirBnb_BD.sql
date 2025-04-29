-- Création de la base de données
CREATE DATABASE airbnb_paris;

-- Après avoir créer la BD, se connecter dessus et passer le script

-- Table neighbourhoods
CREATE TABLE neighbourhoods (
    neighbourhood_group VARCHAR(255),
    neighbourhood VARCHAR(255),
    PRIMARY KEY (neighbourhood_group, neighbourhood)
);

-- Table listings
CREATE TABLE listings (
    row_id BIGSERIAL PRIMARY KEY,
    id BIGINT NOT NULL,  
    name VARCHAR(255),
    host_id BIGINT NOT NULL,  
    host_name VARCHAR(255),
    neighbourhood_group VARCHAR(255),
    neighbourhood VARCHAR(255),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    room_type VARCHAR(50),
    price DECIMAL(10,2),
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE NULL,
    reviews_per_month DECIMAL(4,2) NULL,
    calculated_host_listings_count INT,
    availability_365 INT,
    number_of_reviews_ltm INT,
    license VARCHAR(255) NULL,
    trimestre INT NOT NULL,
    UNIQUE (id, trimestre),
    FOREIGN KEY (neighbourhood_group, neighbourhood) 
        REFERENCES neighbourhoods(neighbourhood_group, neighbourhood)
        ON DELETE CASCADE
);



-- Table reviews
CREATE TABLE reviews (
    listing_id BIGINT,  
    row_id BIGSERIAL PRIMARY KEY,
    date DATE NOT NULL,
    trimestre INT NOT NULL,
    FOREIGN KEY (listing_id, trimestre) REFERENCES listings(id, trimestre) ON DELETE CASCADE
);

