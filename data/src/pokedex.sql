-- table for matching pokedex numbers to names

create table pokemon.pokedex (
  dex_id serial,
  dexno  int not null,
  name   varchar(12) not null,

  primary key(dex_id)
);
