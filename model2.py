from transformers import T5ForConditionalGeneration, T5Tokenizer
import nltk

class Summ_Model():

    def __init__(self, path: str):
        self.model = T5ForConditionalGeneration.from_pretrained(path, local_files_only=True)
        self.tokenizer = T5Tokenizer.from_pretrained(path, local_files_only=True)

    def predict(self, text: str, mode: int):
        if mode == 0:
            input_ids = self.tokenizer("summary big: " + text, return_tensors="pt")

            generated_tokens = self.model.generate(**input_ids)

            result = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

            return result[0]
        elif mode == 1:
            result = ""
            for sent in nltk.sent_tokenize(text, "russian"):
                input_ids = self.tokenizer("summary: " + sent, return_tensors="pt")

                generated_tokens = self.model.generate(**input_ids)

                res = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

                result += res + " "

            return result



# model = Summ_Model("./model2")
# # text = "Вирусы Коксаки (лат. Coxsackievirus) — несколько серотипов РНК-содержащих энтеровирусов, которые хорошо размножаются в желудочно-кишечном тракте. 29 серотипов вирусов Коксаки сейчас относят к трём видам энтеровирусов: Enterovirus A, В и С. Вирусы Коксаки являются одной из основных причин возникновения асептического менингита. После перенесённой манифестной или инаппарантной инфекции развивается стойкий типоспецифический иммунитет."
# # print(model.predict(text, 0))
