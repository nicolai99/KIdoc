FROM node:alpine as build-deps
WORKDIR /DMS-Frontend
COPY package.json package-lock.json ./
RUN npm install
COPY . ./
RUN npm run build