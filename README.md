# Pokemon-Teams

An introductory VueJS app to record Pokemon teams used across various games and/or playthroughs.


![Teams](https://raw.githubusercontent.com/barrettotte/Pokemon-Teams/master/docs/screenshots/home.png?token=ADXGMX3F3M4EAXKFQ6KMJZS7HHQRU)
More screenshots located in [docs/screenshots](https://github.com/barrettotte/Pokemon-Teams/tree/master/docs/screenshots)




## Project Goals
* Introductory Vue Project
* Routing with vue-router
* CRUD functionality
* Call an API with Axios
* State management with vuex
* Simple Python backend (Flask) with local Postgres DB on Pi

This was made to mess around with VueJS and is obviously not a production level application.
For sake of simplicity, this runs locally for a single user.
I did not deploy it anywhere, but I took a couple screenshots so I could remember what it looked like myself.

I also got kind of bored of the project towards the end. So, I cut some stuff out...see below.


## Credit
* The sprite images are © Nintendo/Creatures Inc./GAME FREAK Inc.
* [PokeSprite Project](https://github.com/msikma/pokesprite)
* [GitHub Corners](https://github.com/tholman/github-corners)


## Setup
I wouldn't suggest setting this up.
But, I did take some notes in [docs/](docs/), [app/](app/), [api/](api/), and [data/](data/)**.

* Setup environment file at **/dev.env** based on **/dev.env.example**


| Port | Description | Docker ? |
| ---- | ----------- | -------- |
| 5432 | Postgres    | No       |
| 8020 | Flask API   | Yes      |
| 8021 | Vue App     | Yes      |


## Missing Features
Features that I ended up leaving out because I got bored with the project.

* Display random team on home page
* Popup alerts for deleting, creating, etc.
* Alternate sprite forms - Regional variants, type variants, etc.
* Full modal for team member (missing sprite preview, sprite form, etc.)
* Pokemon lookup by name in team member modal
* Form validation within modal
* Better styling...lol
* There's most definitely some UI bugs I missed
* Docker for frontend
* Docker compose


## References
* VueJS Guide - https://vuejs.org/v2/guide
* VueJS API - https://vuejs.org/v2/api/
* VueJS Config - https://cli.vuejs.org/config/
* Bootstrap-Vue Components - https://bootstrap-vue.org/docs/components
