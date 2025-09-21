from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 1. Spécifier le chemin vers ton modèle fine-tuné
model_path = "./gpt2-finetuned"

# 2. Charger le tokenizer et le modèle
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# 3. Passer ton texte d’entrée
input_text = "Once upon a time"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# 4. Générer une suite de texte
output = model.generate(
    input_ids,
    max_length=100,
    num_return_sequences=1,
    do_sample=True,              # active le sampling (créativité)
    top_k=50,                    # limite aux 50 mots les plus probables
    top_p=0.95,                  # nucleus sampling
    temperature=0.9,             # contrôle de la créativité
    no_repeat_ngram_size=2,     # empêche les répétitions
    early_stopping=True
)

# 5. Afficher le texte généré
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("\n--- Texte généré ---\n")
print(generated_text)