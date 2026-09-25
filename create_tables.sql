CREATE TABLE Places (
    id SERIAL PRIMARY KEY,
    place_name TEXT,
    category TEXT,
    subcategory TEXT,
    location TEXT,
    rating FLOAT,
    estimated_cost_sar INTEGER,
    price_level INTEGER,
    duration_hours_needed FLOAT,
    activity_type TEXT,
    opening_hours TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
