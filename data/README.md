# Pokemon-Teams-Data

This data model isn't very good, really just trying to focus on frontend with this project.
I decided to make this whole app local and single user so there's no need for a user table.


## Setup
Since there was a lot of playing around with this, see [docs/postgres-odbc.md](docs/postgres-odbc.md)

If I have some extra energy, I might make an automated script for the schema/table creation and database seeding...


## Seeding
I seed the local Postgres database using code located in [seed/](seed/).
This made it easy to retrieve the Pokedex and sprite names.

Its pretty junky, but its only meant to be run once anyway.

