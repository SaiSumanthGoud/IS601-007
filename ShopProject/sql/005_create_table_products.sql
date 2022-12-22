CREATE TABLE
    IF NOT EXISTS IS601_Products(
        id int auto_increment PRIMARY KEY,
        name VARCHAR(30) unique,
        description TEXT,
        category VARCHAR(50),
        stock int DEFAULT 0,
        unit_price int DEFAULT 99999,
        image TEXT,
        visibility BOOLEAN,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        check (stock >= 0),
        -- don't allow negative stock; I don't allow backorders
        check (unit_price >= 0) -- don't allow negative costs
    )