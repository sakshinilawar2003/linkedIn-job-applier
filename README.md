# LinkedIn AI Auto Job Applier 🤖
This is an web scraping bot that automates the process of job applications on LinkedIn. It searches for jobs relevant to you, answers all questions in application form, customizes your resume based on the collected job information, such as skills required, description, about company, etc. and applies to the job. Can apply 100+ jobs in less than 1 hour. 




## ✨ Content
- [Introduction](#linkedin-ai-auto-job-applier-)
- [Index](#-content)
- [Install](#%EF%B8%8F-how-to-install)
- [Configure](#-how-to-configure)
- [Features](#-feature-list)

<br>

## ⚙️ How to install
1. [Python 3.10](https://www.python.org/) or above. Visit https://www.python.org/downloads/ to download and install Python, or for windows you could visit Microsoft Store and search for "Python". **Please make sure Python is added to Path in System Environment Variables**.
2. Install necessary [Undetected Chromedriver](https://pypi.org/project/undetected-chromedriver/), [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) and [Setuptools](https://pypi.org/project/setuptools/) packages. After Python is installed, OPEN a console/terminal or shell, Use below command that uses the [pip](https://pip.pypa.io/en/stable) command-line tool to install these 3 package.
  ```
  pip install undetected-chromedriver pyautogui setuptools openai
  ```
3. Download and install latest version of [Google Chrome](https://www.google.com/chrome) in it's default location, visit https://www.google.com/chrome to download it's installer.
4. Clone the current git repo or download it as a zip file, url to the latest update https://github.com/GodsScion/Auto_job_applier_linkedIn.
5. (Not needed if you set `stealth_mode = True` in `config/settings.py` ) Download and install the appropriate [Chrome Driver](https://googlechromelabs.github.io/chrome-for-testing/) for Google Chrome and paste it in the location Chrome was installed, visit https://googlechromelabs.github.io/chrome-for-testing/ to download.
  <br> <br>
  ***OR*** 
  <br> <br>
  If you are using Windows, click on `windows-setup.bat` available in the `/setup` folder, this will install the latest chromedriver automatically.
6. If you have questions or need help setting it up or to talk in general, join the github server: https://discord.gg/fFp7uUzWCY

[back to index](#-content)

<br>

## 🔧 How to configure
1. Open `personals.py` file in `/config` folder and enter your details like name, phone number, address, etc. Whatever you want to fill in your applications.
2. Open `questions.py` file in `/config` folder and enter your answers for application questions, configure wether you want the bot to pause before submission or pause if it can't answer unknown questions.
3. Open `search.py` file in `/config` folder and enter your search preferences, job filters, configure the bot as per your needs (these settings decide which jobs to apply for or skip).
4. Open `secrets.py` file in `/config` folder and enter your LinkedIn username, password to login and OpenAI API Key for generation of job tailored resumes and cover letters (This entire step is optional). If you do not provide username or password or leave them as default, it will login with saved profile in browser, if failed will ask you to login manually.
5. Open `settings.py` file in `/config` folder to configure the bot settings like, keep screen awake, click intervals (click intervals are randomized to seem like human behavior), run in background, stealth mode (to avoid bot detection), etc. as per your needs.
6. (Optional) Don't forget to add you default resume in the location you mentioned in `default_resume_path = "all resumes/default/resume.pdf"` given in `/config/questions.py`. If one is not provided, it will use your previous resume submitted in LinkedIn or (In Development) generate custom resume if OpenAI APT key is provided!
7. Run `runAiBot.py` and see the magic happen.
8. If you have questions or need help setting it up or to talk in general, join the github server: https://discord.gg/fFp7uUzWCY

[back to index](#-content)

<br>



 
  [back to index](#-content)
  

## 🤩 Feature List
(I'm yet to complete the documentation, I'm adding in more features, still in development)

#### General Features 🚀:

- Opens browser with default logged in google account (Yet to test with browsers having multiple profiles)
- **Auto Login**: If configured or already saved in browser (not saved passwords)
- Apply filters (Salary, Companies, Experience Level,... ) Must config
- Region specific searches
- Opens job search and searches key words
- Easy applies
- Auto Answers questions answered in config
- Collects urls of career page if have to Apply externally
- Collects HR Info
- Collects skills required (In Development)
- Collects experience required and skips if not applicable to you, must be configured
- Auto Filters jobs based on your experience and black list key words
- Skips blacklisted jobs
- Can be configured to skip jobs requiring Security Clearance
- You can add exceptions to blacklist key words
- Only applies to filtered jobs
- Auto selects next pages until it hits the quota you configured
- Selects your default resume
- Auto Submits
- Saves all the info of applied jobs, failed to apply jobs in excels and logs
- Takes screenshot of questions answered to fail, for future debugging
- Saves info of all questions, it's options, previous answer and current answer in application
- Option to overwrite previous answers
- Continuous applications non stop (beta)
- No need for fear of missing out, Goes through all possible filters and sorts combinations with each cycle if configured (Most Recent, Most Relevant, Newest First, Past 24 Hrs, Past Month, Past Week etc)
- Option to randomize the search order
- Run in background, headless browser
- Auto collects a looooooooooooooooooot of info about your jobs, check applied-jobs.excel and failed_jobs.excel for info after each run.
- Optional pause before submit application.
- Optional pause if stuck at a question.




#### Stealth features 🥸🤫:  
- Undetected Chromedriver to bypass anti-bot scripts (Browser, Undetected ChromeDriver versions must be compatible) (Beta) {If problem occurs uninstall and install undetected chromedriver, update browser, selenium and chromedriver}
- Click intervals can be randomized and increased to avoid suspicions
- Smooth Scrolls the elements into view before click

#### Upcoming Features or currently in development 🤖🛠️:
- Answer questions with help of chatGpt or other LLMs
- Humanize clicks and mouse movements for stealth 
- Auto send personalized messages to HR that accept messages
- Custom resume generator based on Skills required gathering (In Development)
- Customize resume for every job using LLMs ChatGPT (In Development). (Halted decision pending, will probably implement api or utilize other LLMs or Web Scrape)



<br>




#### ℹ️ Version: 24.12.29.12.30 Stable Preview

---

[back to the top](#linkedin-ai-auto-job-applier-)
