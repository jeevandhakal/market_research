**ASSIGNMENT - 1**

**Market Research Crew**

_Build a 2-Agent CrewAI System for Company Research_

# Objective

Build a CrewAI crew that takes a **company domain** as input (e.g., hubspot.com, salesforce.com), uses a web search tool to research the company, and generates a **strategic market research report** saved as a Markdown (.md) file in the output directory.

# Workflow

Your crew should follow this process:

- **User Input** - Accept a company domain from the user (e.g., salesforce.com)
- **Web Search** - Tool executes search to gather company information
- **Research Agent** - Processes and organizes the fetched data
- **Analysis Agent** - Creates strategic recommendations from research
- **Output** - Generate a Markdown report saved to output directory

# Requirements

## Agent 1: Researcher

- Role: Senior Market Research Analyst
- Must have access to the web search tool
- Should collect: company overview, products/services, target market, recent news, competitors

## Agent 2: Analyst

- Role: Strategic Business Analyst
- Should produce: Executive summary, SWOT analysis, strategic recommendations

## Tool Requirement

- Include at least **one web search/scrape tool**
- Suggested: SerperDevTool, WebsiteSearchTool, or custom search tool

## Tasks

- **Task 1:** Research task - assigned to Researcher agent
- **Task 2:** Analysis task - assigned to Analyst agent, outputs to .md file

## Output Format

- Final report must be saved as a **Markdown (.md) file**
- Save location: **output/** directory
- Report should include: Executive Summary, SWOT Analysis, Strategic Recommendations

**Submission:** Create a **GitHub repository** with all your code and files. Share the **repository link** as your submission.

# ⭐ Bonus Points

- **YAML Configuration** - Use YAML files instead of Python definitions
- **Clean Code/File Structure** - Organized project with separate files for agents, tasks, tools
- **Error Handling** - Implement try-catch blocks and retry logic for API failures

## Example Companies to Research

Choose any company of your choice. Some suggestions:

- hubspot.com
- salesforce.com
- stripe.com
- shopify.com
- Or any company relevant to your interests!

## Resources  
<https://docs.crewai.com/en/introduction>
