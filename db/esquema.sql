
CREATE TABLE sabespRepresa(
  dataBusca date primary key not null,
  jsonData text not null
);

-- para criar o banco 
-- $sqlite3 sabesp.db < esquema.sql
-- nao e bom que o banco e tabelas tenham nomes iguais
