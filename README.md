# This is a demo project which takes the next step after my last post.

## Prelude
I established that different agents can be used to do different tasks where developers can steer using the right spec and get the job done.
Link to the last post: [Build a Full-stack Multi-tech app using Agents, start Problem Engineering](https://www.linkedin.com/posts/vickybiswas_experience-for-yourself-and-let-me-know-how-activity-7431746932739559424-sU-I)
The post showed different agents to establish the strengths for various players in the development team by doing things hands on.
You however were introduced to multiple tools for the hands on experience.
Today let's use one central tool thaa ruuns multiple agents to build a frontend (simple HTML/CSS/JS) and backend (python docker).

## Running all from one command line

I talked about High-level outcome, Constraining details, and Validation methods in my last post.
We will directlly push High-level outcome as our instruction.
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
Use google account to login to github and create an empty repo
https://github.com/vickybiswas/agent-demo
Signup for openrouter https://openrouter.ai./ using your google account
Setup claude code - https://github.com/anthropics/claude-code
* curl -fsSL https://claude.ai/install.sh | bash
* setup openrouter in claude code - 
Enhance Claude Code
* claude plugin install @anthropic/[plugin-name](https://github.com/anthropics/claude-code/blob/main/plugins/README.md)
    * frontend-design
    * pr-review-toolkit
    * security-guidance
* claude mcp - claude mcp list
    * code-review-graph
        * claude plugin marketplace add tirth8205/code-review-graph && claude plugin install code-review-graph@code-review-graph
    * playwright
        * npm install @playwright/mcp && claude mcp add playwright npx @playwright/mcp@latest
    * github
        * claude mcp add-json github '{"type":"http","url":"https://api.githubcopilot.com/mcp","headers":{"Authorization":"Bearer '"$(grep GITHUB_PAT .env | cut -d '=' -f2)"'"}}'
* skill
    * 
* hook
    * validate and generate Pep8 compliant python code using auto-pep8 as file creates
    * validate and generate ES6 compliant typescript code using prettier as file creates
* agent
    * PR Review
    * Python FastAPI Specialist
    * React NextJS Specialist
    * Docker and Orchestration Specialist
* command
    * /fix-next - Pick next Issue from github and fix it and create a PR
* Directions
    * CLAUDE.md
    * frontend/CLAUDE.md
    * backend/CLAUDE.md

Note: https://www.reddit.com/r/LLMDevs/comments/1rwh2yd/your_claudemd_files_in_subdirectories_might_not/

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
* Project wide Styke Change
* Add new features
    * factorial, squareroot, square
    * redesign UI in PacMan theme with sound effects 

### Continuous improvement
* Create Issue
* Raise PR
* Weekly ensure documentatiion matches code
* Solve Issues

## Concluding Remarks

We only covered the frontend and backend but we can add all others we played with in out last post as well.
This is just a small example of what can be done with agents. The possibilities are endless are you ready?



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

   Perfect! I've successfully generated the complete repository setup based on INSTRUCTIONS.md and the repo-setup skill framework. Here's what was created:

  ✅ Setup Complete - All Files Generated                                                                                                                                                                                                                           
  
  1. Five Specialized Agents (.claude/agents/)                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                  
  - 1-pr-review.md - Code review specialist                                                                                                                                                                                                                         
  - 2-fastapi-specialist.md - Backend expert (Python FastAPI)                                                                                                                                                                                                     
  - 3-nextjs-specialist.md - Frontend expert (React/NextJS)                                                                                                                                                                                                         
  - 4-devops-specialist.md - Docker orchestration expert                                                                                                                                                                                                            
  - 5-qa-specialist.md - Testing and coverage expert                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                    
  2. Three Domain Validators (.claude/skills/*/SKILL.md)                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                  
  - fastapi-validator - Backend code quality (PEP8, testing, CORS, coverage)                                                                                                                                                                                        
  - nextjs-validator - Frontend code quality (TypeScript strict, animations, CORS)                                                                                                                                                                                
  - docker-validator - Docker orchestration (Dockerfiles, compose, networking)                                                                                                                                                                                      
                                                                                                                                                                                                                                                                    
  3. Orchestration Guides                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                    
  - CLAUDE.md (Root) - 3-step orchestration with parallel execution strategy for Frontend + Backend                                                                                                                                                                 
  - CREATE.md - Docker phases (Dockerfiles, docker-compose, integration testing)                                                                                                                                                                                  
  - REGRESSION.md - MANDATORY 6-phase pre-PR checklist (prevents integration issues from reaching GitHub)                                                                                                                                                           
  - STARTUP.md - 3 options for starting services (Docker, local dev, automated script)                                                                                                                                                                              
                                                                                                                                                                                                                                                                    
  4. Domain Implementation Guides                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                    
  - frontend/CLAUDE.md - 7 phases (NextJS setup → animations → backend integration → tests → strict validation)                                                                                                                                                     
  - backend/CLAUDE.md - 8 phases (FastAPI setup → CORS → routes → unit tests → API tests → 100% coverage → PEP8 → docs)
                                                                                                                                                                                                                                                                    
  5. Environment & Configuration                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                    
  - .env.example - Docker Compose environment variables                                                                                                                                                                                                             
  - .env.local.example - Local development environment variables                                                                                                                                                                                                  
  - .github/pull_request_template.md - Links to REGRESSION.md (enforces checklist)                                                                                                                                                                                  
                                                                                                                                                                                                                                                                    
  ⭐ Key Highlights
                                                                                                                                                                                                                                                                    
  Parallelization Strategy                                                                                                                                                                                                                                          
  
  - Frontend + Backend agents spawn together (parallel execution)                                                                                                                                                                                                   
  - Within-phase testing: Independent tests run in parallel (unit tests, API tests, Playwright tests)                                                                                                                                                             
  - Result: 5-10x faster execution vs sequential                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                    
  REGRESSION.md (Mandatory Pre-PR Gate)                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                    
  Prevents issues like #3 (CORS/integration problems):                                                                                                                                                                                                              
  - Phase 1: Local setup verification                                                                                                                                                                                                                             
  - Phase 2: CORS & integration testing                                                                                                                                                                                                                             
  - Phase 3: Unit/API tests (100% coverage)                                                                                                                                                                                                                       
  - Phase 4: Frontend tests (TypeScript strict, build, Playwright)                                                                                                                                                                                                  
  - Phase 5: Docker orchestration verification                                                                                                                                                                                                                    
  - Phase 6: Code quality checks                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                    
  All phases required before PR → no integration issues slip through to GitHub                                                                                                                                                                                      
                                                                                                                                                                                                                                                                    
  DRY & SRP Principles                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                    
  - Each file has single responsibility (agents define roles, skills validate domains, CLAUDE.md files orchestrate)                                                                                                                                                 
  - No duplication across files (one source of truth per concern)                                                                                                                                                                                                 
  - Frontend/Backend agents read independent files with no cross-file coordination needed                                                                                                                                                                           
                                                                                                                                                                                                                                                                    
  ---                                                                                                                                                                                                                                                               
  🚀 Ready to Build                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                    
  The repo setup is complete and ready for agent execution. You can now:
                                                                                                                                                                                                                                                                    
  1. Build the full project: claude build (spawns agents to read CLAUDE.md files)                                                                                                                                                                                   
  2. Start developing: Frontend and Backend agents work in parallel on 7 + 8 phases                                                                                                                                                                                 
  3. Test locally: STARTUP.md has 3 options for running services                                                                                                                                                                                                    
  4. Verify before PR: REGRESSION.md checklist ensures everything works                                                                                                                                                                                           
  5. Submit with confidence: PR template links to completed checklistwxit                                                                                                                                                                                               
                                                                                                                                                                                                                                                                    
  All files follow the repo-setup skill framework with proper parallelization guidance, quality gates, and integration testing requirements.                                                                                                                        
                                                                                                                                                