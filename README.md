# This is a demo project which takes the next step after my last post.

## Prelude
I established that different agents can be used to do different tasks where developers can steer using the right spec and get the job done.
Link to the last post: [Build a Full-stack Multi-tech app using Agents, start Problem Engineering](https://www.linkedin.com/posts/vickybiswas_experience-for-yourself-and-let-me-know-how-activity-7431746932739559424-sU-I)
The post showed different agents to establish the strengths for various players in the development team by doing things hands on.
You however were working with multiple tools for the hands on experience. That was designed to show their strengths.
Today let's use one central tool that runs multiple subagents to build a frontend (simple HTML/CSS/JS) and backend (python docker).

## Running all from one command line
I talked last time about about High-level outcome, Constraining details, and Validation methods in my last post.
We will directlly push High-level outcome as our instructions.
We will put Constraining details as our config.
We will create Validation methods as our skills.

We will try to keep costs zero for this demo but subscriptions woulld help.

This is not to establish best practice but as an eye opener for AI nay sayers or people partially commited to "Problem Engineering".
We will do it for:
* [A new project](#new-project)
* [An existing project](#extablished-projects)
* [Continuous improvement](#continuous-improvement)


## Walkthrough
We will create a Stranger Things Calculator
* frontend - docker 3004
    * react
* backend - docker 8004
    * python

### Setup
* Login to github and clone the main branch of this repo https://github.com/vickybiswas/agent-demo
* create a .env file with -> GITHUB_PAT=your-github-pat (create in Githuv > Settings > Developer > Personal access tokens)
* Signup for openrouter https://openrouter.ai./ for free LLM access. Create a Key.
* Setup claude code - https://github.com/anthropics/claude-code
* Install claude cli ->  curl -fsSL https://claude.ai/install.sh | bash
* create setup openrouter in claude code - 
Automatically setup Claude Code for repeatable defaults
* claude plugin install @anthropic/[plugin-name](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)
    * frontend-design -> claude plugin install @anthropic/frontend-design
    * pr-review-toolkit -> claude plugin install @anthropic/pr-review-toolkit
    * security-guidance -> claude plugin install @anthropic/security-guidance
* claude mcp - claude mcp list
    * code-review-graph
        * claude plugin marketplace add tirth8205/code-review-graph && claude plugin install code-review-graph@code-review-graph
    * playwright
        * npm install @playwright/mcp && claude mcp add playwright npx @playwright/mcp@latest
    * github
        * claude mcp add-json github '{"type":"http","url":"https://api.githubcopilot.com/mcp","headers":{"Authorization":"Bearer '"$(grep GITHUB_PAT .env | cut -d '=' -f2)"'"}}'
* skill
    * (added to repo already) repo-setup - Creates CLAUDE.md and skills and other things which gives it constraints to work in. These should be created by teams and changes merged in with a maximum gap of 1 week. That keeps all code aligned with what team wants.
    * (added to repo already) fix-github-issue - This uses MCP servers to handle github Issues, PR etc. Teams should build this as needed.   
    * nextjs-validator - typescript NextJS Architect understands visual asthetics and coding best practices and how to handle and fix issues.
    * fastapi-validator - Python FastAPI Architect understands best practices and how to handle and fix issues.
    * docker-validator - DevOps Specialist understands best practices for Docker and Orchestration, and how to handle and fix issues.
* hook
    * validate and generate Pep8 compliant python code using auto-pep8 as file creates
    * validate and generate ES6 compliant typescript code using prettier as file creates
* agent
    * PR and Code Reviewer uses pr-review-toolkit, security-guidance, code-review-graph mcp, github mcp, playwright mcp
    * Python FastAPI Specialist uses fastapi-validator skill, Pep8 hook, code-review-graph mcp, pr-review-toolkit, security-guidance
    * React NextJS Specialist    uses nextjs-validator skill and Prettier hook, code-review-graph mcp, pr-review-toolkit, security-guidance, frontend-design
    * Docker and Orchestration Specialist uses docker-validator skill, github mcp, security-guidance 
* Directions
    * CLAUDE.md
    * frontend/CLAUDE.md
    * backend/CLAUDE.md

### New Project
I wish to create a themed basic calculator where react nextjs frontend and python fastapi backend run on 2 docker containers on port 3004 and 8004 respectively
* Assume Endpoints
    * /add?num1=xxx&num2=yyy
    * /subtract?num1=xxx&num2=yyy
    * /multiply?num1=xxx&num2=yyy
    * /divide?num1=xxx&num2=yyy
* Create Frontend
    * Create a typescript NextJS SPA with a landing page mimicing a Basic calculator functionality with C M etc baked in. It would be themed based on. the TV show Stranger Things,  and contain animations, button interactions, background and sound effects. The site should be entirely SCSS and Json driven. No images. Use libraries like framer-motion, shadcn/ui, lucide-react, three.js etc.
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

### Extablished Projects
* Guided
    * Convert the Calculator to a Scientific Calculator
        * Create a Issue in Github
        * claude -p "Use fix-github-issue skill to fix Issue 10. Follow instructions as given in md files" --model haiku --dangerously-skip-permissions 
* You should try
    * Redesign UI in PacMan theme with sound effects - Just ask Claude
    * Change complete codebase to use variable name in TITLECASE - Change Project setup files and ask Claude to make sure pproject is following them.

### Continuous improvement
We can cover these as well
* Create Issue - Auto do primary RCA - above example does a basic job
* Raise PR - PR should be auto reviewed and commented on
* Weekly ensure documentatiion matches code - team Review and updates
* Solve Issues - Auto RCA -> Auto fix -> Auto PR -> Auto Review -> Auto Close
* Keep documentation updated - If there is a drift in code

## Concluding Remarks
We only covered the frontend and backend but we can add all others we played with in out last post as well.
Claude in not the only tool you can explore in addition to ones I introduced earlier - Codex CLI, Gemini CLI, Qodo, Windsurf, Cody, Aider, OpenCoder and may others.
Now imagine a bunch of these working together using all different models and tools - further posts will take you there as well. 
This is just a small example of what can be done with agents. The possibilities are endless are you ready?


## Appendix
### Usage and time taken on a Claude Code Pro subscription
0% 52% - Usage at Start
7m - Setup
4% 53% - Usage after Setup
25 m - Application
12% 54% - Usage after App
15 m - Enhance to Scientific
23% 55% - Usage after Enhance

### OpenRouter Free models are slower



For Later
Agent Orchestration
Netwrok AI
ip: Use git worktrees to run multiple Claude sessions in parallel.
  When you have a multi-part setup like this, structure your prompt:                                                                                                                                                                                                      
  1. What to read/analyze (the source docs)
  2. What to create (detailed list with specific requirements)                                                                                                                                                                                                            
  3. Where to put it (local vs global, which directories)     
  4. Format/style preferences (lean vs detailed, no repetition, etc.)                                                                                                                                                                                                     
  5. Success criteria (what done looks like)  