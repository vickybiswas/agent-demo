We will create a Stranger Things Calculator running on docker
* frontend - docker 3004
    * react/nextjs
* backend - docker 8004
    * python/fastapi

### Setup
* (these 3 are installed already) claude plugin install @anthropic/[plugin-name](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)
    * frontend-design
    * pr-review-toolkit
    * security-guidance
* (these 3 are installed already) claude mcp - claude mcp list
    * code-review-graph
        * claude plugin marketplace add tirth8205/code-review-graph && claude plugin install code-review-graph@code-review-graph
    * playwright
        * npm install @playwright/mcp && claude mcp add playwright npx @playwright/mcp@latest
    * github
        * claude mcp add-json github '{"type":"http","url":"https://api.githubcopilot.com/mcp","headers":{"Authorization":"Bearer '"$(grep GITHUB_PAT .env | cut -d '=' -f2)"'"}}'
* skill
    * (installed already) repo-setup - ./claude/skills/repo-setup/SKILL.md
    * (installed already) fix-github-issue - ./claude/skills/fix-github-issue/SKILL.md    
    * nextjs-validator - ./claude/skills/nextjs-validator/SKILL.md
    * fastapi-validator - ./claude/skills/fastapi-validator/SKILL.md
    * docker-validator - ./claude/skills/docker-validator/SKILL.md
* hook
    * validate and generate Pep8 compliant python code using auto-pep8 as file creates
    * validate and generate ES6 compliant typescript code using prettier as file creates
* agent
    * PR Review
    * Python FastAPI Specialist
    * React NextJS Specialist
    * DevOps Specialist
    * QA Automation Specialist
* Directions
    * CLAUDE.md
    * frontend/CLAUDE.md
    * backend/CLAUDE.md

### Project DETAILS
I wish to create a themed basic calculator where react nextjs frontend and python fastapi backend run on 2 docker containers on port 3004 and 8004 respectively
* Assume Endpoints
    * /add?num1=xxx&num2=yyy
    * /subtract?num1=xxx&num2=yyy
    * /multiply?num1=xxx&num2=yyy
    * /divide?num1=xxx&num2=yyy
* Create Frontend
    * Create a typescript NextJS SPA with a landing page mimicing a Basic calculator functionality with C M etc baked in. It would be themed based on. the TV show Stranger Things,  and contain animations, button interactions, background and sound effects. The site should be entirely SCSS and Json driven. No images. Use libraries like framer-motion, shadcn/ui, lucide-react, three.js etc. Ensure the calculator is HIGHLY animated, responsive, and engaging - use innovative Ideas. 
    * Test
        * Do UI testing using Playwright and review code for best practices.
        * Split above instructions into a checklist and validate the code against it. 
* Create Backend
    * Create a FastAPI backend with endpoints for add, subtract, multiply, divide as assumed above. Do not use any external libraries. Ensure each route is coded in a separate file and imported in the main app file. There will be no auth and code should be following best practices.
    * Test
        * Ensure we have unit tests for every function. 
        * Ensure we have api testing for positive, negative, edge and other use cases.
        * There is a regression suite which runs the unit and api tests.
        * Split above instructions into a checklist and validate the code against it. 
* Create Orchestration
    * Create compose.yaml and Dockerfiles for frontend and backend. Ensure frontend and backend can talk to each other. Mount the code as volumes and make them hot reloadable.
    * Use docker to build and run the frontend and backend using ONLY docker compose up.
    * Test
        * Redo frontend and backend tests based on this new setup.
        * Split above instructions into a checklist and validate the code against it. 
