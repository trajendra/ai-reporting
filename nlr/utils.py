import openai
import csv



# Read the CSV file
def read_csv_file(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = []
        for row in csv_reader:
            rows.append(row)
        return rows

# Ask question to OpenAI
def ask_question(question, context):
    model_engine = "text-davinci-002"
    prompt = f"{question}\nContext: {context}\nAnswer:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=25,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer



def get_query_results(uploaded_file, query):
    
    openai.api_key = "ENTER YOUR OPENAI API KEY HERE"
    with uploaded_file.open() as f:
       data = f.read().decode("utf-8")
    
    context = str(data)
    answer = ask_question(query, context)
    print(answer)

    results=answer
    return results
