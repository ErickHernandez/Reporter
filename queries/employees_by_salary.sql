SELECT e.`id`, e.`name` employee_name, e.`position` employee_position, e.`salary`
FROM employee e
WHERE e.`salary` >= 150000;