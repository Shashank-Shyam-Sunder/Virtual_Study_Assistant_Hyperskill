# Write your code here >>>
# %%

def create_study_plan():
    subjects = {}
    while True:
        subject = input("Enter subject name: ")  # subject name
        if not subject:
            break

        while True:
            try:
                subject_time = int(input(f"Enter time allocated for {subject}: "))  # time to study in minutes

                if subject_time < 0:
                    print("Invalid input! Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Enter the subject time in integer format.")

        if subject not in subjects:
            subjects[subject] = subject_time

    if subjects: # Print nothing if subject is empty
        ## Printing your study time including breaks
        print("\nYour study plan:")

        for sub, time in subjects.items():
            print(f"{sub}: {time} minutes")

        total_study_time = sum(subjects.values())

        # Take a break of 15 minutes after every 45 minutes to boost your study
        break_time = 15
        no_breaks = total_study_time // 45
        total_time_plus_breaks = total_study_time + no_breaks * break_time
        print(f"\nTotal study time: {total_study_time} minutes")
        print(f"Total time including breaks: {total_time_plus_breaks} minutes")

        # Asking the user to enter the time spent on studying
        time_spent = int(input("\nEnter time spent studying: "))

        if time_spent >= total_study_time:
            print("\nYou have completed 100.00% of your planned study time.")
        else:
            percent_complete = round(time_spent / total_study_time * 100, 2)
            print(f"\nYou have completed {percent_complete}% of your planned study time.")
            # return subjects, percent_complete

            with open('.env', 'r') as fp:
                hf_api_key = fp.read().strip()

            from huggingface_hub import InferenceClient

            client = InferenceClient(token=hf_api_key)
            prompt = """
            I have to prepare for my {subjects} exams. I've completed {completeness:.2f}% of my curriculum. My motivation should be:
            """.format(
                subjects=','.join(subjects.keys()),
                completeness=percent_complete
            )

            response = client.text_generation(
                prompt=prompt,
                # model="meta-llama/Llama-2-7b-chat-hf",
                model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                temperature=0.01,
                max_new_tokens=50,
                seed=42,
                return_full_text=True,
            )
            print(response)


def gen_motivational_message():
    pass

#  Block to mark the entry point
if __name__ == "__main__":
    create_study_plan()
    # gen_motivational_message()





