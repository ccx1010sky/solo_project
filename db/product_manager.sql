-- 
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufs;

CREATE TABLE manufs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    info VARCHAR(255)
);


CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  stock_quantity INT,
  cost INT,
  selling_price INT,
  mark_up INT,
  manuf_id INT REFERENCES manufs(id) 
  
);

