# Use Node.js LTS on Alpine for small image size
FROM node:22-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Expose development server port
EXPOSE 3004

# Set environment for hot-reload
ENV NODE_ENV=development

# Start development server
CMD ["npm", "run", "dev"]
