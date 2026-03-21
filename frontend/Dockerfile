FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

# Volume mount for source code (hot reload)
# Defined in docker-compose.yaml, not here

EXPOSE 3004

CMD ["npm", "run", "dev"]
