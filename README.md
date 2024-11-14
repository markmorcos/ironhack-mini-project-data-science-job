# Data Science Job Analysis

## Project Overview 

### Business Case Introduction

_We are a recruitment consulting firm hired by a company that looking to renew its data team. The company called us to optimize its recruitment process, allowing it to select top candidates in the market and present them with a more attractive offer than competitors. Our objective is to provide recruitment strategy that not only identifies highly skilled talent but also ensures that our client’s offer stands out in terms of compensation, professional growth opportunities, and work environment. This will help our client position itself as a leader in the market for data talent acquisition, attracting and retaining the best professionals to drive their data initiatives forward._ 


## Data Source
- [Data Science Job](https://www.kaggle.com/datasets/brsahan/data-science-job)

## Hypothesis

1. Jobs in specialized categories (e.g., Machine Learning, AI) offer higher salaries than general data science roles.
2. Full-time roles offer higher salaries than part-time, contract, or freelance positions.
3. Remote positions offer higher salaries compared to in-person or hybrid roles.
4. Today, it may be more beneficial for companies to relocate their data teams to countries with lower salary costs or to hire employees remotely. 

## Analysis Overview

- **Some Jobs Category offer higher salaries**
	- There are very small differences between salaries, when it comes to Data Science, Analysis, ML/AI or Engineering jobs
- **Full-time roles offer higher salaries**
	- Our hypothesis that full-time roles offer higher salaries than part-time, contract, or freelance positions was proven wrong, the highest average salary was in part-time, then freelance and full-time jobs.
- **Remote position offer higher salaries**
	- Remote roles do not offer the highest salaries.
- **Benefit of companies that employ their team in other countries**
	- it is indeed more cost-effective for companies to hire remote employees, as it allows them to reduce salary expenses while accessing a broader talent pool.


## Conclusion

The analysis reveals that some job categories offer higher salaries, with only slight differences noted among Data Science, Analysis, ML/AI, and Engineering roles. Contrary to the initial hypothesis, part-time positions have the highest average salaries, followed by freelance and then full-time roles. Remote roles do not offer the highest salaries. Companies employing remote teams in other countries benefit from cost savings and access to a wider talent pool.

## Presentation 
- [Presentation](https://www.canva.com/design/DAGWSFADUfY/VH4plhxxrQSLMhSpfhkQAw)

## Installation

<details>
  <summary>Click to see the list of functions</summary>
1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/repository_name.git
```

2. **Install UV**

If you're a MacOS/Linux user type:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If you're a Windows user open an Anaconda Powershell Prompt and type :

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. **Create an environment**

```bash
uv venv
```

3. **Activate the environment**

If you're a MacOS/Linux user type (if you're using a bash shell):

```bash
source ./venv/bin/activate
```

If you're a MacOS/Linux user type (if you're using a csh/tcsh shell):

```bash
source ./venv/bin/activate.csh
```

If you're a Windows user type:

```bash
.\venv\Scripts\activate
```

4. **Install dependencies**:

```bash
uv pip install -r requirements.txt
```

</details>

##
