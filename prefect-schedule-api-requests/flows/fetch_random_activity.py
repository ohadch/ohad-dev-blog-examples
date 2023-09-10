from prefect import flow, task


@task
def get_random_activity() -> str:
    """
    Get a random activity from the Bored API
    """
    import requests
    response = requests.get("https://www.boredapi.com/api/activity")
    return response.json()["activity"]


@task
def print_activity(activity: str) -> None:
    """
    Print the activity to the console
    :param activity: The activity to print
    """
    print(f"Today's activity is: {activity}")


@flow
def suggest_activity() -> None:
    """
    Suggest a random activity
    """
    activity = get_random_activity.submit()
    print_activity.submit(activity)


if __name__ == "__main__":
    suggest_activity()
