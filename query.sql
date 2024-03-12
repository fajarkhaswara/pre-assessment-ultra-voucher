SELECT child.id, child.name, parent.name AS parent_name
FROM data_table child
LEFT JOIN data_table parent ON child.parent_id = parent.id;
