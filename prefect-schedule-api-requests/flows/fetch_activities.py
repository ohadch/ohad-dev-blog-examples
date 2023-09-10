from prefect import flow, task


@task
def get_random_activity() -> str:
    """
    Fetches a random activity from the boredapi.
    :return: The activity.
    """
    import requests

    response = requests.get("https://www.boredapi.com/api/activity")
    return response.json()["activity"]


@task
def print_activity(activity: str) -> None:
    """
    Prints the activity.
    :param activity: The activity.
    """
    print(activity)


@flow
def random_activity_flow() -> None:
    """
    A flow that fetches a random activity from the boredapi and prints it.
    """
    activity = get_random_activity()
    print_activity(activity=activity)


if __name__ == "__main__":
    random_activity_flow()
