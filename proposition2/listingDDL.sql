CREATE TABLE listings (
    row_id BIGSERIAL PRIMARY KEY,
    neighbourhood_cleansed TEXT,
    host_has_profile BOOLEAN,
    host_verifications BOOLEAN,
    host_is_superhost BOOLEAN,
    host_since DATE,
    host_response_time TEXT,
    host_response_rate TEXT,
    calculated_host_listings_count INTEGER,
    property_type TEXT,
    room_type TEXT,
    accommodates INTEGER,
    bedrooms NUMERIC,
    beds NUMERIC,
    cancellation_policy TEXT,
    minimum_nights INTEGER,
    maximum_nights INTEGER,
    has_availability BOOLEAN,
    availability_30 INTEGER,
    availability_60 INTEGER,
    availability_90 INTEGER,
    availability_365 INTEGER,
    number_of_reviews INTEGER,
    reviews_per_month NUMERIC,
    first_review DATE,
    last_review DATE,
    review_scores_rating NUMERIC,
    review_scores_accuracy NUMERIC,
    review_scores_cleanliness NUMERIC,
    review_scores_checkin NUMERIC,
    review_scores_communication NUMERIC,
    review_scores_location NUMERIC,
    review_scores_value NUMERIC,
    amenities TEXT[],
    price NUMERIC
);



CREATE TABLE amenities (
    id SERIAL PRIMARY KEY,
    amenity TEXT UNIQUE NOT NULL
);

CREATE TABLE neighbourhoods (
    id SERIAL PRIMARY KEY,
    neighbourhood_cleansed VARCHAR(255) NOT NULL
);

CREATE TABLE room_types (
    id SERIAL PRIMARY KEY,
    room_type VARCHAR(255) NOT NULL
);

CREATE TABLE property_types (
    id SERIAL PRIMARY KEY,
    property_type VARCHAR(255) NOT NULL
);

CREATE TABLE host_response_times (
    id SERIAL PRIMARY KEY,
    host_response_time VARCHAR(255) NOT NULL
);
