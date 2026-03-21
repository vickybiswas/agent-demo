# Frontend Development Guide - Stranger Things Calculator

7-phase guide for building the NextJS/React TypeScript frontend with Stranger Things theme.

## Overview
- **Tech Stack**: NextJS 14+, TypeScript, SCSS, Framer Motion, Shadcn/UI, Lucide React, Three.js
- **Port**: 3004 (Docker)
- **Theme**: Stranger Things (dark, neon glow, retro 80s, demogorgon-inspired)
- **Testing**: Playwright e2e tests
- **Styling**: SCSS modules (no inline styles, JSON-driven config)

## Phase 1: Setup

**Duration**: ~30 mins
**Deliverables**: Project structure, dependencies, TypeScript config

### Tasks
1. Create NextJS project
   ```bash
   npx create-next-app@latest frontend --typescript --tailwind=false --eslint
   cd frontend
   ```

2. Add dependencies
   ```bash
   npm install framer-motion shadcn-ui lucide-react three three-fiber zustand
   npm install --save-dev @types/node @types/react playwright @playwright/test
   ```

3. Configure TypeScript (strict mode)
   ```json
   {
     "compilerOptions": {
       "strict": true,
       "noImplicitAny": true,
       "noUnusedLocals": true,
       "noUnusedParameters": true
     }
   }
   ```

4. Create folder structure
   ```
   frontend/
   ├── pages/
   │   ├── index.tsx       # Main calculator page
   │   └── api/            # (optional API routes)
   ├── components/
   │   ├── Calculator.tsx  # Main component
   │   ├── Display.tsx     # Number display
   │   └── Button.tsx      # Calculator button
   ├── styles/
   │   ├── globals.scss
   │   ├── calculator.module.scss
   │   ├── theme.scss
   │   └── animations.scss
   ├── config/
   │   └── theme.json      # Color palette, animations config
   └── __tests__/
       └── calculator.spec.ts
   ```

5. Create `.env.local`
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8004
   ```

**Quality Gate**: npm install succeeds, TypeScript strict mode enabled

---

## Phase 2: Theme & Layout

**Duration**: ~1 hour
**Deliverables**: Stranger Things aesthetic, color scheme, typography, layout

### Tasks

1. **Create theme.json** (JSON-driven config)
   ```json
   {
     "colors": {
       "primary": "#FF0000",      // Neon red
       "secondary": "#FF6B9D",    // Hot pink
       "accent": "#FFD700",       // Gold
       "background": "#0a0a0a",   // Near black
       "surface": "#1a1a1a",      // Dark gray
       "text": "#FFFFFF",         // White
       "neon": "#00FF41"          // Matrix green
     },
     "fonts": {
       "heading": "'Press Start 2P', cursive",
       "body": "'Courier New', monospace"
     },
     "animations": {
       "glowPulse": {
         "duration": "2s",
         "intensity": "0.5"
       },
       "flicker": {
         "duration": "0.15s",
         "count": 3
       }
     }
   }
   ```

2. **Create globals.scss** (Base styles)
   ```scss
   @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

   * {
     margin: 0;
     padding: 0;
     box-sizing: border-box;
   }

   body {
     background-color: #0a0a0a;
     color: #ffffff;
     font-family: 'Courier New', monospace;
     overflow: hidden;
   }

   html, body, #__next {
     width: 100%;
     height: 100%;
   }
   ```

3. **Create theme.scss** (Stranger Things aesthetic)
   ```scss
   // Color variables
   $neon-red: #FF0000;
   $neon-pink: #FF6B9D;
   $neon-gold: #FFD700;
   $dark-bg: #0a0a0a;
   $dark-surface: #1a1a1a;
   $text-color: #FFFFFF;

   // Mixins
   @mixin glow-effect {
     text-shadow: 0 0 10px $neon-red, 0 0 20px $neon-pink;
     box-shadow: 0 0 10px $neon-red, 0 0 20px $neon-pink;
   }

   @mixin upside-down {
     transform: rotate(180deg);
   }
   ```

4. **Create animations.scss** (Effects)
   ```scss
   @keyframes glowPulse {
     0%, 100% { opacity: 1; }
     50% { opacity: 0.6; }
   }

   @keyframes flicker {
     0%, 100% { opacity: 1; }
     25% { opacity: 0.3; }
     50% { opacity: 1; }
   }

   @keyframes upside-down-text {
     0% { transform: scaleY(1); }
     50% { transform: scaleY(-1); }
   }
   ```

5. **Create calculator layout** (index.tsx)
   - Dark background with neon borders
   - Display area (7-segment style)
   - Button grid (4x5)
   - Demogorgon silhouette in corner (CSS shapes)

**Quality Gate**: Theme matches Stranger Things, no hardcoded colors (all from theme.json)

---

## Phase 3: Core Component

**Duration**: ~1 hour
**Deliverables**: Calculator logic, state management, UI structure

### Tasks

1. **Create state management** (Zustand)
   ```typescript
   // store/calculator.ts
   import create from 'zustand';

   interface CalculatorStore {
     display: string;
     previousValue: number | null;
     operation: string | null;
     newInput: boolean;
     setDisplay: (value: string) => void;
     handleNumber: (num: number) => void;
     handleOperation: (op: string) => void;
     handleEquals: () => void;
     handleClear: () => void;
   }
   ```

2. **Create Display component** (calculator.module.scss)
   - 7-segment style display
   - Neon red/pink glow
   - Right-aligned text
   - Flickering effect on updates

3. **Create Button component**
   - Grid layout (4 columns)
   - Hover: neon glow + scale (1.05x)
   - Click: flash effect
   - Different styles for operations vs numbers

4. **Create main Calculator component**
   - Assemble Display + Button grid
   - Manage calculator logic
   - Wire up store actions

5. **Implement operations**
   - Addition, subtraction, multiplication, division
   - Error handling (divide by zero → "E" in display)
   - Clear (C), All Clear (AC), Delete (DEL)

**Quality Gate**: Calculator works offline (no API calls yet), all buttons functional

---

## Phase 4: Animations & Effects

**Duration**: ~1.5 hours
**Deliverables**: Smooth animations, sound effects, visual polish

### Tasks

1. **Framer Motion animations**
   - Button press → scale down then up (spring physics)
   - Display update → fade in new number
   - Operation glow → pulse effect
   - Clear animation → shrink and fade

2. **Sound effects**
   - Button click: retro beep (Web Audio API or .mp3)
   - Operation: higher beep
   - Error: buzzer sound
   - Success: ding sound

3. **Background animations**
   - Subtle grid pattern (CSS)
   - Floating particles (Three.js or Framer Motion)
   - Demogorgon eyes that follow cursor (optional, advanced)

4. **Easter eggs**
   - Upside-down text mode (click display 3 times)
   - Random flicker on idle
   - Demogorgon roar sound on divide by zero

5. **Performance optimization**
   - 60fps target (use will-change CSS)
   - Memoize components (React.memo)
   - Lazy load Three.js if used

**Quality Gate**: Animations smooth (60fps), no jank, sounds load without errors

---

## Phase 5: Backend Integration

**Duration**: ~45 mins
**Deliverables**: API calls, error handling, loading states

### Tasks

1. **Create API service** (services/api.ts)
   ```typescript
   const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';

   export async function calculate(operation: string, num1: number, num2: number) {
     const response = await fetch(
       `${API_URL}/${operation}?num1=${num1}&num2=${num2}`
     );
     return response.json();
   }
   ```

2. **Integrate with store**
   - handleEquals() calls backend API
   - Show loading state during request
   - Handle errors (display "E" + console warning)
   - Update display with result

3. **Error handling**
   - Network errors → "E" in display, retry button
   - Invalid operations → error message
   - Timeout → "TIMEOUT" message

4. **Environment variables**
   - NEXT_PUBLIC_API_URL: http://localhost:8004 (dev), https://backend.example.com (prod)

**Quality Gate**: API calls work, results display correctly, errors handled gracefully

---

## Phase 6: Testing

**Duration**: ~1 hour
**Deliverables**: Playwright e2e tests covering main flows

### Tasks

1. **Create test file** (`__tests__/calculator.spec.ts`)
   ```typescript
   import { test, expect } from '@playwright/test';

   test('basic addition', async ({ page }) => {
     await page.goto('http://localhost:3004');
     await page.click('[data-button="5"]');
     await page.click('[data-button="add"]');
     await page.click('[data-button="3"]');
     await page.click('[data-button="equals"]');
     await expect(page.locator('[data-display]')).toContainText('8');
   });
   ```

2. **Test scenarios**
   - Basic operations (add, subtract, multiply, divide)
   - Edge cases (0, negative, decimals)
   - Clear functionality (C, AC, DEL)
   - Multiple operations in sequence
   - Error cases (divide by zero)
   - API integration (backend calls)

3. **Run tests**
   ```bash
   npm run test
   ```

**Quality Gate**: All tests pass, >80% coverage

---

## Phase 7: Review & Polish

**Duration**: ~30 mins
**Deliverables**: Final validation, TypeScript strict mode, build success

### Tasks

1. **TypeScript strict validation**
   ```bash
   npm run type-check
   # No errors or warnings
   ```

2. **Build verification**
   ```bash
   npm run build
   # Completes without warnings
   npm run start  # Production build works
   ```

3. **Run nextjs-validator**
   ```bash
   /nextjs-validator
   ```

4. **Final checks**
   - [ ] No `any` types
   - [ ] All components typed
   - [ ] SCSS organized (no duplication)
   - [ ] Theme.json drives all colors/animations
   - [ ] No hardcoded images (only SVG/CSS shapes)
   - [ ] Animations smooth (60fps)
   - [ ] API integration works
   - [ ] All Playwright tests pass
   - [ ] Lighthouse score > 80
   - [ ] No console errors/warnings

**Quality Gate**: nextjs-validator PASSES

---

## Success Checklist
- ✅ NextJS project created (TypeScript strict)
- ✅ Stranger Things theme implemented
- ✅ Calculator logic complete
- ✅ Animations smooth and polished
- ✅ API integration working
- ✅ All Playwright tests pass
- ✅ nextjs-validator approves
- ✅ Build succeeds
- ✅ No hardcoded colors/images
- ✅ Ready for Docker Phase 3

## Notes
- JSON-driven config: All theme values in theme.json
- No inline styles: Use SCSS modules only
- No images: Use SVG, CSS shapes, or Three.js
- Accessibility: Use semantic HTML, alt text for generated content
- Performance: Lazy load animations, memoize components
