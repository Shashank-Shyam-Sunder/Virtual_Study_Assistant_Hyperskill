# Virtual Study Assistant

A Python-based tool to help you create and track study plans, with motivational messages powered by AI.

## What It Does

The Virtual Study Assistant helps you:
- Create a personalized study plan with multiple subjects
- Calculate total study time including recommended breaks
- Track your study progress
- Generate AI-powered motivational messages based on your progress using the TinyLlama/TinyLlama-1.1B-Chat-v1.0 model

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- `huggingface_hub` library

### Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Virtual-Study-Assistant.git
   cd Virtual-Study-Assistant
   ```

2. Install the required dependencies:
   ```
   pip install huggingface_hub
   ```

3. Create a `.env` file in the `Virtual Study Assistant/task` directory with your Hugging Face API key:
   ```
   YOUR_HUGGINGFACE_API_KEY
   ```
   You can get an API key by creating an account at [Hugging Face](https://huggingface.co/).

## How to Use

1. Navigate to the project directory:
   ```
   cd "Virtual Study Assistant/task"
   ```

2. Run the study assistant:
   ```
   python study_assistant.py
   ```

3. Follow the prompts:
   - Enter subject names (leave empty to finish adding subjects)
   - For each subject, enter the time allocated in minutes
   - After your study plan is created, enter the time you've spent studying
   - If you haven't completed 100% of your planned study time, you'll receive a motivational message

## Example Usage

```
Enter subject name: Mathematics
Enter time allocated for Mathematics: 60
Enter subject name: Physics
Enter time allocated for Physics: 45
Enter subject name: 

Your study plan:
Mathematics: 60 minutes
Physics: 45 minutes

Total study time: 105 minutes
Total time including breaks: 135 minutes

Enter time spent studying: 80

You have completed 76.19% of your planned study time.
[Motivational message will appear here]
```

## Project Information
This project was created as part of the JetBrains Academy Python track.
Learn more at [https://hyperskill.org/projects/506](https://hyperskill.org/projects/506)