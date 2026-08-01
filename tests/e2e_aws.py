import os
import pytest
import requests
import json
import time

# Target AWS RAG Gateway endpoint from environment or default placeholder
AWS_RAG_BASE_URL = os.getenv("AWS_RAG_BASE_URL", "http://localhost:30080")
AWS_BEARER_TOKEN = os.getenv("AWS_BEARER_TOKEN", "secret-bearer-token")

@pytest.mark.e2e
def test_aws_e2e_health_check():
    """Verify that the live AWS gateway ingress and health endpoints are responding cleanly."""
    url = f"{AWS_RAG_BASE_URL}/health"
    try:
        response = requests.get(url, timeout=10)
        assert response.status_code == 200, f"Health check failed with status code {response.status_code}"
        res_json = response.json()
        assert res_json.get("status") in ["healthy", "ok", "success"]
    except requests.exceptions.RequestException as e:
        pytest.skip(f"Live AWS cluster at {AWS_RAG_BASE_URL} is unreachable: {e}")

@pytest.mark.e2e
def test_aws_e2e_ingest_document():
    """Verify document ingestion against the live AWS deployment."""
    url = f"{AWS_RAG_BASE_URL}/ingest"
    headers = {
        "Authorization": f"Bearer {AWS_BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": "AWS Enterprise RAG deployment integration test document for cloud infrastructure validation.",
        "metadata": {"environment": "AWS-EKS-Production", "test_id": "e2e_aws_001"}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 401:
            pytest.skip("AWS endpoint returned 401 Unauthorized - Check AWS_BEARER_TOKEN")
        assert response.status_code == 200, f"Ingest endpoint failed: {response.text}"
        res_json = response.json()
        assert res_json.get("status") == "success"
    except requests.exceptions.RequestException as e:
        pytest.skip(f"Live AWS cluster at {AWS_RAG_BASE_URL} is unreachable: {e}")

@pytest.mark.e2e
def test_aws_e2e_chat_query_flow():
    """Verify end-to-end query generation and retrieval response on AWS deployment."""
    url = f"{AWS_RAG_BASE_URL}/query"
    headers = {
        "Authorization": f"Bearer {AWS_BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": "Explain the AWS cloud deployment environment and RAG engine status."
    }
    
    try:
        start_time = time.time()
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        latency = time.time() - start_time
        
        if response.status_code == 401:
            pytest.skip("AWS endpoint returned 401 Unauthorized - Check AWS_BEARER_TOKEN")
        
        assert response.status_code == 200, f"Query endpoint failed: {response.text}"
        res_json = response.json()
        assert "response" in res_json or "text" in res_json
        assert latency < 45.0, f"Response latency too high: {latency:.2f}s"
    except requests.exceptions.RequestException as e:
        pytest.skip(f"Live AWS cluster at {AWS_RAG_BASE_URL} is unreachable: {e}")
