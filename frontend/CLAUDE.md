# Frontend Implementation Guide (7 Phases)

Build a Stranger Things-themed calculator UI with React/NextJS, animations, and SCSS styling.

## Phase 1: NextJS Setup & TypeScript Strict Mode

Initialize a NextJS project with TypeScript strict mode enabled.

### Deliverables
- NextJS project initialized in `frontend/` directory
- TypeScript strict mode enabled (`tsconfig.json` has `"strict": true`)
- No `any` types allowed
- Directory structure: `pages/`, `components/`, `styles/`, `lib/`, `public/`, `__tests__/`

### Implementation Steps
1. `npm create next-app@latest frontend` (TypeScript, ESLint, no Tailwind)
2. Verify `tsconfig.json` has strict mode enabled
3. Create directory structure
4. `npm run type-check` passes with no errors

### Quality Gate ✅
- `npm run type-check` passes (no TypeScript errors)
- No console errors on startup
- All directories created

---

## Phase 2: JSON-Driven Theme & Global Styling

Create SCSS-based theme system driven by JSON configuration.

### Deliverables
- `public/theme.json` - Color palette, typography, spacing (no hardcoded values)
- `styles/theme.scss` - SCSS variables and functions
- `styles/globals.scss` - Global styles (resets, fonts, animations)
- `lib/theme.ts` - Theme loader and application logic
- `styles/animations.scss` - Keyframe animations (scanlines, glows, etc.)

### Theme Configuration (`public/theme.json`)
```json
{
  "colors": {
    "background": "#0a0e27",
    "primary": "#ff006e",
    "secondary": "#00f5ff",
    "accent": "#ffbe0b",
    "text": "#ffffff"
  },
  "typography": {
    "fontSize": "16px",
    "fontFamily": "'Press Start 2P', monospace"
  },
  "spacing": {
    "unit": "8px",
    "padding": "24px"
  }
}
```

### SCSS Organization
```
styles/
├── theme.scss           # Variables from theme.json
├── globals.scss         # Global reset, fonts, body styles
├── animations.scss      # Keyframes for animations
└── mixins.scss         # Responsive design mixins
```

### Stranger Things Aesthetic
- Dark backgrounds (#0a0e27 or darker)
- Neon colors: magenta (#ff006e), cyan (#00f5ff), yellow (#ffbe0b)
- Retro typography: Press Start 2P or similar
- Glow effects: `text-shadow`, `box-shadow` with neon colors
- Scanline effect: overlay animation with horizontal lines

### Quality Gate ✅
- No hardcoded color values in SCSS files
- All colors sourced from `theme.json`
- Global styles applied: body styling, font loading, animation definitions
- Responsive design mixins created for mobile/tablet/desktop

---

## Phase 3: Calculator Component & Button Interactions

Build the main calculator component with button styling and layout.

### Deliverables
- `components/Calculator.tsx` - Main calculator component
- `components/Button.tsx` - Styled button component
- `components/Display.tsx` - Result display area
- `components/Layout.tsx` - Page wrapper with theme
- `pages/index.tsx` - Main page using Calculator component
- `styles/calculator.scss` - Calculator-specific styling

### Component Structure
```typescript
// Button.tsx - Clickable button with state feedback
<Button onClick={() => handleOperation('add')} label="+" />

// Display.tsx - Shows current result
<Display value={result} />

// Calculator.tsx - Orchestrates buttons, display, operations
<Calculator>
  <Display />
  <Button /> × 12
</Calculator>

// pages/index.tsx - Root page
<Layout>
  <Calculator />
</Layout>
```

### Button Styling
- Background: Neon color from theme
- Hover: Brightness increase + scale
- Active: Pressed state (scale down)
- Transition: Smooth (200ms cubic-bezier)

### Calculator Grid
- 4x4 grid for calculator buttons (0-9, +, -, ×, ÷, =, C, CE, M+, M-)
- Buttons: Numbers (10), Operations (4), Control (5)
- Display area at top
- Memory display (optional, for M+/M- context)

### Quality Gate ✅
- All buttons render and respond to clicks
- Calculator grid is responsive (scales for mobile/desktop)
- Button styling matches Stranger Things theme
- Display updates on button click (visual feedback, no calculation yet)

---

## Phase 4: Animations, Sound Effects & Visual Interactions

Add smooth animations using framer-motion and implement audio effects.

### Deliverables
- framer-motion animations on all interactive elements
- Sound effects on button clicks and results
- Result display animation (fade-in + scale)
- Confirmation animation (checkmark or similar)
- Background animations (optional: particle effects, moving shapes)
- 60fps smooth animations, no frame drops

### Animation Details

**Button Interactions**:
- Click: Scale down (0.95) then back up (1.0)
- Color: Brief flash or glow
- Duration: 150ms, easing: easeOut

**Result Display**:
- Appear: Fade-in (0 → 1 opacity) + scale (0.8 → 1.0)
- Duration: 300ms, easing: easeOut
- Leave: Fade-out when new operation starts

**Background**:
- Scanlines: Overlay with moving horizontal lines (subtle, 80s aesthetic)
- Glow: Subtle pulsing glow on buttons (optional)
- Particles: Optional animated background elements (use three.js or canvas)

**Sound Effects**:
- Button click: Sharp beep or tone (100-200ms)
- Successful calculation: Success sound (300-500ms)
- Error: Error buzz (100-150ms)
- Use Web Audio API or HTML5 `<audio>` tags

### Implementation Notes
- Use `framer-motion` for component animations
- Use `useAnimation` or `variants` for controlled animation states
- Keep animations under 300ms to feel responsive
- Test 60fps: DevTools → Performance tab
- No jank: Check for dropped frames during interactions

### Quality Gate ✅
- All buttons animate on click
- Result displays with smooth fade-in + scale
- Sounds play on interaction (test with speakers on)
- 60fps confirmed: DevTools Performance tab shows no dropped frames
- No stuttering during rapid clicks

---

## Phase 5: Backend Integration & CORS Testing

Connect frontend to FastAPI backend with proper environment variable handling and CORS validation.

### Deliverables
- `lib/api.ts` - FastAPI client with environment variable support
- API calls for all 4 operations (add, subtract, multiply, divide)
- CORS headers validation in Network tab
- Error handling (network errors, invalid responses, timeouts)
- Environment variables used (not hardcoded localhost)

### API Client (`lib/api.ts`)
```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';

export async function calculate(operation: 'add' | 'subtract' | 'multiply' | 'divide', num1: number, num2: number) {
  const response = await fetch(`${API_URL}/${operation}?num1=${num1}&num2=${num2}`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return await response.json(); // { result: value }
}
```

### CORS Testing
```bash
# In browser DevTools → Network tab, perform a calculation
# Check request headers:
#   Origin: http://localhost:3004
# Check response headers:
#   Access-Control-Allow-Origin: http://localhost:3004
#   Access-Control-Allow-Credentials: true

# Or via curl:
curl -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3
```

### Environment Variables
**Dev** (`.env.local`):
```
NEXT_PUBLIC_API_URL=http://localhost:8004
```

**Docker** (`.env`):
```
NEXT_PUBLIC_API_URL=http://backend:8004
```

### Error Handling
- Network error: Display "Connection failed" message
- Invalid response: Display "Invalid response from server"
- Timeout: Set 5s timeout, display "Server timeout"
- Invalid operation: Validate inputs before sending request

### Phase 5 Testing - CORS Integration (CRITICAL)
```bash
# 1. Start backend: python main.py (Terminal 1, port 8004)
# 2. Start frontend: npm run dev (Terminal 2, port 3004)
# 3. Open http://localhost:3004 in browser
# 4. Open DevTools (F12) → Network tab
# 5. Enter 5, click +, enter 3, click =
# 6. Check Network tab:
#    - Request to http://localhost:8004/add?num1=5&num2=3
#    - Response headers include: Access-Control-Allow-Origin: *
#    - Response body: {"result": 8}
# 7. Display shows 8 (result animated in)
# 8. No CORS errors in Console tab
```

### Quality Gate ✅
- CORS headers present in response (Network tab shows Access-Control-Allow-Origin)
- Frontend ↔ Backend communication works: 5 + 3 = 8 displays correctly
- No CORS errors in browser console
- Environment variables used (NEXT_PUBLIC_API_URL, not hardcoded)
- Error handling works (network errors display gracefully)

---

## Phase 6: Playwright E2E Tests

Write comprehensive tests validating all calculator operations and interactions.

### Deliverables
- `__tests__/calculator.spec.ts` - Calculator operation tests
- `__tests__/responsive.spec.ts` - Responsive design tests
- All tests passing: `npx playwright test`
- Tests cover: happy path, error cases, animations, CORS, responsive layouts

### Test Examples

**calculator.spec.ts**:
```typescript
test('5 + 3 = 8', async ({ page }) => {
  await page.goto('http://localhost:3004');
  await page.click('button:has-text("5")');
  await page.click('button:has-text("+")');
  await page.click('button:has-text("3")');
  await page.click('button:has-text("=")');
  const result = await page.locator('[data-testid="display"]').textContent();
  expect(result).toBe('8');
});

test('Keyboard Enter calculates', async ({ page }) => {
  await page.goto('http://localhost:3004');
  await page.type('[data-testid="display"]', '5+3');
  await page.press('[data-testid="display"]', 'Enter');
  const result = await page.locator('[data-testid="display"]').textContent();
  expect(result).toBe('8');
});

test('CORS request succeeds', async ({ page }) => {
  // Verify Network tab shows CORS headers
  const responses: string[] = [];
  page.on('response', (response) => {
    if (response.url().includes('localhost:8004')) {
      responses.push(response.headers()['access-control-allow-origin'] || '');
    }
  });
  await page.goto('http://localhost:3004');
  await page.click('button:has-text("5")');
  await page.click('button:has-text("+")');
  await page.click('button:has-text("3")');
  await page.click('button:has-text("=")');
  expect(responses.some(h => h.includes('*') || h.includes('localhost'))).toBeTruthy();
});
```

**responsive.spec.ts**:
```typescript
test('Mobile layout (320px)', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 640 });
  await page.goto('http://localhost:3004');
  const display = page.locator('[data-testid="display"]');
  expect(await display.isVisible()).toBeTruthy();
  // Verify buttons stack appropriately
});

test('Desktop layout (1920px)', async ({ page }) => {
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.goto('http://localhost:3004');
  const buttons = page.locator('button');
  expect(await buttons.count()).toBeGreaterThan(10);
});
```

### Test Coverage
- ✅ All 4 operations: add, subtract, multiply, divide
- ✅ Display updates correctly
- ✅ Animations trigger on click
- ✅ Sound plays on interaction (check audio element)
- ✅ Keyboard navigation works
- ✅ Mobile responsive (320px)
- ✅ Tablet responsive (768px)
- ✅ Desktop responsive (1920px)
- ✅ CORS requests succeed (no browser blocking)
- ✅ Error handling (backend timeout, invalid response)

### Quality Gate ✅
- All Playwright tests pass: `npx playwright test` shows all green
- Tests cover calculator operations, animations, CORS, responsive layouts
- No test skips (no `.skip`, `.only`)
- Test execution < 30 seconds

---

## Phase 7: TypeScript Strict Validation & Build

Verify TypeScript strict mode compliance and NextJS build succeeds.

### Deliverables
- `npm run type-check` passes (no TypeScript errors)
- `npm run build` succeeds (no build warnings/errors)
- No `any` types in codebase
- All components properly typed
- Production build runs: `npm run start`

### Validation Steps

**TypeScript Strict Check**:
```bash
npm run type-check
# Expected: "Type checking complete"
```

**Build Check**:
```bash
npm run build
# Expected: ✓ Compiled successfully
# Expected: ✓ Collected all compiled pages
# Expected: ✓ Created optimized production build
```

**Production Run** (optional):
```bash
npm run build
npm run start
# Open http://localhost:3000 (default port)
```

**Browser Console Check**:
- Open http://localhost:3004 (dev server) or http://localhost:3000 (prod)
- Open DevTools (F12) → Console tab
- Perform a calculation
- Expected: No errors, no warnings
- No `any` types, no @ts-ignore comments

### Performance (Bonus)
- Lighthouse check: DevTools → Lighthouse
  - LCP < 2.5s (Largest Contentful Paint)
  - FID < 100ms (First Input Delay)
  - CLS < 0.1 (Cumulative Layout Shift)

### Code Quality Checks
- ✅ No unused imports: `npm run lint`
- ✅ No hardcoded localhost: `grep -r "localhost" src/`
- ✅ No debug code: `grep -r "console.log" src/` (should be empty)
- ✅ All components documented: JSDoc comments on components

### Quality Gate ✅
- `npm run type-check` passes (no TypeScript errors)
- `npm run build` succeeds (no build warnings/errors)
- `npm run lint` passes (no linting issues)
- No `any` types in code
- No console errors when running
- Browser console clean (no errors/warnings)

---

## Parallelization Strategy

**Within Phase Testing** (when tests are independent):

Spawn all test suites in parallel:
```bash
npm run type-check &
npx playwright test &
npm run build &
# All three run simultaneously
# Collect results when all complete
```

This cuts validation time from ~3 minutes (sequential) to ~1 minute (parallel).

---

## Success Criteria

✅ **Frontend is production-ready if ALL phases are complete**:
- ✅ Phase 1: NextJS + TypeScript strict mode
- ✅ Phase 2: JSON-driven SCSS theme
- ✅ Phase 3: Calculator component with styled buttons
- ✅ Phase 4: Smooth animations and sound effects (60fps)
- ✅ Phase 5: Backend integration with CORS working
- ✅ Phase 6: All Playwright tests passing
- ✅ Phase 7: TypeScript strict + build succeeds

---

## Next Steps

Once all 7 phases are complete:
1. Verify REGRESSION.md Phase 4 checks pass
2. Backend must also be complete (see backend/CLAUDE.md)
3. Docker orchestration will be built (see CREATE.md)
4. After everything is working, create PR with REGRESSION.md checklist
