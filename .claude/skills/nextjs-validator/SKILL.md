# NextJS Validator Skill

## Purpose
Validate TypeScript/NextJS frontend code against INSTRUCTIONS.md and frontend/CLAUDE.md requirements.

## Triggered On
- Frontend code creation (hooks auto-format)
- Manual invocation: `/nextjs-validator`

## Validation Checklist

### TypeScript & Code Quality
- [ ] TypeScript strict mode enabled (tsconfig.json)
- [ ] No `any` types without explicit escape hatches
- [ ] All component props typed
- [ ] No console.logs or debug code in production paths
- [ ] Imports organized (React, libraries, local components)

### Styling & Theme
- [ ] SCSS modules used (no inline CSS, no CSS-in-JS)
- [ ] Stranger Things theme variables defined in global.scss
- [ ] No hardcoded colors (all from theme variables)
- [ ] No image imports or background images (theme.json driven)
- [ ] Responsive design via media queries (mobile, tablet, desktop)

### Animations & Interactions
- [ ] framer-motion used for animations
- [ ] 60fps smooth animations (no jank)
- [ ] Button hover effects implemented
- [ ] Button click effects implemented
- [ ] Sound effects integrated (if applicable)
- [ ] Background animations present
- [ ] Animations respect prefersReducedMotion

### Calculator Functionality
- [ ] /add endpoint integration
- [ ] /subtract endpoint integration
- [ ] /multiply endpoint integration
- [ ] /divide endpoint integration
- [ ] Input validation (numbers only)
- [ ] Result display
- [ ] Error handling (division by zero, invalid input)

### Integration
- [ ] NEXT_PUBLIC_API_URL environment variable used
- [ ] .env.local and .env.example documented
- [ ] CORS headers validated in tests
- [ ] Backend communication tested
- [ ] No hardcoded localhost:8004

### Testing (Playwright)
- [ ] playwright.config.ts configured
- [ ] tests/ directory with *.spec.ts files
- [ ] Calculator operation tests (5+ basic operations)
- [ ] Backend integration tests
- [ ] CORS validation tests
- [ ] All tests pass

### Build & Performance
- [ ] `npm run build` succeeds
- [ ] No build warnings
- [ ] Bundle size reasonable
- [ ] First contentful paint < 2s
- [ ] Lighthouse score > 80

### Documentation
- [ ] README.md in frontend/
- [ ] .env.local.example documented
- [ ] CLAUDE.md phase checklist followed
- [ ] Comments explain non-obvious logic

## Pass/Fail Criteria
✅ **PASS**: All checked items pass, no blocking errors
❌ **FAIL**: Any unchecked items or blocking errors

## Outputs
- Checklist results (passed/failed items)
- Recommendations for improvement
- Performance metrics (if applicable)
