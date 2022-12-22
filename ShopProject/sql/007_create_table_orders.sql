CREATE TABLE
    IF NOT EXISTS IS601_S_Orders(
        id int AUTO_INCREMENT PRIMARY KEY,
        total_price int,
        address VARCHAR(100),
        payment_method VARCHAR(30),
        money_received int,
        first_name  VARCHAR(60),
        last_name  VARCHAR(60),
        user_id int,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )