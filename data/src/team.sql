-- teams of pokemon

create table pokemon.team (
  team_id serial,
  label   varchar(128) not null,

  primary key(team_id)
);
