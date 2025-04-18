CREATE TABLE Departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    department_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    inventory_count INT NOT NULL DEFAULT 0,
    alert_threshold INT NOT NULL DEFAULT 0,
    UNIQUE(department_id, name),
    FOREIGN KEY (department_id) REFERENCES Departments(id) ON DELETE CASCADE
);
