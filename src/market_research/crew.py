from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai import LLM
from typing import List

# Use 1.5-flash for better free-tier stability
# Added requests_per_minute to handle the 'wait' automatically
llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.1,
    requests_per_minute=10, 
)

@CrewBase
class MarketResearch():
    """MarketResearch crew"""

    agents: List[Agent] 
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],
            llm=llm,
            verbose=True,
            max_iter=2, # Increased slightly to allow for one retry if a tool fails
            allow_delegation=False
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            llm=llm,
            verbose=True,
            max_iter=1,
            allow_delegation=False
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='output/{company_domain}_report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )