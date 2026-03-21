# NextJS Validator Skill

Validates React NextJS frontend implementation for TypeScript strict mode, animations, styling, and Playwright testing.

## Usage

```
/nextjs-validator
```

## What It Validates

### 1. Project Structure
- ✅ `frontend/` directory exists
- ✅ `pages/index.tsx` (main calculator page)
- ✅ `components/` directory with components:
  - `Calculator.tsx`, `Button.tsx`, `Display.tsx`, `Layout.tsx`
- ✅ `styles/` directory with SCSS files:
  - `globals.scss`, `theme.scss`, `calculator.scss`, `animations.scss`
- ✅ `public/theme.json` (JSON-driven theme config)
- ✅ `__tests__/` directory with Playwright tests
- ✅ `tsconfig.json` with strict mode enabled
- ✅ `next.config.js` exists
- ✅ `Dockerfile` exists in `frontend/`

### 2. TypeScript Strict Mode
- ✅ `tsconfig.json` has `"strict": true`
- ✅ No `any` types in code
- ✅ All component props typed
- ✅ All function parameters typed
- ✅ No type errors: `npm run type-check` passes
- ✅ No TypeScript warnings

### 3. Styling & Theme
- ✅ SCSS used (no CSS/inline styles)
- ✅ JSON-driven theme configuration:
  - `public/theme.json` defines colors, spacing, typography
  - `lib/theme.ts` loads and applies theme
- ✅ No hardcoded color values in SCSS
- ✅ Responsive design with mixins (mobile, tablet, desktop)
- ✅ Stranger Things aesthetic:
  - Dark background with neon accents
  - Glow effects and shadows
  - Retro 80s typography
  - Scanline effects

### 4. Animations
- ✅ framer-motion animations smooth (60fps)
- ✅ Animations triggered on button click:
  - Button scale/color change
  - Result display fade-in/scale
  - Confirmation checkmark animation
- ✅ three.js or canvas for background effects
- ✅ Sound effects play on interaction (Web Audio API)
- ✅ No jank, no frame drops

### 5. API Integration
- ✅ Environment variable for API URL:
  - Dev: `NEXT_PUBLIC_API_URL=http://localhost:8004`
  - Docker: `NEXT_PUBLIC_API_URL=http://backend:8004`
- ✅ API client (`lib/api.ts`):
  - Calls GET /add?num1=X&num2=Y endpoints
  - Parses JSON response `{"result": value}`
  - Handles errors (network, timeout, invalid JSON)
- ✅ CORS: Frontend sends Origin header, backend responds correctly
- ✅ No hardcoded localhost in code

### 6. Build & Performance
- ✅ NextJS build succeeds: `npm run build`
- ✅ No build warnings/errors
- ✅ No console errors or warnings
- ✅ LCP < 2.5s (Lighthouse)
- ✅ FID < 100ms
- ✅ CLS < 0.1

### 7. Testing
- ✅ Playwright tests in `__tests__/`:
  - Calculator operations (5 + 3 = 8)
  - Display updates
  - Sound effects (audio element checked)
  - Keyboard navigation (Enter key)
  - Mobile responsive (320px layout)
  - Desktop responsive (1920px layout)
  - CORS requests succeed (no browser blocking)
  - Error handling (backend timeout, invalid response)
- ✅ All Playwright tests pass: `npx playwright test`
- ✅ Tests cover happy path and error cases

## Validation Steps

1. Check file structure exists
2. Verify TypeScript strict mode: `npm run type-check` passes
3. Build frontend: `npm run build` succeeds
4. Check for no console errors
5. Run Playwright tests: `npx playwright test`
6. Validate SCSS (no hardcoded colors, JSON-driven config)
7. Check animations: 60fps, smooth easing
8. Verify API integration (environment variable used)
9. Check Docker image builds: `docker build -f frontend/Dockerfile .`

## Pass Criteria

✅ **PASS** if ALL of the following are true:
- File structure correct
- TypeScript strict mode enabled, no errors
- NextJS build succeeds
- All Playwright tests pass
- SCSS properly organized with JSON-driven theme
- Animations smooth (60fps, no jank)
- API integration working (environment variable based)
- CORS requests succeed
- No console errors/warnings

❌ **FAIL** if ANY of:
- TypeScript errors or type violations
- NextJS build fails
- Playwright tests failing
- Hardcoded colors/values in SCSS
- Animations jank or drop frames
- API calls hardcoded to localhost
- CORS errors in browser console

## Output

```
✅ NextJS Validator Results

Project Structure:
  ✅ pages/, components/, styles/ directories
  ✅ Playwright tests in __tests__/
  ✅ theme.json exists

TypeScript & Build:
  ✅ tsconfig.json strict mode enabled
  ✅ npm run type-check passes (no errors)
  ✅ npm run build succeeds

Styling & Theme:
  ✅ SCSS properly organized
  ✅ JSON-driven theme configuration
  ✅ No hardcoded values
  ✅ Responsive design (mobile, tablet, desktop)

Animations:
  ✅ framer-motion animations smooth (60fps)
  ✅ Button interactions responsive
  ✅ Result display animated
  ✅ Sound effects present

API Integration:
  ✅ NEXT_PUBLIC_API_URL environment variable used
  ✅ API client handles CORS
  ✅ Calculator operations work (5 + 3 = 8)

Testing:
  ✅ Playwright tests: 8+ tests
  ✅ All tests passing
  ✅ Coverage: calculator ops, animations, CORS, responsive

Performance:
  ✅ LCP < 2.5s
  ✅ FID < 100ms
  ✅ CLS < 0.1

Result: ✅ PASS - Frontend ready for integration
```
