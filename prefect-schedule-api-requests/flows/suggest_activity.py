from prefect import flow, task
from prefect.artifacts import create_markdown_artifact


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
    print(f"The activity is: {activity}")


@task
def save_activity_artifact(activity: str) -> None:
    """
    Print the activity to the console
    :param activity: The activity to print
    """
    create_markdown_artifact(
        markdown=f"""
        Today, you should do the following activity: **{activity}**. 
        """,
        key="activity"
    )


@flow
def suggest_activity() -> None:
    """
    Suggest a random activity
    """
    activity = get_random_activity()
    print_activity(activity)
    save_activity_artifact(activity)


if __name__ == "__main__":
    suggest_activity()

    # If you want to visualize the flow, you can uncomment the following line:
    # suggest_activity.visualize()
