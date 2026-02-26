# Stage 1 — build
FROM node:20-alpine AS builder

WORKDIR /app
# Використовуємо npm ci для більш стабільної та швидкої інсталяції в CI/Docker
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2 — serve
FROM nginx:alpine

# Видаляємо дефолтні файли nginx
RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]