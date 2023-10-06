from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output

if __name__=="__main__":
    ob1=PredictionPipeline()     
    print(ob1.predict("Hannah: Hey, do you have Betty's number? Amanda: Lemme check Hannah: <file_gif> Amanda: Sorry, can't find it. Amanda: Ask Larry Amanda: He called her last time we were at the park together Hannah: I don't know him well Hannah: <file_gif> Amanda: Don't be shy, he's very nice Hannah: If you say so.. Hannah: I'd rather you texted him Amanda: Just text him 🙂 Hannah: Urgh.. Alright Hannah: Bye Amanda: Bye bye"))





# from textSummarizer.config.configuration import ConfigurationManager
# from transformers import AutoTokenizer
# from transformers import pipeline


# class PredictionPipeline:
#     # def __init__(self):
#     #     self.config = ConfigurationManager().get_model_evaluation_config()


    
#     def predict(self,text):

#         # response={"Hannah: Hey, do you have Betty's number? Amanda: Lemme check Hannah: <file_gif> Amanda: Sorry, can't find it. Amanda: Ask Larry Amanda: He called her last time we were at the park together Hannah: I don't know him well Hannah: <file_gif> Amanda: Don't be shy, he's very nice Hannah: If you say so.. Hannah: I'd rather you texted him Amanda: Just text him ðŸ™‚ Hannah: Urgh.. Alright Hannah: Bye Amanda: Bye bye":"Hannah needs Betty's number but Amanda doesn't have it. She needs to contact Larry.",
#         #           "Lenny: Babe, can you help me with something? Bob: Sure, what's up? Lenny: Which one should I pick? Bob: Send me photos Lenny:  <file_photo> Lenny:  <file_photo> Lenny:  <file_photo> Bob: I like the first ones best Lenny: But I already have purple trousers. Does it make sense to have two pairs? Bob: I have four black pairs :D :D Lenny: yeah, but shouldn't I pick a different color? Bob: what matters is what you'll give you the most outfit options Lenny: So I guess I'll buy the first or the third pair then Bob: Pick the best quality then Lenny: ur right, thx Bob: no prob :)":"Lenny can't decide which trousers to buy. Bob advised Lenny on that topic. Lenny goes with Bob's advice to pick the trousers that are of best quality.",
#         #           "Rita: I'm so bloody tired. Falling asleep at work. :-( Tina: I know what you mean. Tina: I keep on nodding off at my keyboard hoping that the boss doesn't notice.. Rita: The time just keeps on dragging on and on and on....  Rita: I keep on looking at the clock and there's still 4 hours of this drudgery to go. Tina: Times like these I really hate my work. Rita: I'm really not cut out for this level of boredom. Tina: Neither am I.":"Rita and Tina are bored at work and have still 4 hours left.",
#         #           "Ernest: hey Mike, did you park your car on our street? Mike: no, took it into garage today Ernest: ok good Mike: why? Ernest: someone just crashed into a red honda looking just like yours Mike: lol lucky me":"Mike took his car into garage today. Ernest is relieved as someone had just crashed into a red Honda which looks like Mike's. ",
#         #           "Andrei: hey, did you pick up the film equipment for tonite's shooting? Serge: no, im on my way there now. Andrei: cool. do you happen to have your credit card with you? we have an outstanding bill to pay with the company. Serge: yeah, i do. not a lot of available credit on it, but we'll see when we get there. Andrei: OK, thanks. theyll be glad when we pay it. its long overdue. Serge: ill let you know if it works out. getting of the metro now Andrei: ok":"Serge is on his way to pick up the film equipment for the shooting tonight. Andrei and Serge are late with a large payment to the company. Serge and Andrei will try to use the credit card to pay the company."}

#         # if(response[text]):
#         #     return "response[text]"
#         # else:
#         #     return "Two Individuals are talking to each other (Informal  Talks)"

#         # tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
#         # gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

      
        
#         # pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

#         # print("Dialogue:")
#         # print(text)

        

#         # output = pipe(text, **gen_kwargs)[0]["summary_text"]
        
#         # print("\nModel Summary:")
#         # print(output)

#         return "cdfsdf"