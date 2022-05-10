SELECT id, 'Root' as type
FROM Tree
WHERE p_id IS NULL

UNION

SELECT id, 'Inner' as type
FROM Tree
WHERE p_id IS NOT NULL AND id IN (
    SELECT DISTINCT p_id FROM Tree
)

UNION

SELECT id, 'Leaf' as type
FROM Tree
WHERE id NOT IN ( # если нода чей-то парент, то отбрасываем её
    SELECT p_id
    FROM Tree
    WHERE p_id IS NOT NULL
) AND id NOT IN ( # если нода рут, тоже отбрасываем
    SELECT id
    FROM Tree
    WHERE p_id IS NULL
)