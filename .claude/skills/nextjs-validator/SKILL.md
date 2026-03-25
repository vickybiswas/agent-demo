# NextJS Validator Skill

## Purpose
Validate NextJS frontend code against project standards before merging.

## Validation Rules

### TypeScript
- ✅ Strict mode enabled in tsconfig.json
- ✅ No `any` types without justification
- ✅ All props typed
- ✅ All function returns typed
- ✅ No unused variables
- ✅ No implicit dependencies

### SCSS & Styling
- ✅ SCSS files only (no CSS-in-JS)
- ✅ Variables defined in _variables.scss
- ✅ No hardcoded colors
- ✅ Responsive breakpoints used
- ✅ Organized by component
- ✅ BEM naming convention where applicable

### Animations
- ✅ Framer-motion used consistently
- ✅ Animations target 60fps
- ✅ No jank or layout shifts
- ✅ Smooth transitions
- ✅ Proper spring/easing config
- ✅ Accessibility: prefers-reduced-motion respected

### Components
- ✅ Functional components with hooks
- ✅ Props properly typed
- ✅ State management clean
- ✅ No prop drilling
- ✅ Component composition clear
- ✅ Reusable patterns

### Integration
- ✅ Environment variables used: NEXT_PUBLIC_API_URL
- ✅ API calls use correct backend URL
- ✅ Error handling for failed requests
- ✅ Loading states implemented
- ✅ CORS headers validated

### Testing
- ✅ Playwright E2E tests exist
- ✅ Tests cover main calculator operations
- ✅ Responsive design tested
- ✅ Animations checked
- ✅ CORS communication verified

### Build
- ✅ `npm run build` succeeds
- ✅ No TypeScript errors
- ✅ No console warnings/errors
- ✅ Assets load correctly
- ✅ Bundle size reasonable

### Code Quality
- ✅ Prettier formatting applied
- ✅ ESLint rules pass
- ✅ No dead code
- ✅ Comments explain complex logic
- ✅ Component names PascalCase
- ✅ File names kebab-case

## Validation Checklist

### Pre-Merge Validation
Run before creating PR:
```bash
# 1. Type checking
npm run type-check

# 2. Linting
npm run lint

# 3. Formatting
npm run format

# 4. Building
npm run build

# 5. Tests
npm run test

# 6. Review checklist
- [ ] TypeScript strict: no errors
- [ ] SCSS organized: variables, animations, layout
- [ ] Animations: smooth 60fps
- [ ] CORS tested: frontend→backend works
- [ ] Responsive: mobile, tablet, desktop
- [ ] Tests: Playwright E2E pass
```

## Failure Cases
Validation fails if:
- TypeScript compilation errors
- ESLint violations
- Playwright tests fail
- Build fails
- CORS communication broken
- Responsive design broken
- Bundle size exceeds threshold

## Success Criteria
- TypeScript strict mode ✅
- Build succeeds ✅
- All tests pass ✅
- Prettier formatted ✅
- CORS verified ✅
- Responsive on all devices ✅
- No console errors ✅

## Integration with CLAUDE.md
This validator runs at the end of frontend/CLAUDE.md Phase 7 (Review).

## Usage
```bash
claude run nextjs-validator
```

Or invoke from CLAUDE.md:
```markdown
## Phase 7: Review
Run `/nextjs-validator` before committing:
- [ ] TypeScript strict
- [ ] Build succeeds
- [ ] Tests pass
- [ ] CORS verified
```
