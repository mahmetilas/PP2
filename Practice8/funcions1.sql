-- CREATE TABLE IF NOT EXISTS numbers (
--     name TEXT,
--     num TEXT
-- );

-- =========================
-- 1. FUNCTION: SEARCH PATTERN
-- =========================
CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(name VARCHAR(255), num VARCHAR(30))
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT n.name, n.num
    FROM numbers n
    WHERE n.name ILIKE '%' || pattern || '%'
       OR n.num ILIKE '%' || pattern || '%';
END;
$$;
-- SELECT * FROM search_pattern('ali');
-- =========================
-- 4. FUNCTION: PAGINATION
-- =========================
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE(name VARCHAR(255), num VARCHAR(30))
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT n.name, n.num
    FROM numbers n
    ORDER BY n.name
    LIMIT p_limit
    OFFSET p_offset;
END;
$$;
-- SELECT * FROM get_contacts_paginated(5, 0);