# Stranger Things Calculator Frontend

A retro Stranger Things-themed calculator web application built with Next.js, TypeScript, SCSS, and Framer Motion animations.

## Features

- **Stranger Things Theme**: JSON-driven configuration with neon colors, glitch effects, and scanlines
- **HIGHLY ANIMATED**: Framer Motion animations for button interactions, SCSS keyframe animations for text effects
- **TypeScript Strict Mode**: Full type safety with no implicit any
- **SCSS Modules**: Component-scoped styling with global animations
- **Responsive Design**: Mobile-first approach with breakpoints for tablet and desktop
- **Backend Integration**: Communicates with FastAPI backend for calculations
- **E2E Testing**: Playwright tests for calculator operations and CORS validation

## Quick Start

### Prerequisites

- Node.js 18+
- Backend running on `http://localhost:8004`

### Setup & Run

```bash
npm install
npm run dev
```

Frontend starts on `http://localhost:3004`

### Environment Variables

Create `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8004
```

## Building & Testing

```bash
# Build for production
npm run build

# Run E2E tests (backend must be running)
npm run test

# TypeScript strict mode check
npx tsc --noEmit
```

## Project Structure

- `app/` - Next.js pages and layout
- `components/` - React components (Calculator, Display, Button)
- `styles/` - Global SCSS with theme variables and animations
- `config/` - Theme configuration (theme.json)
- `tests/` - Playwright E2E tests

## Theme Configuration

Edit `config/theme.json` to customize Stranger Things colors, fonts, and effects.

## SCSS Animations

Global animations include:
- Glitch text effect
- Neon glow
- CRT scanlines
- Screen flicker
- Neon pulse

## Code Quality

- TypeScript strict mode enabled
- No console.log or debug code
- SCSS modules for component styling
- Responsive design (mobile-first)
- Accessibility: respects `prefers-reduced-motion`

## Backend Integration

Calculator calls FastAPI backend endpoints:
- `GET /add?num1=X&num2=Y`
- `GET /subtract?num1=X&num2=Y`
- `GET /multiply?num1=X&num2=Y`
- `GET /divide?num1=X&num2=Y`

## Testing

Playwright E2E tests verify:
- All calculator operations
- CORS headers from backend
- Backend communication
- Error handling

## References

- [frontend/CLAUDE.md](./CLAUDE.md) - Complete development guide
- [REGRESSION.md](../REGRESSION.md) - Pre-PR checklist
- [Next.js Docs](https://nextjs.org/)
- [Playwright Docs](https://playwright.dev/)
