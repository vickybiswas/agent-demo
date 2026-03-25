FROM node:22-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy application code
COPY . .

# Expose port 3004 for dev server
EXPOSE 3004

# Run dev server with hot reload
CMD ["npm", "run", "dev"]
