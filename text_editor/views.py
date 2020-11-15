from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'index.html')


def analyze(request):
	
	#get the text
	djtext=request.POST.get('text')
	
	
	# get checkbox value
	copied = request.GET.get('copy')	
	print(copied)
	
	
	removepunc=request.POST.get('removepunc','off')
	
	uppercase=request.POST.get('uppercase','off')
	
	newlineremover=request.POST.get('line-remover','off')
	
	extraspaceremover=request.POST.get('space-remover','off')
	
	chr_counter = request.POST.get('count','off')
	
	#check which box value is on 			
	if removepunc == 'on':
		analyzed=''
		for char in djtext:
			if char.isalnum() or char.isspace():
				analyzed += char
		djtext = analyzed
		context={'purpose':'remove punctuation','analyzed_text':analyzed}

	if uppercase == 'on':
		analyzed=''
		for char in djtext:
				analyzed += char.upper()
		context={'purpose':'In UpperCase','analyzed_text':analyzed}
		djtext = analyzed	
			
	if newlineremover == 'on':
			analyzed=''
			s=djtext.split('\r\n')
			for char in s:
						analyzed += char +' '
			context={'purpose':'line remover','analyzed_text':analyzed}
			djtext = analyzed

												
	if extraspaceremover == 'on':
			analyzed=''
			lines = djtext.split('\r\n')
			
			for line in lines:
				words = line.split()
				analyzed += ' '.join(words) + '\r\n'

			context={'purpose':'extra space  remover','analyzed_text':analyzed}
			djtext = analyzed
			
			
	if chr_counter == 'on':
		count = 0
		for char in djtext:
			count +=1
		context={'purpose':'Total chr : ','analyzed_text':analyzed + '\n' + str(count)}
			
												
																
	if   removepunc ==uppercase == newlineremover == extraspaceremover == chr_counter != 'on':
		context={'purpose':'Not applied','analyzed_text':djtext}

	
	return render(request,'analyze.html',context)
	
	
	
	