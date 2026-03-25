# Stranger Things Calculator Frontend

A Stranger Things themed calculator SPA built with Next.js 14, TypeScript, SCSS, and Framer Motion animations.

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript (strict mode)
- **Styling**: SCSS modules with variables
- **Animations**: Framer Motion
- **Testing**: Playwright E2E
- **UI Components**: Custom components with neon Stranger Things aesthetic

## Project Structure

```
frontend/
├── app/                          # Next.js app directory
│   ├── layout.tsx               # Root layout
│   ├── page.tsx                 # Home page
│   ├── globals.scss             # Global styles
│   └── page.module.scss         # Page styles
├── components/                   # React components
│   ├── Calculator.tsx           # Main calculator logic
│   ├── Display.tsx              # Display screen
│   ├── Button.tsx               # Calculator button
│   ├── Calculator.module.scss   # Calculator styles
│   ├── Display.module.scss      # Display styles
│   └── Button.module.scss       # Button styles
├── styles/                       # Global SCSS
│   ├── _variables.scss          # Colors, fonts, breakpoints
│   ├── _layout.scss             # Layout and container
│   └── _animations.scss         # Keyframe animations
├── config/                       # Configuration
│   └── config.json              # Theme configuration
├── tests/                        # Playwright tests
│   └── calculator.spec.ts       # E2E test suite
├── public/                       # Static assets
├── tsconfig.json                # TypeScript configuration
├── next.config.js               # Next.js configuration
├── playwright.config.ts         # Playwright configuration
├── .env.local                   # Environment variables
└── package.json                 # Dependencies and scripts
```

## Features

- **Stranger Things Theme**: Neon colors (#FF6B6B, #4ECDC4, #00D4FF), 80s aesthetic
- **Responsive Design**: Mobile, tablet, and desktop layouts
- **Smooth Animations**: Framer Motion for button interactions and display transitions
- **Basic Calculator Operations**: Addition, subtraction, multiplication, division, clear
- **Decimal Support**: Handle decimal numbers
- **TypeScript Strict Mode**: Full type safety
- **E2E Testing**: 5+ Playwright test scenarios

## Getting Started

### Prerequisites

- Node.js 18+
- npm 9+

### Installation

```bash
npm install
```

### Development

Start the dev server:

```bash
npm run dev
```

Open http://localhost:3004 in your browser.

### Build

Build for production:

```bash
npm run build
```

Start production server:

```bash
npm start
```

## Scripts

- `npm run dev` - Start dev server (port 3004)
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run type-check` - Check TypeScript types
- `npm run format` - Format code with Prettier
- `npm test` - Run Playwright E2E tests
- `npm run test:ui` - Run tests with UI

## Testing

Run all E2E tests:

```bash
npm test
```

Test scenarios:

1. **Addition**: 5 + 3 = 8
2. **Subtraction**: 10 - 3 = 7
3. **Multiplication**: 4 * 5 = 20
4. **Division**: 20 / 4 = 5
5. **Clear**: Reset display to 0

## Theme Configuration

Colors are defined in `styles/_variables.scss`:

- Primary (Buttons): #FF6B6B (red)
- Secondary (Display): #4ECDC4 (cyan)
- Background: #1A1A2E (dark blue)
- Text: #EAEAEA (light gray)
- Neon: #00D4FF (bright cyan)

## Environment Variables

Configure in `.env.local`:

```
NEXT_PUBLIC_API_URL=http://localhost:8004
```

## Backend Integration

The calculator frontend connects to a backend API at `http://localhost:8004` for advanced operations (future use).

Current operations are handled client-side (add, subtract, multiply, divide).

## Performance

- Optimized build with SWC
- SCSS modules for scoped styling
- Framer Motion for hardware-accelerated animations
- Next.js automatic code splitting

## Quality Checklist

- TypeScript strict mode: ✓ Pass
- Build: ✓ Success
- Prettier formatting: ✓ Applied
- E2E tests: ✓ Pass (5 scenarios)
- Responsive design: ✓ Verified
- CORS ready: ✓ Configured

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Future Enhancements

- Backend API integration for scientific operations
- Calculation history
- Dark/light theme toggle
- Keyboard support (number pad)
- More advanced mathematical operations (sqrt, power, trig)
