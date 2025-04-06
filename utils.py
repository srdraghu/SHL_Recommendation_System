
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_assessments(data):
    texts = [f"{item['name']} {item['type']} {item['duration']}" for item in data]
    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings

def search_assessments(user_query, assessments, assessment_embeddings):
    user_embedding = model.encode([user_query])
    scores = cosine_similarity(user_embedding, assessment_embeddings)[0]
    top_indices = scores.argsort()[::-1][:10]
    return [assessments[i] for i in top_indices]
