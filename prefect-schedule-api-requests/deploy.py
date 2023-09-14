import asyncio
from prefect.deployments import Deployment
from flows.suggest_activity import suggest_activity


async def main():
    # This line creates a deployment for the flow, which will be scheduled to run every day at 9:00 AM
    deployment = await Deployment.build_from_flow(
        name="Daily",
        flow=suggest_activity,
        work_pool_name="activities"
    )

    await deployment.apply()

    print("Deployment created!")


if __name__ == '__main__':
    asyncio.run(main())
