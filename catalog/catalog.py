import os
import grpc

from flask import Flask, render_template

from recommendations_pb2 import MovieCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1, category=MovieCategory.SCIENCE_FICTION, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )
    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations,
    )
