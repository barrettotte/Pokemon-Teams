# Build stage
FROM node:lts-alpine as build-stage
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /usr/src/app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


# docker build -t barrettotte/pokemon-teams-app .
# docker run -it -p 8021:80 --rm --name pokemon-teams-app barrettotte/pokemon-teams-app