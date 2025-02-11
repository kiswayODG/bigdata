-- Création de la base de données
CREATE DATABASE parisAirBnB;

-- Après avoir créer la BD, se connecter dessus et passer le script

-- Table neighbourhoods
CREATE TABLE neighbourhoods (
    neighbourhood_group VARCHAR(255),
    neighbourhood VARCHAR(255),
    PRIMARY KEY (neighbourhood_group, neighbourhood)
);

-- Table listing
-- Table listing
CREATE TABLE listing (
    id BIGINT PRIMARY KEY,  
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
    FOREIGN KEY (neighbourhood_group, neighbourhood) 
        REFERENCES neighbourhoods(neighbourhood_group, neighbourhood)
        ON DELETE CASCADE
);

-- Table calendar
CREATE TABLE calendar (
    listing_id BIGINT,  
    date DATE,
    available BOOLEAN,
    price DECIMAL(10,2) NULL,
    adjusted_price DECIMAL(10,2) NULL,
    minimum_nights INT,
    maximum_nights INT,
    PRIMARY KEY (listing_id, date),
    FOREIGN KEY (listing_id) REFERENCES listing(id) ON DELETE CASCADE
);

-- Table reviews
CREATE TABLE reviews (
    listing_id BIGINT,  
    id BIGSERIAL PRIMARY KEY,
    date DATE NOT NULL,
    reviewer_id BIGINT NOT NULL,  
    reviewer_name VARCHAR(255),
    comments TEXT,
    FOREIGN KEY (listing_id) REFERENCES listing(id) ON DELETE CASCADE
);

