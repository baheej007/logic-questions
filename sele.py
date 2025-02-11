SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department = departments.id;
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department = departments.id;
