from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'myapp/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'myapp/home.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})

from django.shortcuts import render
from django.http import HttpResponse

import openai

@csrf_exempt
def index(request):
    data = {
        "model": "text-davinci-003",
        "prompt": "write a resume for web devlpoer in which first write skills in which write technologies name only, expirence, summary",
        "max_tokens": 4000,
        "temperature": 0,
        # "top_p": 1,
        # "n": 1,
        # "stream": False,
        # "logprobs": None,
        # "stop": "\n"
    }
    headers = {
        "Authorization": f"Bearer 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"
    }
    response = requests.post('https://api.openai.com/v1/completions', json=data, headers=headers)
    api_response = response.json()
    print(api_response)

    text = api_response['choices'][0]['text']

# Extract skills
    skills_start_index = text.index("Skills:")
    skills_end_index = text.index("Experience:")
    skills = text[skills_start_index:skills_end_index]

# Extract experience
    experience_start_index = text.index("Experience:")
    experience_end_index = text.index("Summary:")
    experience = text[experience_start_index:experience_end_index]

# Extract summary
    summary_start_index = text.index("Summary:")
    summary = text[summary_start_index:]

# Print the extracted information
    print("Skills:", skills)
    print("Experience:", experience)
    print("Summary:", summary)


    
    # return an HttpResponse object with the API response
    return HttpResponse(api_response)






# def index(request):
#     # Get the job title from the query parameter
#     # job_title = request.GET.get('jobTitle')
#     job_title = "flutter developer"
#     openai.api_key= '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'

#     # Make a request to the OpenAI API using the job title
#     prompt = f"Write a Resume for a {job_title}"
#     model_engine = "text-davinci-003"

#     completion = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=10,
#         temperature=0
#     )

#     # Send the response data to the webpage
#     return HttpResponse(completion.text)





