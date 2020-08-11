# Pokemon-Teams

An introductory VueJS app to record Pokemon teams used across various games and/or playthroughs.


## Project Goals
* Introductory Vue Project
* Routing with vue-router
* CRUD functionality
* Call an API with Axios
* State management with vuex
* Simple Python backend (Flask) with local Postgres DB on Pi

This was made to mess around with VueJS and is obviously not a production level application.
For sake of simplicity, this runs locally for a single user. 

**I really just wanted to focus on learning Vue with this project.**


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


## References
* VueJS Guide - https://vuejs.org/v2/guide
* VueJS API - https://vuejs.org/v2/api/
* VueJS Config - https://cli.vuejs.org/config/
* Bootstrap-Vue Components - https://bootstrap-vue.org/docs/components