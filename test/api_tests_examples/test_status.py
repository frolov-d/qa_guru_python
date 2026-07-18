import requests


def test_total_amount():
    response = requests.get("https://selenoid.autotests.cloud/status")
    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)

    data = response.json()
    print("Body:", data)

    total = data.get("state", {}).get("total")
    print("Total:", total)

    assert response.status_code == 200
    assert total == 20, f"Expected total 20, got {total}"