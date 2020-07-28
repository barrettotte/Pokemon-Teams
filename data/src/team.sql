-- store teams of 6 pokemon

create table pokemon.team (
  team_id serial,
  label   varchar(64) not null,

  primary key(team_id)
);
