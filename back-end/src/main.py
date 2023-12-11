from fastapi import FastAPI
# import sentry_sdk

from routes import user_router, auth_router

# sentry_sdk.init(
#     dsn="https://f2b55ea07e5be52b2c66d045a1f66d40@o4506254438694912.ingest.sentry.io/4506254457438208",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)