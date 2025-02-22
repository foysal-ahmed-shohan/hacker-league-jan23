```
     _    ___   _    _            _             _                           
    / \  |_ _| | |  | | __ _  ___| | _____ _ __| |    ___  __ _  __ _  _   _  ___ 
   / _ \  | |  | |__| |/ _` |/ __| |/ / _ \ '__| |   / _ \/ _` |/ _` || | | |/ _ \
  / ___ \ | |  |  __  | (_| | (__|   <  __/ |  | |__|  __/ (_| | (_| || |_| |  __/
 /_/   \_\___| |_|  |_|\__,_|\___|_|\_\___|_|  |_____\___|\__,_|\__, | \__,_|\___|
                                                                 |___/            
```

*Created during AI Hacker League live coding session - Every Thursday at 12pm ET*

# Welcome to AI Hacker League! 🚀

AI Hacker League is a vibrant community of developers, researchers, and enthusiasts who come together to explore and push the boundaries of AI technology. Our weekly live coding sessions are more than just tutorials - they're collaborative experiments in cutting-edge AI development.

## What is AI Hacker League?

- **Live Coding Sessions**: Every Thursday at 12pm ET, we dive into hands-on AI development, building real systems in real-time.
- **Community Learning**: Join fellow AI enthusiasts in exploring new technologies and techniques.
- **Practical Experience**: Learn by doing, with real-world applications and use cases.
- **Expert Guidance**: Sessions led by experienced AI developers and researchers.

## Why Join AI Hacker League?

- 🔧 **Hands-On Experience**: Get practical experience with cutting-edge AI tools and frameworks.
- 🤝 **Networking Opportunities**: Connect with other AI developers and enthusiasts.
- 💡 **Practical Implementation Techniques**: Learn techniques not typically covered in traditional courses.
- 🚀 **Stay Ahead in AI Development**: Keep up with the latest advancements and trends in AI.
- 🛠️ **Build Your Portfolio**: Work on real AI projects that showcase your skills.
- 🎓 **Learn Best Practices**: Gain insights from experienced developers to enhance your development workflow.

## About This Project

This repository showcases a project created during one of our live sessions, demonstrating the power of AI agents using CrewAI, LangChain/LangGraph, and Aider. It's a perfect example of the practical, hands-on learning you'll experience in AI Hacker League.

---

# 🤖 Building AI Agents: From Zero to Hero
## A Comprehensive Tutorial on AI Agent Development

*Learn to build, customize, and deploy intelligent AI agents using CrewAI, LangChain/LangGraph, and Aider*

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Getting Started](#getting-started)
4. [Understanding the Components](#understanding-the-components)
5. [Customization Guide](#customization-guide)
6. [Advanced Topics](#advanced-topics)
7. [Contributing](#contributing)
8. [Join AI Hacker League](#join-ai-hacker-league)
9. [License](#license)

## Introduction
Welcome to the AI Agent Development Tutorial! This guide is designed to help you build and customize AI agents using powerful tools like CrewAI, LangChain/LangGraph, and Aider. Whether you're an entry-level developer or an experienced AI enthusiast, this tutorial will provide you with the knowledge and steps needed to create sophisticated AI-driven systems.

**Benefits of Following This Tutorial:**
- **Step-by-Step Guidance**: Clear instructions to guide you through each phase of development.
- **Detailed Descriptions**: In-depth explanations of each component and their interactions.
- **Customizable Codebase**: Learn how to modify and extend the code to suit your specific needs.
- **Practical Examples**: Real-world examples to demonstrate the application of concepts.
- **Enhanced Understanding**: Gain a comprehensive understanding of AI agent architecture and functionality.

## Project Overview
The project implements a modular AI agent system with the following key features:
- **ReACT (Reasoning and Acting) Methodology**: Structured problem-solving approach integrating reasoning and action-taking.
- **Multi-Agent Coordination using CrewAI**: Allows multiple agents to work together seamlessly.
- **Task Configuration and Agent Role Definition**: Defines specific tasks and assigns roles to agents for efficient execution.
- **Interactive Command-Line Interface with Cyberpunk Styling**: Engaging interface for interacting with the system.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.8+**: Python programming language.
- **Poetry**: Dependency management and packaging tool.

```bash
# Clone the repository
git clone https://github.com/ruvnet/hacker-league-jan23
cd hacker-league-jan23

# Install dependencies
poetry install
```

### Environment Setup
1. **Configure Environment Variables**

Copy the sample environment file and set up your environment variables:

```bash
cp env.sample .env
```

Open `.env` in your preferred editor and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

2. **Setting Up OpenRouter API Key**

The project utilizes OpenRouter for certain AI functionalities. You will be prompted to enter your OpenRouter API key during the initial run. You can obtain this key from [OpenRouter's website](https://openrouter.ai/keys).

## Running the Agent

### Using the Interactive Menu
The project includes a user-friendly command-line interface (`start.sh`) to manage various operations.

```bash
./start.sh
```

**Menu Options:**
1. **Install Neural Dependencies**: Ensures all required Python packages are installed.
2. **Activate AI Cores (Default Mode)**: Runs the AI agent with default settings.
3. **Activate AI Cores (Custom Mode)**: Allows you to input custom prompts and select specific tasks.
4. **Enter Sleep Mode**: Safely shuts down the AI cores.

### Direct Execution with Custom Prompt
For more control, you can directly run the agent with custom arguments:

```bash
poetry run python src/hello_world/main.py --prompt "Your prompt here" --task research
```

**Arguments:**
- `--prompt`: Specify the prompt/question for the AI system. *(Default: "Tell me about yourself")*
- `--task`: Define the type of task to perform. *(Options: research, execute, both; Default: both)*

## Configuration Management

The project includes a powerful configuration management script (`coding-admin.sh`) that provides an interactive interface for customizing and managing your AI development environment.

### Running the Configuration Manager

```bash
./coding-admin.sh
```

### Key Features

1. **AI Chat Assistant**
   - Get help with settings configuration
   - Development workflow guidance
   - Configuration recommendations
   - Chat settings management

2. **Model Settings**
   - Configure main model (GPT-4, Claude-3, etc.)
   - Set editor model preferences
   - Manage model aliases
   - Configure SSL and API settings

3. **Git Integration**
   - Toggle auto-commits
   - Configure commit messages
   - Set repository preferences
   - Manage author attribution

4. **Output Customization**
   - Toggle dark/light mode
   - Configure color schemes
   - Set code themes
   - Manage diff display

5. **History Management**
   - Configure input/chat history
   - Set history file locations
   - Manage chat history restoration

6. **Development Tools**
   - Configure linting settings
   - Set up testing preferences
   - Manage environment variables
   - Configure shell commands

7. **Performance Settings**
   - Configure cache settings
   - Manage map settings
   - Set up analytics preferences

8. **OpenRouter Integration**
   - Configure API keys
   - Set up model preferences
   - Manage development workflows

### Configuration Files

The script manages several configuration files:
- `.aider.conf.yml`: Main configuration file
- `openrouter_config.yml`: OpenRouter-specific settings
- `.env`: Environment variables and API keys

### Common Configuration Tasks

1. **Setting Up OpenRouter**
```bash
./coding-admin.sh
# Select option 2 (OpenRouter Settings)
# Follow prompts to enter your API key
```

2. **Configuring Model Settings**
```bash
./coding-admin.sh
# Select option 4 (Model Settings)
# Choose your preferred model and settings
```

3. **Customizing Output**
```bash
./coding-admin.sh
# Select option 6 (Output Settings)
# Configure themes and display preferences
```

The configuration manager provides an intuitive interface for managing all aspects of your AI development environment. Use the interactive menus to explore and customize settings according to your needs.

## Understanding the Components

### 1. Agent Configuration (`src/hello_world/config/agents.yaml`)
Defines agent roles and capabilities:

```yaml
research_analyst:
  name: Research Analyst
  model: deepseek
  temperature: 0.7
  description: |
    Expert in analyzing information and providing insights using ReACT methodology.
```

### 2. Task Configuration (`src/hello_world/config/tasks.yaml`)
Defines tasks and their requirements:

```yaml
research:
  description: Conduct research and analysis
  tools:
    - web_search
    - document_analysis
```

### 3. Main Agent Logic (`src/hello_world/main.py`)
Orchestrates the agent system:

```python
def run():
    args = parse_args()
    crew = HelloWorldCrew()
    result = crew.run(prompt=args.prompt, task_type=args.task)
```

### 4. Crew Management (`src/hello_world/crew.py`)
Handles agent coordination and task execution:

```python
class HelloWorldCrew:
    def __init__(self):
        self.crew = Crew(
            agents=[self.research_analyst],
            tasks=[self.research_task]
        )
```

## Customization Guide

This section will guide you through customizing the AI agent system to better fit your specific needs. We'll cover adding new agents, defining new tasks, and creating custom tools.

### 1. Adding New Agents
To create a new agent type:

1. **Define Agent Configuration**

Add a new agent configuration in `agents.yaml`:

```yaml
code_expert:
  name: Code Expert
  model: gpt-4
  temperature: 0.3
  description: |
    Specialized in code analysis and generation.
```

2. **Implement Agent Logic**

Create the agent implementation in `crew.py`:

```python
def create_code_expert(self):
    return Agent(
        role="Code Expert",
        goal="Generate and analyze code efficiently",
        backstory="Expert software developer with broad language expertise",
        tools=[self.code_analysis_tool]
    )
```

### 2. Adding New Tasks
To implement new task types:

1. **Define Task Configuration**

Add a new task in `tasks.yaml`:

```yaml
code_review:
  description: Perform code analysis and review
  tools:
    - code_analysis
    - best_practices_check
```

2. **Implement Task Handler**

Create the task handler in `crew.py`:

```python
def code_review_task(self):
    return Task(
        description="Analyze code for quality and improvements",
        tools=self.get_code_tools()
    )
```

### 3. Adding Custom Tools
To create new tools for agents:

1. **Develop the Tool**

Create a new tool in `tools/custom_tool.py`:

```python
class CodeAnalysisTool:
    def analyze_code(self, code: str) -> dict:
        # Implementation
        return {
            "complexity": calculate_complexity(code),
            "suggestions": generate_suggestions(code)
        }
```

2. **Register the Tool with Agents**

Register the new tool in `crew.py`:

```python
def get_code_tools(self):
    return [
        Tool(
            name="code_analysis",
            func=self.code_analysis_tool.analyze_code,
            description="Analyzes code quality and structure"
        )
    ]
```

## Advanced Topics

Explore more complex functionalities to extend the AI agent system.

### 1. Implementing Custom Workflows
Create specialized workflows by combining agents and tasks:

```python
class CustomWorkflow:
    def __init__(self):
        self.research_agent = ResearchAnalyst()
        self.code_agent = CodeExpert()
        
    def execute(self, prompt):
        research_results = self.research_agent.analyze(prompt)
        code_implementation = self.code_agent.implement(research_results)
        return code_implementation
```

### 2. Integration with External Services
Enhance agent capabilities by integrating external APIs:

```python
class ExternalServiceTool:
    def __init__(self, api_key):
        self.client = ExternalAPI(api_key)
        
    def fetch_data(self, query):
        return self.client.search(query)
```

### 3. Custom Output Formatting
Implement custom formatters for agent outputs to improve readability:

```python
class OutputFormatter:
    def format_research(self, results):
        return f"""
╔══════════════════════════════════════════════════════════════════╗
║                    RESEARCH FINDINGS                             ║
╚══════════════════════════════════════════════════════════════════╝

{results}
"""
```

## Contributing
We welcome contributions to enhance this project. Follow these steps to contribute:

1. **Fork the Repository**

    Click the "Fork" button at the top-right corner of the repository page to create your own copy.

2. **Create a Feature Branch**

    ```bash
    git checkout -b feature/YourFeatureName
    ```

3. **Make Your Changes**

    Implement your feature or bug fix. Ensure your code follows the project's coding standards.

4. **Commit Your Changes**

    ```bash
    git commit -m "Add feature: YourFeatureName"
    ```

5. **Push to Your Fork**

    ```bash
    git push origin feature/YourFeatureName
    ```

6. **Submit a Pull Request**

    Navigate to the original repository and click "New pull request". Describe your changes and submit.

## Join AI Hacker League
Be a part of our thriving AI Hacker League community! Join us every Thursday at 12pm ET for live coding sessions where we build and explore AI systems together. Whether you're a beginner or an expert, there's something for everyone.

**Why Join?**
- **Collaborative Learning**: Work alongside other AI enthusiasts and learn collaboratively.
- **Real-Time Feedback**: Get immediate insights and feedback on your work.
- **Stay Updated**: Keep up with the latest tools and technologies in AI.

Follow [@rUv](https://github.com/ruvnet) on GitHub for updates and announcements.

## License
This project is open source and available under the [MIT License](LICENSE).

Created by rUv, cause he could. 🚀
