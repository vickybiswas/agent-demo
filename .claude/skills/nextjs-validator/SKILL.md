# NextJS Validator Skill

Validates NextJS/React TypeScript frontend for quality and specification compliance.

## Purpose
Ensures frontend meets all project requirements before integrating with backend.

## Validation Checklist

### TypeScript Validation
- [ ] `tsconfig.json` has strict mode enabled
- [ ] No `any` types without justification
- [ ] All components properly typed
- [ ] Build succeeds without warnings

### SCSS & Styling
- [ ] All styles in SCSS (no inline styles)
- [ ] JSON-driven configuration (theme colors, animations)
- [ ] No hardcoded images (use SVG or generated shapes)
- [ ] Responsive design implemented

### Stranger Things Theme
- [ ] Dark color palette (blacks, deep purples, reds)
- [ ] Retro 80s typography
- [ ] Neon glow effects (CSS animations)
- [ ] Upside-down text easter egg elements
- [ ] Demogorgon-inspired UI elements

### Animations
- [ ] Framer-motion animations smooth (60fps)
- [ ] Button hover/click interactions
- [ ] Sound effects functional
- [ ] No jank or stuttering

### Backend Integration
- [ ] API calls point to `http://backend:8004`
- [ ] Endpoints: /add, /subtract, /multiply, /divide
- [ ] Error handling for failed requests
- [ ] Loading states during API calls

### Testing
- [ ] Playwright tests pass (all scenarios)
- [ ] UI tests cover main flows
- [ ] No hardcoded timeouts
- [ ] Accessibility checks pass

### Build & Performance
- [ ] NextJS build completes without errors
- [ ] Production bundle size reasonable
- [ ] Lighthouse score > 80
- [ ] No console errors in browser

## How to Invoke

```bash
/nextjs-validator
```

Validator will:
1. Check TypeScript compilation
2. Verify SCSS structure
3. Validate Playwright tests
4. Check API integration
5. Verify theme compliance

## Output Format
- ✅ Passing checks
- ⚠️ Warnings
- ❌ Failing checks (blocks merge)

## Pass Criteria
- All ❌ items resolved
- No hardcoded images
- All tests passing
- Build successful
- TypeScript strict mode passes
