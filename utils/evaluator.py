# evaluator.py

from nltk.translate.bleu_score import sentence_bleu

def evaluate_response(prompt, response, task_type):
    """
    Evaluate response quality using BLEU or any other metrics.
    """
    # For simplicity, just use BLEU for now (you can extend it for ROUGE etc.)
    reference = [prompt.split()]  # BLEU expects a list of lists of words
    candidate = response.split()
    
    score = sentence_bleu(reference, candidate)
    return score
