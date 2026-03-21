# Frontend Development - 7 Phase Checklist

**For**: @React NextJS Specialist agent
**Location**: `/frontend` | **Port**: 3004 | **Stack**: NextJS/TypeScript/SCSS/Animations
**Theme**: Stranger Things (dark, neon, 80s retro) | **Assets**: No images - CSS/SVG/Canvas only

**Hooks Active**: TypeScript/SCSS auto-format on creation
**Skill**: `/nextjs-validator` (run after each phase)
**Duration**: 2-3 hours | **Must Complete**: All 7 phases sequentially

---

## 🎯 Mission

Build a fully-functional Stranger Things themed calculator SPA. No images. JSON-driven design. Use libraries: framer-motion, shadcn-ui, lucide-react, three.js.

---

## 📋 Execution: 7 Phases

### Phase 1: Project Setup ✅ Must Complete
- [ ] Run: `npx create-next-app@latest frontend --typescript --tailwind=no --scss=yes`
- [ ] Install required libraries:
  ```bash
  npm install framer-motion shadcn-ui lucide-react three @three/fiber @three/drei
  npm install --save-dev sass prettier
  ```
- [ ] Create directory structure:
  ```
  src/
  ├── components/        (React components)
  ├── pages/            (NextJS pages)
  ├── styles/           (SCSS files)
  ├── config/           (JSON config files)
  ├── hooks/            (Custom React hooks)
  └── utils/            (Utility functions)
  ```
- [ ] Create `public/config/theme.json` with color palette
- [ ] Create `.env.local` with `NEXT_PUBLIC_API_URL=http://backend:8004`
- [ ] Create `.gitignore` and exclude node_modules
- [ ] Run `npm run dev` and verify localhost:3004 loads

**Validation**: Use `/nextjs-validator` after setup

---

### Phase 2: Theme & Layout ✅ Must Complete
- [ ] Create landing page (`pages/index.tsx`)
- [ ] Create layout component with Stranger Things aesthetic:
  - [ ] Dark background (black/dark purple)
  - [ ] Neon glows on interactive elements
  - [ ] Retro 80s typography and spacing
  - [ ] Upside Down imagery or references
- [ ] Create theme JSON (`public/config/theme.json`):
  ```json
  {
    "colors": {
      "primary": "#6b21a8",
      "secondary": "#06b6d4",
      "accent": "#dc2626",
      "background": "#1a1a2e"
    },
    "fonts": {
      "heading": "font-family: 'Arial', sans-serif",
      "body": "font-family: 'Courier New', monospace"
    }
  }
  ```
- [ ] Create global SCSS with CSS variables
- [ ] Create responsive design for mobile (375px), tablet (768px), desktop (1920px)

**Validation**: Use `/nextjs-validator` after layout

---

### Phase 3: Calculator Component ✅ Must Complete
- [ ] Create `components/Calculator.tsx`:
  - [ ] Display with neon styling (mimics retro calculator)
  - [ ] Input field showing current calculation
  - [ ] Number buttons (0-9)
  - [ ] Operation buttons (+ - * /)
  - [ ] Clear (C) and backspace button
  - [ ] Equals button (=)
  - [ ] Memory buttons (M+, M-, MC, MR) - optional
- [ ] Create `config/calculator.json` with button layout and labels
- [ ] Implement calculator logic:
  - [ ] Add two numbers
  - [ ] Subtract
  - [ ] Multiply
  - [ ] Divide
  - [ ] Handle decimal inputs
  - [ ] Clear and reset functionality

**Validation**: Use `/nextjs-validator` after implementation

---

### Phase 4: Animations & Interactions ✅ Must Complete
- [ ] Add framer-motion animations:
  - [ ] Button press animations (scale, shadow changes)
  - [ ] Display update animations (number slide in)
  - [ ] Page load animation (fade in)
  - [ ] Hover effects on buttons
- [ ] Add sound effects:
  - [ ] Background ambient audio (plays on page load, loops)
  - [ ] Click sound for buttons
  - [ ] Volume control slider
  - [ ] Mute button
- [ ] Add visual effects:
  - [ ] Glow effects on display
  - [ ] Shadow animations on interactions
  - [ ] Smooth transitions between states

**Validation**: Use `/nextjs-validator` after animations

---

### Phase 5: Backend Integration ✅ Must Complete
- [ ] Create `lib/api.ts` with API client:
  ```typescript
  const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';

  export const calculateAdd = async (num1: number, num2: number) => {
    const response = await fetch(`${API_URL}/add?num1=${num1}&num2=${num2}`);
    return response.json();
  };
  // ... other operations
  ```
- [ ] Update Calculator component to use backend:
  - [ ] Replace local calculation with API calls
  - [ ] Handle API errors gracefully
  - [ ] Show loading states during API calls
- [ ] Test with backend running on port 8004

**Validation**: Check calculator works with backend endpoints

---

### Phase 6: Testing & Validation ✅ Must Complete
- [ ] Install Playwright: `npm install --save-dev @playwright/test`
- [ ] Create `tests/calculator.spec.ts`:
  ```typescript
  test('should add two numbers', async ({ page }) => {
    await page.goto('http://localhost:3004');
    await page.click('[data-testid="button-5"]');
    await page.click('[data-testid="button-plus"]');
    await page.click('[data-testid="button-3"]');
    await page.click('[data-testid="button-equals"]');
    const result = await page.textContent('[data-testid="display"]');
    expect(result).toBe('8');
  });
  ```
- [ ] Add data-testid to all interactive elements
- [ ] Write tests for:
  - [ ] Addition
  - [ ] Subtraction
  - [ ] Multiplication
  - [ ] Division
  - [ ] Decimal handling
  - [ ] Clear functionality
- [ ] Run: `npx playwright test`
- [ ] Run: `npm run build` (production build)

**Validation**: Use `/nextjs-validator` before committing

---

### Phase 7: Code Review & Documentation ✅ Must Complete
- [ ] Review all TypeScript code for type safety (no `any` types)
- [ ] Check SCSS for consistency with theme
- [ ] Verify all animations are smooth (60fps)
- [ ] Check for console errors/warnings: `npm run build`
- [ ] Create README.md in frontend/:
  ```markdown
  # Frontend - Stranger Things Calculator

  ## Setup
  npm install
  npm run dev

  ## Testing
  npx playwright test

  ## Build
  npm run build
  npm run start
  ```
- [ ] Document component architecture
- [ ] Add JSDoc comments to complex functions

**Validation**: Use `/nextjs-validator` and `/code-review`

---

## 🚀 Quick Commands

```bash
# Setup
npm install

# Development
npm run dev              # Start dev server on 3004

# Testing
npx playwright test      # Run UI tests
npm run build           # Check for build errors

# Code Quality
npm run lint            # Check linting
prettier --write .      # Format all files (auto via hook)

# Production
npm run build           # Create optimized build
npm start               # Start production server
```

---

## ✅ Work Completion Checklist

Before marking frontend as DONE, verify ALL of these:

- [ ] **Phase 1 Complete**: Project runs on localhost:3004
- [ ] **Phase 2 Complete**: Stranger Things theme fully implemented
- [ ] **Phase 3 Complete**: Calculator displays and handles input
- [ ] **Phase 4 Complete**: All animations and sounds working
- [ ] **Phase 5 Complete**: API integration works with backend
- [ ] **Phase 6 Complete**: All Playwright tests pass
- [ ] **Phase 7 Complete**: No TypeScript errors, SCSS validated
- [ ] **Skills**: Passed `/nextjs-validator`
- [ ] **Tests**: `npx playwright test` shows all pass ✅
- [ ] **Build**: `npm run build` succeeds with no errors
- [ ] **Code**: No console errors when running
- [ ] **Documentation**: README.md created with setup instructions

---

## 🛠️ Tools & Skills Available

| Tool | Use Case |
|------|----------|
| `/nextjs-validator` | Validate TypeScript, SCSS, animations, theme |
| `/code-review` | Code quality and best practices |
| `prettier` | Auto-format TypeScript/SCSS (automatic via hook) |
| `@playwright/test` | UI and integration testing |
| `framer-motion` | Animations and interactions |

---

## ⚠️ Critical Requirements (DO NOT SKIP)

1. **NO IMAGES** - All visual effects via CSS/SVG/Canvas
2. **JSON-DRIVEN DESIGN** - Theme, layout, content in JSON files
3. **TYPESCRIPT STRICT** - Full typing, no `any` types
4. **RESPONSIVE** - Works on mobile, tablet, desktop
5. **TESTABLE** - All interactive elements have data-testid
6. **BACKEND INTEGRATED** - Calls API on port 8004
7. **ANIMATIONS** - Smooth, 60fps, framer-motion based
8. **SOUNDS** - Background ambient + click feedback
9. **THEME** - Consistent Stranger Things aesthetic throughout

---

## 🔍 Validation Workflow

```
1. Write/modify code
   ↓
2. Run: npm run dev (check visually)
   ↓
3. Use: /nextjs-validator (check compliance)
   ↓
4. Run: npx playwright test (check functionality)
   ↓
5. Use: /code-review (check quality)
   ↓
6. Fix any issues found
   ↓
7. Commit with message: "feat(frontend): [description]"
```

---

## 📞 When Stuck

**Use these skills in order**:
1. `/nextjs-validator` - Diagnose what's missing
2. `/code-review` - Identify code issues
3. `/plan` - Redesign approach if needed

---

**Remember**: Each phase MUST be completed and validated before moving to the next. No skipping!
