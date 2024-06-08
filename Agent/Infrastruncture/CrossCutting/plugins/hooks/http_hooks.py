from pluggy import HookspecMarker

hookspec = HookspecMarker("http")

@hookspec
async def call_api(job_data):
    pass
