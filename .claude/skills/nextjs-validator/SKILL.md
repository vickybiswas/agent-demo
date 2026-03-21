---
name: nextjs-validator
description: Validate NextJS frontend implementation against Stranger Things theme requirements. Use this skill to check TypeScript/SCSS code quality, validate animations and interactions, verify required libraries (framer-motion, shadcn/ui, lucide-react, three.js), ensure JSON-driven design patterns, and validate Playwright test coverage. Run this whenever building or reviewing NextJS components, layout, styling, or UI interactions for compliance with project specifications.
compatibility:
  - playwright (for UI testing)
  - code-review-graph (for code analysis)
---

# NextJS Frontend Validator

This skill validates your React/NextJS frontend implementation against the Stranger Things Calculator specifications.

## What This Skill Does

Validates that your NextJS SPA meets these requirements:
- **TypeScript compliance** - proper typing, no `any` types where avoidable
- **SCSS implementation** - styled entirely with SCSS/CSS, no images
- **Stranger Things theme** - consistent dark/neon aesthetic, purple/teal colors, retro 80s elements
- **Animations** - smooth transitions, button interactions, scene effects using framer-motion
- **Sound & effects** - background ambient audio, click feedback
- **JSON-driven design** - theme config, animation specs, text content in JSON, not hardcoded
- **Library usage** - framer-motion, shadcn/ui, lucide-react, three.js properly imported and used
- **Responsive design** - works on mobile, tablet, desktop
- **Playwright readability** - selectable elements with proper test IDs

## How to Use This Skill

**Check your current implementation:**
```
/nextjs-validator
Check my frontend code against the Stranger Things theme requirements.
Look at the components, styling, and animations.
Are we meeting the theme spec?
```

**After adding new features:**
```
/nextjs-validator
I just added a new button component. Validate it against theme requirements -
animations, styling, click interactions, accessibility.
```

**Before running tests:**
```
/nextjs-validator
Validate the entire frontend structure. Check if it's ready for Playwright testing
and can run in the Docker container on port 3004.
```

## Validation Checklist

The skill will check these items:

### Structure & Setup
- [ ] NextJS project initialized with TypeScript
- [ ] Required dependencies installed (framer-motion, shadcn/ui, lucide-react, three.js)
- [ ] pages/ or app/ directory structure correct
- [ ] Environment variables configured for API endpoint (backend on :8004)

### Code Quality - TypeScript
- [ ] No `any` types (use proper interfaces/types)
- [ ] Components properly typed with React.FC or functional component types
- [ ] Props properly defined with interfaces
- [ ] State management is typed (useState, useContext with generics)
- [ ] Event handlers have proper typing

### Styling - SCSS/CSS
- [ ] All styling in SCSS/CSS modules or global SCSS
- [ ] No inline styles (except framer-motion inline animations)
- [ ] Consistent spacing scale (8px, 16px, 24px, etc.)
- [ ] Color palette defined in variables (purples, teals, blacks, neon accents)
- [ ] Dark theme applied throughout
- [ ] No images - all effects are CSS/SVG/Canvas

### Stranger Things Theme
- [ ] Landing page mimics calculator layout (display, buttons C/M/etc)
- [ ] Neon glow effects on buttons and display
- [ ] Retro 80s typography and spacing
- [ ] Dark atmospheric background (dark purple/black)
- [ ] Upside Down imagery or references implemented
- [ ] Overall aesthetic consistent throughout

### Animations (framer-motion)
- [ ] Button press animations (scale, shadow, glow)
- [ ] Page transitions smooth (fade, slide)
- [ ] Input display updates animated
- [ ] Hover effects on interactive elements
- [ ] No jarring jumps or instant changes

### Sound & Effects
- [ ] Background ambient audio plays on page load
- [ ] Click sound feedback on buttons
- [ ] Volume controls included
- [ ] No autoplay blocking (user interaction triggers audio)

### JSON-Driven Design
- [ ] Theme config in JSON (colors, shadows, spacing)
- [ ] Animation configs in JSON (durations, easing, keyframes)
- [ ] Calculator buttons defined in JSON (label, value, styling)
- [ ] Copy/labels in JSON (not hardcoded strings)
- [ ] Easy to modify without code changes

### Testing Readiness
- [ ] All interactive elements have data-testid
- [ ] Form inputs have proper labels/names
- [ ] Buttons have descriptive text or aria-labels
- [ ] API endpoints referenced correctly (http://localhost:8004 or environment var)
- [ ] No console errors or warnings
- [ ] Ready for Playwright automated testing

### Responsive Design
- [ ] Mobile (375px): calculator visible, buttons accessible
- [ ] Tablet (768px): good spacing and layout
- [ ] Desktop (1920px): centered, not too large, readable
- [ ] Touch targets 44px+ for mobile
- [ ] Text readable at all sizes

## How the Skill Works

1. **Code Analysis**: Reviews TypeScript files for type safety and best practices
2. **Styling Check**: Inspects SCSS files for theme compliance, color usage, animations
3. **Library Audit**: Verifies framer-motion, shadcn/ui, lucide-react, three.js are properly used
4. **Theme Validation**: Checks for Stranger Things aesthetic elements
5. **Configuration Review**: Verifies JSON-driven design patterns
6. **Test Readiness**: Checks for Playwright compatibility (test IDs, selectors)
7. **Report**: Generates a checklist with pass/fail status and actionable feedback

## Output Format

The skill produces a validation report with:
- **Status**: ✅ Pass, ⚠️ Warnings, ❌ Failures
- **Category**: which area was checked
- **Finding**: what was found
- **Action**: how to fix if needed
- **Severity**: Critical, High, Medium, Low

### Example Report
```
NEXTJS FRONTEND VALIDATION REPORT
==================================

✅ Structure & Setup (4/4)
  ✅ NextJS with TypeScript configured
  ✅ Required dependencies installed
  ✅ API endpoint correctly referenced

⚠️ Styling - SCSS (3/4)
  ✅ All styles in SCSS modules
  ✅ Dark theme applied
  ❌ Color variables not extracted to common file
    Action: Create colors.scss with all theme colors
    Severity: Medium

❌ Animations (2/4)
  ✅ Button hover animations working
  ❌ Page transition animations missing
    Action: Add fade transitions between pages
    Severity: High
```

## When to Run This

- **Initial setup**: After creating the project structure
- **During development**: After implementing major features
- **Before testing**: Before writing Playwright tests
- **Code review**: Before committing to version control
- **Docker prep**: Before containerizing the frontend

## Pro Tips

1. **Keep JSON config files in `public/config/`** - easy to load and modify without rebuilds
2. **Use CSS variables for theme** - wrap JSON theme in CSS custom properties for runtime changes
3. **Playwright test IDs** - use `data-testid="button-add"` consistently
4. **Performance** - lazy load three.js scenes, memoize expensive animations
5. **Accessibility** - ensure keyboard navigation works, button labels are descriptive

## Troubleshooting

**"Missing library X"**: Run `npm install framer-motion shadcn/ui lucide-react three.js`

**"Animations feel laggy"**: Check if using `will-change` CSS, reduce animation complexity, check GPU acceleration

**"API calls failing"**: Verify backend URL in environment variables, check Docker networking

**"Playwright can't find elements"**: Add `data-testid` to interactive elements, use role queries for buttons/inputs

**"Theme not consistent"**: Move all colors/sizes to JSON config, import in all components
