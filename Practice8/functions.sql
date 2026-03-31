-- =========================
-- 2. PROCEDURE: INSERT OR UPDATE
-- =========================
CREATE OR REPLACE PROCEDURE insert_or_update(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM numbers WHERE name = p_name) THEN
        UPDATE numbers
        SET num = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO numbers(name, num)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;
-- CALL insert_or_update('Ali', '87001234567');
-- =========================
-- 3. PROCEDURE: INSERT MANY WITH VALIDATION
-- =========================
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    invalid_data TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(p_names, 1)
    LOOP
        IF p_phones[i] ~ '^87[0-9]{9}$' THEN
            INSERT INTO numbers(name, num)
            VALUES (p_names[i], p_phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, p_names[i] || ':' || p_phones[i]);
        END IF;
    END LOOP;

    RAISE NOTICE 'Invalid data: %', invalid_data;
END;
$$;
-- CALL insert_many_users(ARRAY['Ali','Test'], ARRAY['87001234567','123']);
-- =========================
-- 5. PROCEDURE: DELETE USER
-- =========================
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM numbers
    WHERE name = p_value
       OR num = p_value;
END;
$$;
-- CALL delete_user('Ali');