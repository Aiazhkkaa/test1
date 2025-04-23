DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE table_name = 'phonebook' AND constraint_type = 'UNIQUE' AND constraint_name = 'unique_name'
    ) THEN
        ALTER TABLE phonebook ADD CONSTRAINT unique_name UNIQUE(name);
    END IF;
END
$$;