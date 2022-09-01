import sys
import time
import os


f = open("data.txt", "a")

print("Write \"stop\" as any input to end the session!")

def newinput(): #just like input() but closes the file and terminates execution when "stop" is inputted
	x=input()
	if x=="stop":
		f.close()
		sys.exit("You asked me to stop. I'll obey you, old man... for now...")
	return x



while True:
	os.system("say 'new question time you dum-dum'") 
	print("enter your new fermi question")
	question = newinput()

	print("what is the answer?")
	answer = newinput()

	print("what's the reasonable range of answers? please try to answer either like \"1.36 doubling\" or \"20 absolute\"") #not quite sure what one should mean by this "reasonable range", one formalization would be to look at median guess of ppl who guess too little and median guess of people who guess too much, and average the diffs of these two from the true answer to find the radius of the reasonable range, or maybe just standard deviation, in scoring we might give 0.5 to edges of reasonable range and extrapolate the rest between 1 for the correct answer and 0 asymptotically (in log space if in terms of doublings)
	rang = newinput()

	print("what is the type of your question? e.g., mathematics, technology; feel free to come up with a new type on a similar level of generality")
	topic = newinput()

	f.write(question+"\n")
	f.write(answer+"\n")
	f.write(rang+"\n")
	f.write(topic+"\n")

	print("enter rest time (in minutes) before next question")
	t = int(newinput())
	for remaining in range(t*60, 0, -1):
		sys.stdout.write("\r")
		sys.stdout.write("{} minutes and {} seconds remaining".format(remaining//60,remaining%60)) 
		sys.stdout.flush()
		time.sleep(1)







